# Justificación

El proyecto propuesto tiene un gran potencial para mejorar la experiencia del espectador en las salas de cine. La aplicación permitiría recopilar datos sobre las reacciones emocionales de los espectadores ante diferentes tipos de escenas, lo que facilitaría el entrenamiento de nuevos modelos de aprendizaje automático más precisos y eficientes. Eso sería posible mediante esta adaptabilidad, ya que ayudaría a ofrecer recomendaciones personalizadas, como propuestas de película o cambio de género, basadas en el estado emocional del espectador. Es decir, si el sistema detectara señales de aburrimiento o desinterés, podría proponer una alternativa más próxima a sus gustos, con lo que su nivel de satisfacción aumentaría [1].

Desde una perspectiva social, este proyecto tiene implicaciones significativas en términos de inclusión, bienestar y accesibilidad. La capacidad de detectar emociones en tiempo real puede utilizarse para crear entornos más empáticos y receptivos, especialmente en contextos donde la expresión emocional puede estar limitada o inhibida. Por ejemplo, personas con condiciones que dificulten la comunicación verbal podrían beneficiarse de sistemas que interpreten su estado emocional y ajusten la interacción del entorno en consecuencia [2][3].

Desde el punto de vista técnico el principal reto consiste en integrar diversos componentes tecnológicos en un sistema compacto y eficiente de una Raspberry Pi. Esta se encargará de ejecutar las herramientas de visión por computadora con la ayuda de OpenCV, para procesar las imágenes en tiempo real. Además, se implementará un modelo de redes neuronales optimizado para dispositivos embebidos mediante TensorFlow Lite, lo que permite realizar el procesamiento local sin comprometer el rendimiento [4].

El sistema debe ser capaz de reconocer seis emociones básicas: ira, alegría, tristeza, miedo, asco y sorpresa. Se logra entrenar al realizarlo en redes neuronales profundas en bases de datos de imágenes faciales con gran volumen y etiquetadas. Para garantizar un procesamiento eficiente en dispositivos de bajo consumo, el modelo de red neuronal será optimizado o recortado para ejecutarse en dispositivos como la Raspberry Pi [5] que en muchos casos conlleva a consecuencias como la reducción la precisión o certeza del modelo.

Por otro lado, como norma se debe asegurar que el sistema cuente con mecanismos de seguridad y privacidad que garanticen que los datos capturados sean procesados de manera segura. Esto implica el uso de técnicas de encriptación para transmitir la información de manera protegida hacia un sistema de análisis local [6]. Además, la personalización del sistema operativo a través del uso de Yocto Project facilitará la creación de una imagen de sistema operativo optimizada y específica para el hardware de la Raspberry Pi 5, garantizando que todas las dependencias necesarias para el correcto funcionamiento del sistema [7].

La integración de sistemas de reconocimiento emocional en entornos como las salas de cine es un avance significativo en el campo de la interacción humano-máquina (HCI). Estos sistemas permiten adaptar dinámicamente la experiencia del usuario en función de su estado emocional, lo que favorece una comunicación más natural y empática entre el ser humano y la tecnología. En el contexto del entretenimiento, esto podría traducirse en una mayor inmersión y disfrute, ya que el contenido se ajusta automáticamente a las respuestas emocionales del espectador. Este enfoque se alinea con los postulados del affective computing, un área de la HCI que pretende endosar a los sistemas computacionales el algoritmo para reconocer, interpretar y responder a emociones humanas, y que por lo tanto mejora la calidad de interacción y la satisfacción del usuario [8].

Al considerar la utilización de tecnologías que monitorean emociones, se alude a beneficios potenciales por lo que respecta a la personalización y al bienestar, pero también se levantaron cuestiones al respecto de su impacto psicológico. La continua evaluación emocional puede tener efectos secundarios, como fatiga cognitiva, sensación de vigilancia o dependencia de validaciones externas por parte del sistema. Por otro lado, también se corre el riesgo de que los usuarios cambien su comportamiento de manera inconsciente al sentirse observados, lo que podría alterar la autenticidad de sus reacciones. Es necesario tener en cuenta estos factores para diseñar sistemas que no solo sean eficientes a nivel tecnológico, sino también emocionalmente sostenibles. Por lo tanto, corresponde el establecimiento de mecanismos de control, consentimiento informado y retroalimentación del usuario que fomenten una relación ética y saludable con estas tecnologías [9].

Por último este proyecto tiene futuro en el análisis emocional en salas de cine, que puede tener la capacidad de analizar emociones en tiempo real de espectadores y tener una personalización del contenido. Por último, el sistema es potencial para ser utilizado a otros campos de aplicación, tales como la educación o el bienestar mental, donde el seguimiento emocional tiene una influencia benefactora para el bienestar de las personas [10].


### Referencias

[1] Matsumoto, D., Hwang, H. S., López, R. M., & Pérez-Nieto, M. Á. (2013). Lectura de la expresión facial de las emociones: Investigación básica en la mejora del reconocimiento de emociones. Ansiedad y estrés.

[2] Lee, J. R. H., & Wong, A. (2020). AEGIS: A real-time multimodal augmented reality computer vision based system to assist facial expression recognition for individuals with autism spectrum disorder.

[3] Khanzada, A., Bai, C., & Celepcikay, F. T. (2020). Facial expression recognition with deep learning.

[4] R. Turabzadeh, L. Meng, S. Swash, M. Pleva, and M. Juhar, "Optimizing neural networks for embedded systems: TensorFlow Lite and Raspberry Pi," Embedded Systems Journal, vol. 13, no. 2, pp. 75-88, 2017.

[5] J. Wang, M. Chen, and H. Zhao, "Facial emotion recognition using deep learning techniques," IEEE Transactions on Artificial Intelligence, vol. 5, no. 2, pp. 56-65, 2021.

[6] Y. Wang, Z. Liu, and X. Yang, "Data security in real-time emotion recognition systems," Journal of Information Security, vol. 34, no. 1, pp. 101-110, 2021.

[7] T. Cheng, X. Zhang, and P. Yang, "Yocto Project for embedded system customization," IEEE Embedded Systems Conference, pp. 45-51, 2017.

[8] Picard, R. W. (1997). Affective Computing. MIT Press.

[9] Calvo, R. A., & D'Mello, S. (2010). Affect detection: An interdisciplinary review of models, methods, and their applications. IEEE Transactions on Affective Computing, 1(1), 18–37. https://doi.org/10.1109/T-AFFC.2010.1

[10] A. T. Nelson, J. A. Glickman, and P. Sharma, "Scalable emotion recognition: Applications in education and mental health," IEEE Transactions on Affective Computing, vol. 12, no. 3, pp. 99-110, 2023.
