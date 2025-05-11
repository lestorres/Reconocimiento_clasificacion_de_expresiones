# Vista Funcional
En esta apartado se analizará la interacción de los componentes del sistema y sus funciones clave.

## 1. Entrada: Captura de Datos
**Función**: La cámara captura imágenes de los rostros de los espectadores.

**Dispositivo**: Cámara USB (tipo UVC) conectada a la Raspberry Pi.

**Descripción**: Las imágenes deben ser procesadas en tiempo real para no interferir con la experiencia del espectador y la cámara debe estar posicionada discretamente para capturar solo las expresiones faciales sin invadir el espacio del espectador.

## 2. Preprocesamiento y Procesamiento de Imágenes
**Función**: El sistema realiza un preprocesamiento básico de las imágenes (redimensionamiento, conversión a escala de grises, etc.) para optimizar la clasificación de emociones.

**Software**: OpenCV para el procesamiento inicial de imágenes.

**Descripción**: Las imágenes se preparan para la clasificación utilizando un modelo de aprendizaje automático **Edge AI**.

## 3. Clasificación de Emociones 
**Función**: Este será el modelo de inteligencia artificial a utilizar, este ejecutará localmente en la Raspberry Pi con TensorFlow Lite y clasificará las emociones de los espectadores.

**Modelo**: Se utiliza un modelo entrenado con una base de datos como FER2013, RAF-DB, o CK+.

**Emociones clasificadas**: Enojo, disgusto, miedo, felicidad, tristeza y sorpresa.

**Descripción**: El modelo realiza la clasificación en menos de 2 segundos por imagen. El procesamiento es realizado en la propia Raspberry Pi 5, aprovechando la capacidad de **Edge AI** para evitar la latencia asociada a la comunicación con servidores externos.

## 4. Almacenamiento y Registro de Resultados
**Función**: Los resultados de la clasificación se almacenan localmente con una marca temporal en la Raspberry Pi.

**Descripción**: La información será almacenada en de manera local en archivos de registro para su posterior análisis y evaluación.

## 5. Comunicación y Envío de Datos
**Función**: Los resultados de la clasificación se envían de forma periódica al sistema de visualización a través de la red local (Wi-Fi o Ethernet).

**Protocolo**: Los datos pueden ser enviados mediante un protocolo de comunicación como HTTP, MQTT o WebSocket.

**Descripción**: La comunicación debe ser eficiente y no debe afectar el rendimiento de la Raspberry Pi.

## 6. Visualización de Datos
**Función**: El sistema central recibe los datos y los muestra en una interfaz gráfica para su análisis.

**Software**: Se puede utilizar una plataforma de visualización como Grafana, Kibana o una aplicación web personalizada.

**Descripción**: Los datos deben presentarse de manera clara y accesible, permitiendo a los operadores o responsables del análisis ver las emociones de los espectadores en tiempo real o a posteriori.

---

# Diagrama de Flujo Funcional:

Captura de Imágenes

→ Cámara USB → (Captura imágenes) → Raspberry Pi

Preprocesamiento de Imágenes

Raspberry Pi → (Preprocesa imágenes con OpenCV) → TensorFlow Lite

Clasificación de Emociones (Edge AI)

Raspberry Pi → (Clasificación de emociones) → TensorFlow Lite

Almacenamiento de Resultados

Raspberry Pi → (Almacena resultados con marca temporal)

Envío de Datos a Servidor

Raspberry Pi → (Envía resultados por Wi-Fi/Ethernet) → Servidor Central

Visualización en la Interfaz

Servidor Central → (Muestra resultados en interfaz gráfica)
