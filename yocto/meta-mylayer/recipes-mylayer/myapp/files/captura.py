import cv2
import numpy as np
from PIL import Image
from datetime import datetime
import csv
import time
import subprocess
import os
import signal
import sys
from tflite_runtime.interpreter import Interpreter

# Emociones según modelo FER+
EMOCIONES = ['neutral', 'happy', 'sad', 'surprise', 'anger']

# Configuración de rutas
ARCHIVO_LOCAL = "/usr/bin/myapp/emociones.csv"
USUARIO_PC = "lesmes"
IP_PC = "192.168.100.1"
RUTA_DESTINO_PC = "/home/lesmes/Desktop/emociones.csv"
MODELO_TFLITE = "/usr/bin/myapp/model/ferplus_model_pd_best.tflite"

# Inicializar modelo
interpreter = Interpreter(model_path=MODELO_TFLITE)
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Abrir cámara
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print(f"[X] No se pudo abrir la cámara.")
    sys.exit(1)

# Lista para guardar resultados
datos = []

def guardar_csv():
    with open(ARCHIVO_LOCAL, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Hora", "Emocion", "Probabilidad"])
        writer.writerows(datos)
    print(f"\n[:] Archivo CSV guardado en: {ARCHIVO_LOCAL}")

def enviar_csv():
    comando_scp = f"scp {ARCHIVO_LOCAL} {USUARIO_PC}@{IP_PC}:{RUTA_DESTINO_PC}"
    try:
        subprocess.run(comando_scp, shell=True, check=True)
        print(f"[:] Archivo enviado a: {USUARIO_PC}@{IP_PC}:{RUTA_DESTINO_PC}")
    except subprocess.CalledProcessError:
        print("[X] Error al enviar el archivo CSV")

def manejar_salida(sig, frame):
    print("\n[!] Interrupción recibida. Guardando y enviando datos...")
    cap.release()
    guardar_csv()
    enviar_csv()
    sys.exit(0)

signal.signal(signal.SIGINT, manejar_salida)

print("[-->] Procesando emociones desde la cámara (Ctrl+C para cancelar)...\n")
try:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("[X] No se pudo leer el frame de la cámara.")
            break

        # Convertir a escala de grises y redimensionar
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        image = Image.fromarray(gray).resize((48, 48))
        input_data = np.asarray(image, dtype=np.float32) / 255.0
        input_data = input_data.reshape(1, 48, 48, 1)

        # Ejecutar inferencia
        interpreter.set_tensor(input_details[0]['index'], input_data)
        interpreter.invoke()
        output_data = interpreter.get_tensor(output_details[0]['index'])[0]

        # Emoción más probable
        idx = np.argmax(output_data)
        emocion = EMOCIONES[idx]
        probabilidad = output_data[idx]
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        datos.append([timestamp, emocion, f"{probabilidad:.2f}"])
        print(f"{timestamp} - {emocion} ({probabilidad:.2f})")

        time.sleep(1)

except Exception as e:
    print(f"[X] Error inesperado: {e}")
    manejar_salida(None, None)

# Al salir normalmente (aunque Ctrl+C lo maneja arriba)
manejar_salida(None, None)
