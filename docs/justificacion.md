# Justificación

El proyecto propuesto tiene un gran potencial para mejorar la experiencia del espectador en las salas de cine. La aplicación permitiría recopilar datos sobre las reacciones emocionales de los espectadores ante diferentes tipos de escenas, lo que facilitaría el entrenamiento de nuevos modelos de aprendizaje automático más precisos y eficientes. Esta capacidad de adaptación permitiría ofrecer recomendaciones personalizadas, como sugerencias de películas o cambios de género, en función del estado emocional del espectador. Por ejemplo, si el sistema detecta señales de aburrimiento o desinterés, podría recomendar una alternativa más acorde con las preferencias del usuario, mejorando así su nivel de satisfacción [1].

Desde una perspectiva social, este proyecto tiene implicaciones significativas en términos de inclusión, bienestar y accesibilidad. La capacidad de detectar emociones en tiempo real puede utilizarse para crear entornos más empáticos y receptivos, especialmente en contextos donde la expresión emocional puede estar limitada o inhibida. Por ejemplo, personas con condiciones que dificulten la comunicación verbal podrían beneficiarse de sistemas que interpreten su estado emocional y ajusten la interacción del entorno en consecuencia [2][3].

Desde el punto de vista técnico el principal reto consiste en integrar diversos componentes tecnológicos en un sistema compacto y eficiente de una Raspberry Pi. Esta se encargará de ejecutar las herramientas de visión por computadora con la ayuda de OpenCV, para procesar las imágenes en tiempo real. Además, se implementará un modelo de redes neuronales optimizado para dispositivos embebidos mediante TensorFlow Lite, lo que permite realizar el procesamiento local sin comprometer el rendimiento [4].

El sistema tiene como requisito ser capaz de reconocer seis emociones básicas: enojo, felicidad, tristeza, miedo, disgusto y sorpresa. Este reconocimiento se logra mediante el entrenamiento de redes neuronales profundas en bases de datos con grandes volúmenes de imágenes faciales etiquetadas. Para garantizar un procesamiento eficiente en dispositivos de bajo consumo, el modelo de red neuronal será optimizado o recortado para ejecutarse en dispositivos como la Raspberry Pi [5] que en muchos casos conlleva a consecuencias como la reducción la precisión o certeza del modelo.

Por otro lado, como norma se debe asegurar que el sistema cuente con mecanismos de seguridad y privacidad que garanticen que los datos capturados sean procesados de manera segura. Esto implica el uso de técnicas de encriptación para transmitir la información de manera protegida hacia un sistema de análisis local [6]. Además la personalización del sistema operativo a través del uso de Yocto Project permitirá crear una imagen de sistema operativo adaptada y optimizada para el hardware de la Raspberry Pi 5, garantizando que todas las dependencias necesarias para el funcionamiento del sistema [7].

Finalmente este proyecto tiene aplicaciones en el análisis emocional en salas de cine, que tiene la capacidad de analizar las reacciones emocionales en tiempo real de los espectadores y permitir una personalización del contenido. Además, el sistema tiene un potencial de ser aplicado a otros sectores, como la educación o la salud mental, donde la monitorización emocional tiene un impacto positivo en el bienestar de los individuos [8].



### Referencias

[1] Matsumoto, D., Hwang, H. S., López, R. M., & Pérez-Nieto, M. Á. (2013). Lectura de la expresión facial de las emociones: Investigación básica en la mejora del reconocimiento de emociones. Ansiedad y estrés, 19.

[2] Lee, J. R. H., & Wong, A. (2020). AEGIS: A real-time multimodal augmented reality computer vision based system to assist facial expression recognition for individuals with autism spectrum disorder.

[3] Khanzada, A., Bai, C., & Celepcikay, F. T. (2020). Facial expression recognition with deep learning.

[4] R. Turabzadeh, L. Meng, S. Swash, M. Pleva, and M. Juhar, "Optimizing neural networks for embedded systems: TensorFlow Lite and Raspberry Pi," Embedded Systems Journal, vol. 13, no. 2, pp. 75-88, 2017.

[5] J. Wang, M. Chen, and H. Zhao, "Facial emotion recognition using deep learning techniques," IEEE Transactions on Artificial Intelligence, vol. 5, no. 2, pp. 56-65, 2021.

[6] Y. Wang, Z. Liu, and X. Yang, "Data security in real-time emotion recognition systems," Journal of Information Security, vol. 34, no. 1, pp. 101-110, 2021.

[7] T. Cheng, X. Zhang, and P. Yang, "Yocto Project for embedded system customization," IEEE Embedded Systems Conference, pp. 45-51, 2017.

[8] A. T. Nelson, J. A. Glickman, and P. Sharma, "Scalable emotion recognition: Applications in education and mental health," IEEE Transactions on Affective Computing, vol. 12, no. 3, pp. 99-110, 2023.
