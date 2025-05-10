# Reconocimiento_clasificacion_de_expresiones
II Proyecto: EdgeAI - Sistema Embebido para el reconocimiento y clasificación de expresiones faciales



# 📡 Propuesta de Diseño: Sistema Embebido para Análisis de Emociones en una Sala de Cine

## 1. Justificación

Explique aquí la motivación del proyecto, su relevancia tecnológica, impacto social, y beneficios esperados del uso de edge computing e inteligencia artificial en contextos inmersivos como una sala de cine.

## 2. Descripción y Síntesis del Problema

Describa claramente el problema a resolver. Incluya:
- El contexto (sala de cine)
- La necesidad de evaluar emociones de manera no invasiva
- El rol del sistema embebido
- El uso de nodos camuflados y procesamiento local con Raspberry Pi

## 3. Gestión de los Requerimientos

Especifique los requerimientos del sistema, incluyendo:
- **Funcionales** (detección de emociones, procesamiento local, comunicación)
- **No funcionales** (latencia, privacidad, precisión, consumo de energía)

Puede usar tablas como:

| Tipo | Requerimiento | Descripción |
|------|----------------|-------------|
| Funcional | Detección de emociones | Reconocer 6 emociones básicas |
| No funcional | Privacidad | No almacenar rostros ni datos identificables |

## 4. Vista Operacional del Sistema

Explique cómo funcionará el sistema en operación real, incluyendo:
- Instalación física de los nodos
- Flujo de datos: Captura → Procesamiento → Clasificación → Envío
- Interacción con otros sistemas (servidor central, visualización de datos)

## 5. Vista Funcional del Sistema

Describa los módulos y funciones clave del sistema. Ejemplo:
- Captura de imagen
- Preprocesamiento de datos
- Modelo de inferencia (clasificador de emociones)
- Comunicación con servidor

## 6. Arquitectura del Sistema Propuesto

Incluya un diagrama (puede indicarse como pendiente) y explique:
- Componentes hardware (Raspberry Pi, cámara, red)
- Software embebido (sistema operativo, librerías, AI model)
- Flujo de datos entre módulos

## 7. Análisis de Dependencias

Detalle:
- Hardware requerido
- Librerías de procesamiento de imágenes y machine learning (OpenCV, TensorFlow Lite, etc.)
- Conectividad (WiFi, MQTT, HTTP)
- Compatibilidad entre componentes

## 8. Estrategia de Integración de la Solución

Describa cómo se integrarán los distintos componentes del sistema:
- Pruebas en entorno controlado
- Integración progresiva en la sala
- Validación del funcionamiento distribuido

## 9. Planeamiento de la Ejecución

Proporcione una tabla de fases con tiempos estimados:

| Fase | Actividades | Duración Estimada |
|------|-------------|-------------------|
| Fase 1 | Levantamiento de requerimientos y diseño | 2 semanas |
| Fase 2 | Desarrollo e integración de nodos | 4 semanas |
| Fase 3 | Pruebas piloto en sala de cine | 2 semanas |

## 10. Conclusiones y Aspectos Relevantes

Resuma los puntos fuertes de la propuesta, como:
- Uso de edge computing para eficiencia
- Enfoque no invasivo
- Potencial para ser escalable o aplicable en otros contextos

---

**📌 Nota:** Puedes agregar diagramas o imágenes utilizando la sintaxis `![Descripción](ruta/imagen.png)` y mejorar la presentación con tablas y listas.

