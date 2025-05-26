import time
import random
import subprocess
from datetime import datetime
import csv
import os

# Emociones simuladas
EMOCIONES = ["Enojo", "Disgusto", "Miedo", "Felicidad", "Tristeza", "Sorpresa"]

# Configuración del PC remoto
USUARIO_PC = "lesmes"
IP_PC = "192.168.100.1"
RUTA_DESTINO_PC = "/home/lesmes/Desktop/emociones_recibidas.csv"

# Ruta temporal local
ARCHIVO_LOCAL = "/tmp/emociones.csv"

# Duración de la simulación (en segundos)
DURACION = 30  # puedes ajustar este valor según lo necesites

# Recolectar emociones detectadas
datos = []

print(" Iniciando simulación de emociones...")
for _ in range(DURACION):
    emocion = random.choice(EMOCIONES)
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    datos.append([timestamp, emocion])
    print(f"{timestamp} - {emocion}")
    time.sleep(1)

# Guardar CSV en /tmp
with open(ARCHIVO_LOCAL, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Hora", "Emocion"])
    writer.writerows(datos)

print(f"\n Archivo CSV guardado localmente en: {ARCHIVO_LOCAL}")

# Enviar el archivo por SCP al PC remoto
comando_scp = f"scp {ARCHIVO_LOCAL} {USUARIO_PC}@{IP_PC}:{RUTA_DESTINO_PC}"

try:
    subprocess.run(comando_scp, shell=True, check=True)
    print(f" Archivo enviado exitosamente a: {USUARIO_PC}@{IP_PC}:{RUTA_DESTINO_PC}")
except subprocess.CalledProcessError:
    print(" Error al enviar el archivo CSV por SSH/SCP")
