import numpy as np
from PIL import Image
import tflite_runtime.interpreter as tflite

# Cargar la imagen
image_path = "/usr/bin/myapp/test_image.png"
image = Image.open(image_path).convert('L')  # Convertir a escala de grises
image = image.resize((48, 48))               # Redimensionar a 48x48

# Convertir a numpy array y normalizar
input_data = np.asarray(image, dtype=np.float32)
input_data = input_data / 255.0
input_data = input_data.reshape(1, 48, 48, 1)

# Cargar el modelo TFLite
interpreter = tflite.Interpreter(model_path="/usr/bin/myapp/model/ferplus_model_pd_best.tflite")
interpreter.allocate_tensors()

# Obtener los detalles de los tensores
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Asignar entrada y ejecutar
interpreter.set_tensor(input_details[0]['index'], input_data)
interpreter.invoke()

# Obtener resultados
output_data = interpreter.get_tensor(output_details[0]['index'])[0]

# Lista de emociones según el modelo FER+
emotions = ['neutral', 'happy', 'sad', 'surprise', 'anger']
predicted_index = np.argmax(output_data)
predicted_emotion = emotions[predicted_index]

print(f"Emoción predicha: {predicted_emotion} (probabilidad: {output_data[predicted_index]:.2f})")
