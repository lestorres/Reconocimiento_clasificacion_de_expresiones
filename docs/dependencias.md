# Dependencias
Dentro de las dependencias generales para la imagen del sistema operativo de Yocto.

## 🌲 Árbol de Dependencias de Capas Yocto (general)
```plaintext
meta (poky base)
│
├── meta-poky (distribución de referencia)
├── meta-yocto-bsp (BSPs de referencia)
├── meta-openembedded
│   ├── meta-oe (paquetes básicos y utilidades)
│   ├── meta-python (soporte para Python y paquetes relacionados)
│   ├── meta-multimedia (paquetes multimedia: codecs, players, etc.)
│   └── meta-networking (paquetes de red y protocolos)
│
├── meta-raspberrypi (BSP específico para RPi)
└── meta-mylayer (capa personalizada del usuario para la app DNN)

```

## 📋 Análisis general de las dependencias:
`meta y meta-poky`: proporcionan el núcleo del sistema de construcción (Poky) y la distribución base de referencia.

`meta-yocto-bsp`: incluye soporte para placas de hardware de referencia para la Raspberry Pi.

`meta-openembedded`: agrupación clave que extiende las capacidades de Poky.

`meta-oe`: utilidades básicas, bibliotecas comunes.

`meta-python`: dependencias de Python.

`meta-multimedia`: soporte para procesamiento de video/audio.

`meta-networking`: gestión de interfaces y protocolos de red.

`meta-raspberrypi`: contiene todo lo necesario para generar imágenes compatibles con Raspberry Pi.

`meta-mylayer`: es la capa personalizada que incluye recetas para la aplicación de inferencia, los scripts y las dependencias específicas.

