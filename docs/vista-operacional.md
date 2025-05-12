# Vista Operacional

```mermaid
flowchart TD
    subgraph Sala de Cine
        U1[🎟️ Espectadores entran al cine]
        U2[🎥 Inicia la película]
    end

    subgraph Operador
        O1[🧑‍💻 Inicia el sistema]
        O2[📤 Envía comando SSH]
    end

    subgraph Cámara
        CAM1[📷 Captura emociones]
    end

    subgraph Raspberry Pi
        R1[📷 Procesa la imagen]
        R2[🧠 Clasificación con modelo TFLite]
        R4[💾 Guarda emociones + timestamp]
        R5[📤 Envía reporte por SSH]
    end

    subgraph Computador del Usuario
        C1[📥 Recepción del reporte]
        C2[📊 Visualización/Análisis de emociones]
    end

    U1 --> U2
    U2 --> O1
    O1 --> O2
    O2 --> R1
    R1 --> R2
    R2 --> CAM1
    CAM1 --> R3
    R3 --> R4
    R4 --> R5
    R5 --> C1
    C1 --> C2

```
