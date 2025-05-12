# Integración

El diagrama de la arquitectura integrada de software y hardware es: 

```mermaid
flowchart TB
    subgraph Espectador
        P[😃 Reacción del Espectador]
    end

    subgraph Camara USB
        A[🎥 Captura de imágenes]
    end

    subgraph Raspberry Pi 5
        B[🧠 Preprocesamiento OpenCV]
        C[🔍 Inferencia con TFLite]
        D[🏷️ Clasificación con Modelo ]
        E[💾 Almacenamiento local]
        F[📡 Envío de datos ]

        subgraph Sistema Yocto
            Y1[meta-poky]
            Y2[meta-yocto-bsp]
            Y3[meta-raspberrypi]
            Y4[meta-openembedded]
            Y5[meta-mylayer]
        end
    end

    subgraph Servidor Central
        G[🖥️ Visualización resultados]
        H[🧩 Interfaz de control]
        I[🔁 Control de ciclo remoto]
    end

    subgraph Operador
        O[👤 Interacción y monitoreo]
    end

    A --> B
    B --> C
    C --> D
    D --> E
    E --> F
    F --> G
    G --> H
    H --> I
    I --> B
    O --> H
    P --> A

    %% Colores suaves y distintos para cada capa
    style Y1 fill:#dbeafe,stroke:#3b82f6,color:#1e3a8a
    style Y2 fill:#fef3c7,stroke:#f59e0b,color:#78350f
    style Y3 fill:#ede9fe,stroke:#8b5cf6,color:#4c1d95
    style Y4 fill:#dcfce7,stroke:#22c55e,color:#14532d
    style Y5 fill:#ffe4e6,stroke:#e11d48,color:#881337,font-weight:bold



```


## 🧩 Descripción del proceso de integración hardware/software
La solución implementada combina de forma coordinada componentes de hardware y software para lograr un sistema funcional de detección y visualización de emociones. A continuación se detalla cómo se integran y complementan estos componentes en cada etapa del proceso:

- 😃 Reacción del Espectador: Es la reacción o la expresión de la emoción por parte del espectador

- 🟦 Cámara USB (hardware): Es el punto de entrada del sistema. Captura imágenes en tiempo real del espectador o usuario cuya expresión emocional será analizada.

- 🟩 Raspberry Pi 5 (hardware + software): Actúa como nodo de procesamiento en el borde. Recibe la imagen desde la cámara y ejecuta varios procesos:

  - OpenCV (software): Realiza el preprocesamiento de la imagen (detección de rostro, recorte, escalado y normalización).

  - TensorFlow Lite (software): Ejecuta el modelo de aprendizaje automático entrenado para clasificar emociones en tiempo real.

  - Red de comunicación (hardware/software): Se utiliza WiFi o Ethernet para transferir los resultados inferidos (emociones y timestamps) al servidor central.

- 🟥 Servidor o computador Central (hardware + software): Recibe los datos procesados desde la Raspberry Pi y permite la interacción con el operador:

  - Interfaz Gráfica (software): Presenta visualmente las emociones detectadas y permite al operador ajustar parámetros del sistema (por ejemplo, encender/apagar el ciclo de inferencia o cambiar umbrales de confianza).

  - Control remoto del ciclo de procesamiento (software): El operador puede modificar el comportamiento del sistema en tiempo real, enviando instrucciones de vuelta a la Raspberry Pi.

Este diseño modular e integrado permite una interacción fluida entre hardware y software: la Raspberry Pi se encarga de la inferencia local, optimizando la latencia y reduciendo la carga sobre la red, mientras que el servidor central actúa como centro de control y visualización, facilitando ajustes remotos y monitoreo continuo.
