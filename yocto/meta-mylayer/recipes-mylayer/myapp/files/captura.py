import cv2

cap = cv2.VideoCapture(0)  # Usa /dev/video0 por defecto
ret, frame = cap.read()

if ret:
    cv2.imwrite("captura.jpg", frame)

cap.release()
