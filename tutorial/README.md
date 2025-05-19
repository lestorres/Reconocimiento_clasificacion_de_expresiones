#Tutorial yocto project para Raspberry pi 5

## Paso 1.  Crear directorio fuente
```bash
mkdir yocto-rpi5
cd yocto-rpi5
```

## Paso 2. Clonar poky
```bash
git clone https://github.com/yoctoproject/poky.git
cd poky
```

## Paso 3.  Pasarse al branch scarthgap
```bash
git branch -a
git checkout -t origin/scarthgap -b my-scarthgap
```
## Paso 4. Agregar  meta-layers

#### Organizacon de los directorio
```plaintext
yocto-rpi5/
├── poky/                      ← poky ( branch scarthgap)
├── meta-raspberrypi/          ← capa para RPi
├── meta-openembedded/         ← capas openembedded
└── build-rpi5/                ← entorno de compilación
```



### Paso 4.1. Agregar meta-raspberrypi layer
```bash
git clone git://git.yoctoproject.org/meta-raspberrypi
cd meta-raspberrypi
git checkout scarthgap
```
### Paso 4.2. Agregar meta-openembedded layer
```bash
git clone https://github.com/openembedded/meta-openembedded.git
cd meta-openembedded
git checkout scarthgap
```

## Paso 5. añadir y mostrar layers

### Iniciar entorno de build
```bash
cd ~/yocto-rpi5/poky
source oe-init-build-env ../build-rpi5
```

### Agregar los layers
```bash
bitbake-layers add-layer ../meta-raspberrypi
bitbake-layers add-layer ../meta-openembedded/meta-oe
bitbake-layers add-layer ../meta-openembedded/meta-python
bitbake-layers add-layer ../meta-openembedded/meta-networking
```

al hacer ´bitbake-layers show-layers´ se debe desplegar algo como esto:

```plaintext
NOTE: Starting bitbake server...
layer                 path                                                                    priority
========================================================================================================
core                  /home/lesme/yocto-rpi5/poky/meta                                        5
yocto                 /home/lesme/yocto-rpi5/poky/meta-poky                                   5
yoctobsp              /home/lesme/yocto-rpi5/poky/meta-yocto-bsp                              5
raspberrypi           /home/lesme/yocto-rpi5/meta-raspberrypi                                 9
openembedded-layer    /home/lesme/yocto-rpi5/meta-openembedded/meta-oe                        5
meta-python           /home/lesme/yocto-rpi5/meta-openembedded/meta-python                    5
networking-layer      /home/lesme/yocto-rpi5/meta-openembedded/meta-networking                5
```






## Paso 6. Moficar local_conf dentro de 
```bash
nano conf/local.conf
```

### Paso 6.1. Añadir


```bash
#--------Limitar threads---------
BB_NUMBER_THREADS = "8"
PARALLEL_MAKE = "-j8"

#---------------------------------------
MACHINE = "raspberrypi5"
IMAGE_INSTALL:append = " openssh"
ENABLE_UART = "1"
```


# Paso 7. A cocinar
```bash
bitbake core-image-minimal
```


# TARGET

### Camara Logitech Webcam C170 - Especificaciones Técnicas

| Característica              | Detalle                                                                 |
|----------------------------|-------------------------------------------------------------------------|
| **Modelo**                 | Logitech C170                                                           |
| **Tipo de conexión**       | USB 2.0 (compatible con USB 3.0)                                        |
| **Compatibilidad UVC**     | Sí (funciona sin drivers en Linux/Raspberry Pi)                         |
| **Resolución de video**    | Hasta 640x480 píxeles (VGA) a 30 fps                                    |
| **Resolución de imagen**   | Hasta 5 megapíxeles (interpolados por software)                         |
| **Micrófono integrado**    | Sí, con reducción de ruido                                              |
| **Longitud del cable**     | Aproximadamente 1.5 metros                                              |
| **Montaje**                | Clip universal (para monitores y laptops)                              |
| **Sistemas compatibles**   | Windows, macOS, Linux (incluyendo Raspberry Pi OS)                      |
| **Estándar de video**      | UVC (USB Video Class)                                                   |
| **Requisitos de energía**  | Alimentación por USB (bajo consumo)                                     |
| **Uso típico**             | Videollamadas, vigilancia, visión por computadora, educación, proyectos |





# REFERENCIAS

https://eclipse.dev/kanto/docs/how-to-guides/build-yocto-image-raspberry-pi/
