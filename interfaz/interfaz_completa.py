import sys
import csv
from collections import Counter
import matplotlib
matplotlib.use('Qt5Agg')

import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog, QMessageBox
import subprocess
import os
from ventana_ui import Ui_Dialog  # Asegúrate de tener este archivo generado por pyuic5


class Ventana(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ruta_csv = ""
        self.proceso = None

        # Conectar botones
        self.ui.pushButton_2.clicked.connect(self.seleccionar_csv)  # Cargar CSV
        self.ui.pushButton.clicked.connect(self.mostrar_graficas)   # Graficar
        self.ui.pushButton_3.clicked.connect(self.ejecutar_captura)  # Play
        self.ui.pushButton_4.clicked.connect(self.detener_proceso)   # Stop
        self.ui.pushButton_5.clicked.connect(self.ejecutar_calibracion)  # Calibración

    def seleccionar_csv(self):
        archivo, _ = QFileDialog.getOpenFileName(self, "Seleccionar archivo CSV", "", "Archivos CSV (*.csv)")
        if archivo:
            self.ruta_csv = archivo
        else:
            QMessageBox.warning(self, "Advertencia", "No se seleccionó ningún archivo.")

    def lector_csv(self, filename):
        emociones = []
        with open(filename, 'r', encoding='utf-8') as archivo:
            lector = csv.reader(archivo)
            next(lector, None)
            for fila in lector:
                if fila and len(fila) > 1:
                    emociones.append(fila[1])
        return Counter(emociones)

    def mostrar_graficas(self):
        if not self.ruta_csv:
            QMessageBox.warning(self, "Error", "Primero debes seleccionar un archivo CSV.")
            return
        try:
            conteo = self.lector_csv(self.ruta_csv)
            self.graficas_juntas(conteo)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Ocurrió un error al procesar el archivo:\n{e}")

    def graficas_juntas(self, conteo):
        labels = list(conteo.keys())
        counts = list(conteo.values())

        fig, axs = plt.subplots(1, 2, figsize=(14, 6))

        axs[0].pie(counts, labels=labels, autopct='%1.1f%%', startangle=90,
                   colors=['gold', 'lightcoral', 'tomato', 'lightblue', 'green'])
        axs[0].set_title('Distribución de Emociones')
        axs[0].axis('equal')

        axs[1].bar(labels, counts, color='skyblue')
        axs[1].set_title('Conteo de emociones')
        axs[1].set_xlabel('Emoción')
        axs[1].set_ylabel('Cantidad')
        axs[1].tick_params(axis='x', rotation=45)

        plt.tight_layout()
        plt.show()

    def ejecutar_captura(self):
        if self.proceso is None:
            try:
                comando = (
                    'lxterminal -e bash -c "ssh root@192.168.100.2 \'python3 -u /usr/bin/myapp/captura.py\'; '
                    'echo Presiona Enter para salir...; read"'
                )
                self.proceso = subprocess.Popen(comando, shell=True)
                QMessageBox.information(self, "Éxito", "Captura iniciada en terminal externa.")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"No se pudo iniciar la captura:\n{e}")
        else:
            QMessageBox.warning(self, "Advertencia", "La captura ya está en ejecución.")

    def ejecutar_calibracion(self):
        if self.proceso is None:
            try:
                comando = (
                    'lxterminal -e bash -c "ssh root@192.168.100.2 \'python3 -u /usr/bin/myapp/calibracion_server.py\'; '
                    'echo Presiona Enter para salir...; read"'
                )
                self.proceso = subprocess.Popen(comando, shell=True)
                QMessageBox.information(self, "Éxito", "Calibración iniciada en terminal externa.")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"No se pudo iniciar la calibración:\n{e}")
        else:
            QMessageBox.warning(self, "Advertencia", "Ya hay un proceso en ejecución.")

    def detener_proceso(self):
        try:
            # Buscar PIDs de captura.py y calibracion_server.py en la Raspberry
            buscar_pid_cmd = (
                'ssh root@192.168.100.2 '
                '"pgrep -f captura.py; pgrep -f calibracion_server.py"'
            )
            resultado = subprocess.run(buscar_pid_cmd, shell=True, capture_output=True, text=True)
            pids = resultado.stdout.strip().split('\n')

            if pids and pids != ['']:
                for pid in pids:
                    # Enviar señal SIGINT (2) para permitir finalización limpia
                    kill_cmd = f'ssh root@192.168.100.2 kill -2 {pid}'
                    subprocess.run(kill_cmd, shell=True)
                self.proceso = None
                QMessageBox.information(self, "Éxito", "Proceso(s) detenido(s) en Raspberry PI.")
            else:
                QMessageBox.information(self, "Info", "No se encontraron procesos activos para detener.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo detener el proceso:\n{e}")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.setWindowTitle("Visualizador de Emociones")
    ventana.show()
    sys.exit(app.exec_())
