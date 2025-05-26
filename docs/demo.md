# Introducción
En la actualidad, la inteligencia artificial en el borde (Edge AI) está transformando la forma en que los dispositivos interactúan con el mundo en tiempo real. Este proyecto explora la implementación de un sistema autónomo de reconocimiento de emociones basado en visión por computadora, ejecutado localmente en una Raspberry Pi 5. Utilizando el entorno de desarrollo embebido Yocto Project, se personalizó una imagen ligera que integra herramientas como TensorFlow Lite, OpenCV y Python, permitiendo el análisis de expresiones faciales captadas por una cámara sin necesidad de conexión a internet. Esta solución busca ser eficiente, portable y adaptable a diversos entornos, como salas de cine, instalaciones educativas o espacios de interacción emocional.

# Objetivo del Proyecto
Diseñar e implementar un sistema embebido de bajo costo que permita detectar emociones humanas en tiempo real a partir de imágenes faciales, utilizando técnicas de Edge AI sobre una Raspberry Pi 5 con un sistema operativo personalizado generado mediante Yocto Project.

# Resumen
Este proyecto presenta el desarrollo de un sistema de inteligencia artificial en el borde para la detección de emociones a través de visión por computadora. El sistema se construyó sobre una Raspberry Pi 5, utilizando una imagen personalizada del sistema operativo generada con Yocto Project, en la cual se integraron TensorFlow Lite, OpenCV y Python. Se logró la captura de imágenes mediante una cámara UVC estándar y la inferencia local de emociones faciales en tiempo real sin conexión a la nube. El sistema se diseñó para operar de forma autónoma y eficiente, siendo ideal para aplicaciones donde la privacidad y la baja latencia son esenciales. La propuesta demuestra el potencial del Edge AI en dispositivos de bajo consumo para análisis emocional, interacción humano-máquina y ambientes adaptativos.


# Conclusiones
Este proyecto logró implementar una solución funcional de inteligencia artificial en el borde (Edge AI) para el reconocimiento de emociones en tiempo real mediante una cámara conectada a una Raspberry Pi 5. Utilizando una imagen personalizada generada con el sistema de compilación Yocto Project, se integraron herramientas como TensorFlow Lite, OpenCV y Python, manteniendo un entorno ligero, optimizado y autónomo.

Es importante destacar que el uso de Yocto demostró ser clave para personalizar sistemas embebidos con alto nivel de control, aunque exige una curva de aprendizaje considerable. Se validó que la inteligencia artificial en el borde es factible en hardware como la Raspberry Pi 5 si se emplean modelos optimizados y herramientas ligeras como TensorFlow Lite. Además, quedó clara la importancia de la modularidad y personalización para lograr sistemas autónomos, eficientes y adaptados a entornos con recursos limitados.

## Principales logros:
- Integración eficiente con Yocto Project:
	Se logró crear una imagen personalizada para Raspberry Pi 5 incluyendo solo los paquetes necesarios (TensorFlow Lite, OpenCV, Python, etc.), lo cual redujo el tamaño del sistema y mejoró el rendimiento.

- Ejecución local sin conexión a la nube:
	El modelo de reconocimiento facial y clasificación de emociones funciona completamente en el dispositivo, lo que garantiza privacidad, baja latencia y autonomía frente a la nube.

- Conexión remota y operación headless:
	Se configuró con éxito la conexión Ethernet entre la PC y la Raspberry Pi para interacción vía SSH, lo que facilita el despliegue y monitoreo sin necesidad de pantalla o teclado en el dispositivo.

- Uso de cámara UVC estándar:
	Se aprovechó la compatibilidad UVC de una webcam Logitech C170 para capturar imágenes de forma inmediata y sin necesidad de drivers propietarios, facilitando la portabilidad del sistema.

- Flujo completo de Edge AI:
	Desde la captura de imágenes, el preprocesamiento, la inferencia con TensorFlow Lite hasta la visualización de resultados se realiza en tiempo real, mostrando la viabilidad del enfoque Edge AI.


