# Requerimientos

Entre los Requerimientos funcionales del sistema a implementar, se debe cumplir con lo siguiente:

## ✅ 1. Requerimientos Funcionales (RF)
| ID  | Nombre                        | Descripción                                                                                     |
| --- | ----------------------------- | ----------------------------------------------------------------------------------------------- |
| RF1 | Captura de imágenes           | El sistema debe capturar imágenes de los rostros de los espectadores utilizando una cámara USB. |
| RF2 | Clasificación de emociones    | El sistema debe clasificar emociones en enojo, disgusto, miedo, felicidad, tristeza y sorpresa. |
| RF3 | Procesamiento local (Edge AI) | El procesamiento de imágenes y clasificación debe realizarse localmente en la Raspberry Pi 5.   |
| RF4 | Almacenamiento de resultados  | El sistema debe almacenar los resultados de la clasificación por nodo con marca temporal.       |
| RF5 | Comunicación en red           | Los nodos deben enviar sus resultados a un servidor central de manera periódica.                |
| RF6 | No intrusión al ambiente      | El sistema no debe perturbar la experiencia de los espectadores ni ser visualmente evidente.    |
| RF7 | Visualización remota         | El sistema debe permitir la visualización de los resultados de emociones desde una interfaz en un servidor o PC. |


## ✅ 2. Requerimientos No Funcionales (RNF)
Es importante aclarar que los **Requerimientos No Funcionales** hacen referencias a **restricciones o características de calidad que debe cumplir el sistema**, siendo "una métrica" para evaluar el rendimiento del sistema empleado. 
| ID   | Nombre                     | Descripción                                                                 |
| ---- | -------------------------- | --------------------------------------------------------------------------- |
| RNF1 | Tiempo de respuesta        | El sistema debe clasificar emociones en menos de 2 segundos por imagen.     |
| RNF2 | Precisión del modelo       | El modelo de emociones debe tener al menos 80% de precisión en validación.  |
| RNF3 | Uso de recursos limitado   | El sistema debe funcionar con un máximo del 70% de CPU y 512 MB de RAM.     |
| RNF4 | Portabilidad               | El sistema debe ser desplegable en Raspberry Pi 5.                          |
| RNF5 | Privacidad de los usuarios | No se debe almacenar imágenes completas ni datos personales identificables. |
| RNF6 | Requerimientos de energía   | Cada nodo debe poder alimentarse con una fuente de 5V 3A mediante USB-C. |


## ✅ 3. Requerimientos del Sistema (Hardware y Software)
Entre lo planeado para el hardware a utilizar se proponen los siguientes elementos:

| Tipo          | Requerimiento                                                                                                                                                                                         |
| ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Hardware**  | - Raspberry Pi 5 (8GB RAM)  <br> - Webcam USB tipo UVC  <br> - Fuente de alimentación 5V 3A USB-C <br> - Conectividad Wi-Fi o Ethernet                                       |
| **Software**  | - Linux embebido generado con **Yocto Project** <br> - Python 3.10+ <br> - OpenCV 4+ <br> - TensorFlow Lite (tflite-runtime) <br> - Sistema de comunicación cliente-servidor para envío de resultados |
| **Bibliotecas** | - Numpy <br> - OpenCV <br> - TensorFlow Lite Runtime <br> - imutils <br> - PyUSB (opcional para gestión de dispositivos USB)                                                                          |
| **Dataset**   | - Bases de datos de emociones faciales etiquetadas como:  <br> → FER2013  <br> → RAF-DB  <br> → CK+ (Cohn-Kanade+)                                                                                    |


