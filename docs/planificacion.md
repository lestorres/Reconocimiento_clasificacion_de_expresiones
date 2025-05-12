# Planificación
Para garantizar una ejecución ordenada y efectiva del proyecto, se realizó una planificación estructurada que contempla la asignación de roles, la división de tareas y la definición de entregables asociados a cada fase del desarrollo. Esta planificación está representada en un diagrama de Gantt, el cual permite visualizar la secuencia lógica y temporal de las actividades. A continuación, se presenta la lista de tareas principales que guiarán el desarrollo del sistema embebido:

- Revisión técnica y conceptual del problema: Esta etapa inicial está orientada a comprender en profundidad los objetivos del proyecto, las emociones a clasificar, y los requisitos funcionales y no funcionales del sistema. Incluye además el estudio preliminar de las tecnologías involucradas.
- Diseño y documentación de la propuesta técnica: Se elabora el documento de propuesta de diseño, el cual define la arquitectura general del sistema, los componentes a integrar, y los criterios de operación bajo un esquema de Edge AI.
- Desarrollo inicial del modelo de clasificación de emociones: Se implementa un modelo de reconocimiento facial de emociones en Python, utilizando un entorno de escritorio como plataforma de prueba. Esta versión permitirá validar la lógica del modelo y realizar ajustes antes de optimizarlo.
- Incorporación de funcionalidad de registro: Se añade al sistema la capacidad de registrar los resultados de la clasificación junto con sus respectivas marcas de tiempo, en un formato estructurado para facilitar su análisis posterior.
- Conversión y validación del modelo con TensorFlow Lite: El modelo desarrollado se convierte a TensorFlow Lite para reducir su tamaño y mejorar su rendimiento en entornos con recursos limitados. Posteriormente se realizan pruebas de compatibilidad y precisión.
- Configuración de capas Yocto necesarias para el sistema: Se configuran e integran las capas meta-tensorflow-lite, meta-openembedded, meta-python y meta-raspberrypi, necesarias para compilar una imagen personalizada de Linux compatible con Raspberry Pi y con las dependencias requeridas.
- Desarrollo de capa personalizada meta-edgeAI: Se crea una capa específica que contenga tanto el modelo convertido como el código necesario para ejecutarlo dentro del sistema embebido.
- Generación y prueba de la imagen embebida en entorno virtual: Se genera la imagen del sistema operativo mediante Yocto y se prueba en un entorno de máquina virtual utilizando videos como insumo para simular la entrada de cámara.
- Despliegue y verificación en hardware físico: La imagen generada se despliega en una Raspberry Pi 4, conectada a una cámara. Se valida el funcionamiento del sistema en condiciones reales, verificando detección, registro y procesamiento local.
- Implementación de la comunicación remota: Se establece un canal de comunicación seguro entre la Raspberry Pi y un equipo remoto utilizando SSH, permitiendo la transferencia de reportes y el control del sistema de forma externa.
- Desarrollo de una interfaz operativa básica: Se crea una interfaz de usuario simple que facilite el arranque, monitoreo y cierre del sistema, así como la consulta de los reportes generados.
- Integración final y pruebas completas del sistema: Se realiza una verificación integral que incluya detección en tiempo real, registro local, comunicación remota, y funcionamiento continuo en la Raspberry Pi, asegurando la coherencia con los objetivos del proyecto.

<p align="center">
  <img src="imag/diagrama.jpg"  width="500"/>
</p>
