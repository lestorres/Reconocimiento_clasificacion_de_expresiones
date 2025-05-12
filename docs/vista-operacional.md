# Vista Operacional
A continuación, se muestra un diagrama de la vista operacional del sistema:

```mermaid
flowchart TD
    subgraph Sala de Cine
        A[🎟️ Espectadores entran al cine]
        B[🎥 Inicia la película]
    end

    subgraph Operador
        C[🧑‍💻 Inicia el sistema]
    end

    subgraph Cámara
        CAM1[📷 Captura emociones]
    end

    subgraph Raspberry Pi
        R1[📥 Solicita imagen a cámara]
        R2[🧠 Clasificación de emociones]
        R3[💾 Guarda emociones + timestamp]
        R4[📤 Envía reporte]
    end

    subgraph Computador del Operador
        D[📥 Recepción del reporte]
        E[📊 Visualización/Análisis de emociones]
    end

    A --> B
    B --> C
    C --> R1
    R1 --> CAM1
    CAM1 --> R2
    R2 --> R3
    R3 --> R4
    R4 --> D
    D --> E

```

## 🧩 Descripción de la vista operacional
En este punto se presenta una descripción del comportamiento del sistema con el fin de que cualquier persona pueda entender su funcionamiento. Es importante que el modelo defina una perspectiva completamente operacional, sencilla y comprensible para el usuario. Por esta razón, se realiza una representación de alto nivel, en la cual se destacan los componentes principales del sistema y la manera en que se utilizan de forma secuencial para lograr la detección y registro de emociones. Esta representación permite visualizar el flujo de operación desde la llegada del espectador hasta la recopilación final de datos por parte del operador.

- 🎟️ Llegada del público: Los espectadores ingresan a la sala de cine y se acomodan en sus respectivas butacas para disfrutar de la película.

- 🧑‍💻 Operador: Cuando inicia la película, el operador activa el sistema de detección de emociones. Para ello, envía un comando a la Raspberry Pi a través de la red WiFi, ordenándole que encienda la cámara y comience el procesamiento.

- 🟦 Cámara USB: La camára se conecta a la Raspberry Pi, esta comienza a capturar imágenes de los rostros del público a razón de 1 fotograma por segundo (1 fps), y envía las capturas en tiempo real a la Pi.

- 🟩 Raspberry Pi 5: La raspberry recibe las imágenes capturadas por la cámara y la clasifica para determinar el estado emocional de la persona, por ultimo guarda la imagen mediante un archivo que contiene la emoción y el tiempo en que el rostro fue capturado.

- 🟥 Computador del Operador: Cuando termina la función o el operador decide finalizar el monitoreo, este envía otro comando a la Raspberry Pi para detener el sistema. Los archivos generados (emociones + timestamps) se transfieren automáticamente al computador del operador mediante protocolo SSH, aprovechando que ambos dispositivos están conectados a la misma red WiFi.

## 🎯 Diagrama de casos de uso
A partir de las funciones que desempeñan el espectador y el operador, es posible construir el diagrama de casos de uso. El espectador simplemente se sienta y disfruta de la función de cine, mientras que el operador se encarga de varias funciones importantes como iniciar y finalizar la ejecución de la aplicación, además de analizar los datos obtenidos y generar reportes.

Cabe destacar que la elección de capturar las imágenes a una tasa de 1 cuadro por segundo (1 fps) se debe a que las emociones de corta duración —que suelen ser las expresiones más comunes al visualizar una película— tienden a mantenerse durante varios segundos. Por ello, este intervalo de captura resulta suficiente para registrar dichas emociones de manera efectiva [Kadakia et al., 2022].

```mermaid
flowchart TD

    subgraph Eventos
        A[Se sienta en la sala de cine y visualiza la película]
        B[Inicia la ejecución del sistema]
        C[Finaliza la ejecución del sistema]
        D[Analiza los datos del sistema]
        E[Genera un reporte con datos obtenidos]
    end

    subgraph Espectador
        S[Espectador]
    end

    subgraph Operador
        O[Operador]
    end


    S --> A
    O --> B
    O --> C
    O --> D
    O --> E



```

## 🕒 Diagrama de secuencia
Seguidamente se presenta el diagrama de secuencia del sistema, en el que se consideran cinco elementos principales: el espectador, la cámara, la Raspberry Pi, el operador y el computador del operador. En esta secuencia, el espectador se limita a disfrutar de la película sin intervenir en el proceso. El operador se encarga de inicializar el sistema, lo que activa la interfaz e inicia el programa de detección de emociones. A partir de este punto, la cámara captura imágenes que son procesadas por la Raspberry Pi, donde también se almacenan los archivos generados. Este ciclo se repite de forma continua hasta que el operador decide finalizar la ejecución. Finalmente, los datos son transferidos al computador, donde la interfaz permite visualizar los resultados en formato de texto o gráficos.

<p align="center">
  <img src="../imag/secuencia.jfif"  width="800"/>
</p>

### Referencias
- R. Kadakia, P. Kalkotwar, P. Jhaveri, R. Patanwadia and K. Srivastava, "Analysis of Micro Expressions using XAI," 2022 3rd International Conference on Computing, Analytics and Networks (ICAN), Rajpura, Punjab, India, 2022, pp. 1-7, doi: 10.1109/ICAN56228.2022.10007340.
