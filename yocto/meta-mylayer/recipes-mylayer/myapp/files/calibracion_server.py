# calibracion_server.py
import cv2
import socket
import struct
import pickle

def main():
    print("[*] Iniciando cámara...")
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("[X] No se pudo abrir la cámara.")
        return

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('0.0.0.0', 8000))
    s.listen(1)
    print("[*] Esperando conexión desde el cliente (Debian)...")
    conn, addr = s.accept()
    print(f"[+] Conectado desde: {addr}")

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            data = pickle.dumps(frame)
            msg = struct.pack("Q", len(data)) + data
            conn.sendall(msg)
    except Exception as e:
        print("[X] Error durante transmisión:", e)
    finally:
        cap.release()
        conn.close()
        print("[*] Cámara cerrada y conexión finalizada.")

if __name__ == "__main__":
    main()
