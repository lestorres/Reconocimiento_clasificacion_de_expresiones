import sys
import csv
from collections import Counter

# Asegura que matplotlib use el backend adecuado para PyQt5
import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt

from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog, QMessageBox
from ventana_ui import Ui_Dialog  # Asegúrate de haber generado esto con pyuic5

class Ventana(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ruta_csv = ""

        # Conectar botones
        self.ui.pushButton_2.clicked.connect(self.seleccionar_csv)  # Botón "Cargar CSV"
        self.ui.pushButton.clicked.connect(self.mostrar_graficas)   # Botón "Graficar"

    def seleccionar_csv(self):
        archivo, _ = QFileDialog.getOpenFileName(
            self, "Seleccionar archivo CSV", "", "Archivos CSV (*.csv)"
        )
        if archivo:
            self.ruta_csv = archivo
        else:
            QMessageBox.warning(self, "Advertencia", "No se seleccionó ningún archivo.")

    def lector_csv(self, filename):
        emociones = []
        try:
            with open(filename, 'r', encoding='utf-8') as archivo:
                lector = csv.reader(archivo)
                next(lector, None)  # Saltar encabezado
                for fila in lector:
                    if fila and len(fila) > 1:
                        emociones.append(fila[1].strip())
            return Counter(emociones)
        except Exception as e:
            raise RuntimeError(f"No se pudo leer el archivo: {e}")

    def mostrar_graficas(self):
        if not self.ruta_csv:
            QMessageBox.warning(self, "Error", "Primero debes seleccionar un archivo CSV.")
            return

        try:
            conteo = self.lector_csv(self.ruta_csv)
            if not conteo:
                QMessageBox.information(self, "Sin datos", "No se encontraron emociones en el archivo.")
                return
            self.graficas_juntas(conteo)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Ocurrió un error al procesar el archivo:\n{e}")

    def graficas_juntas(self, conteo):
        labels = list(conteo.keys())
        counts = list(conteo.values())

        fig, axs = plt.subplots(1, 2, figsize=(14, 6))

        axs[0].pie(counts, labels=labels, autopct='%1.1f%%', startangle=90)
        axs[0].set_title('Distribución de Emociones')
        axs[0].axis('equal')

        axs[1].bar(labels, counts, color='skyblue')
        axs[1].set_title('Conteo de emociones')
        axs[1].set_xlabel('Emoción')
        axs[1].set_ylabel('Cantidad')
        axs[1].tick_params(axis='x', rotation=45)

        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.setWindowTitle("Visualizador de Emociones")
    ventana.show()
    sys.exit(app.exec_())
