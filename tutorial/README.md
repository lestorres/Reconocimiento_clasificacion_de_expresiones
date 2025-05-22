#Tutorial yocto project para Raspberry pi 5

## Paso 1.  Crear directorio fuente
```bash
mkdir yocto-rpi5
cd yocto-rpi5
```

## Paso 2. Clonar poky y seleccionar scarthgap
```bash
git clone https://github.com/yoctoproject/poky.git
cd poky
git branch -a
git checkout -t origin/scarthgap -b my-scarthgap
```
## Paso 3. Agregar  meta-layers

#### Organizacon de los directorio
```plaintext
yocto-rpi5/
├── poky/                      ← poky ( branch scarthgap)
├── meta-raspberrypi/          ← capa para RPi
├── meta-openembedded/         ← capas openembedded
├── meta-tensorflow/           ← capa tensorflow
├── meta-mylayer   /           ← capa my-layer
└── build-rpi5/                ← entorno de compilación
```



### Paso 3.1. Agregar meta-raspberrypi layer en el directorio `~/yocto-rpi5`
```bash
git clone git://git.yoctoproject.org/meta-raspberrypi
cd meta-raspberrypi
git checkout scarthgap
```
### Paso 3.2. Agregar meta-openembedded layer
```bash
git clone https://github.com/openembedded/meta-openembedded.git
cd meta-openembedded
git checkout scarthgap
```

### Paso 3.3. Agregar meta-tensorflow
```bash
git clone https://git.yoctoproject.org/meta-tensorflow
cd meta-tensorflow
git checkout scarthgap
```

### Paso 3.4. Agregar meta-mylayer

```bash
cd ~/yocto-rpi5
bitbake-layers create-layer meta-mylayer
```

Quedará de esta forma, 

```bash
	
meta-mylayer/
├── conf/
│   └── layer.conf
└── README
```

Sobre el directorio meta-mylayer se debe copiar la capa "meta-mylayer" del repositorio de git. 


## Paso 4. Añadir y mostrar layers

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
bitbake-layers add-layer ../meta-openembedded/meta-multimedia
bitbake-layers add-layer ../meta-tensorflow
bitbake-layers add-layer ../meta-mylayer
```

- Al hacer `bitbake-layers show-layers` se debe desplegar algo como esto:

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
multimedia-layer      /home/lesme/yocto-rpi5/meta-openembedded/meta-multimedia                5
meta-tensorflow       /home/lesme/yocto-rpi5/meta-tensorflow                                  10
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

#-------------------------------0----------------------------------
MACHINE = "raspberrypi5"
INIT_MANAGER = "systemd"
LICENSE_FLAGS_ACCEPTED = "synaptics-killswitch"
IMAGE_INSTALL:append = " openssh"

```


# Paso 7. A cocinar
```bash
bitbake core-image-base
```

# Paso 8. Imagen 

Para descomprimir la imagen generada:
```bash
bzip2 -dc core-image-minimal-raspberrypi5.rootfs-20250519232619.wic.bz2 > ../core-image-minimal-raspberrypi5.rootfs-20250519232619.wic
```






# TARGET

### Camara Logitech Webcam C170 - Especificaciones Técnicas

| Característica             | Detalle                                                                |
|----------------------------|-------------------------------------------------------------------------|
| **Modelo**                 | Logitech C170                                                           |
| **Tipo de conexión**       | USB 2.0 (compatible con USB 3.0)                                        |
| **Compatibilidad UVC**     | Sí (funciona sin drivers en Linux/Raspberry Pi)                         |
| **Resolución de video**    | Hasta 640x480 píxeles (VGA) a 30 fps                                    |
| **Resolución de imagen**   | Hasta 5 megapíxeles (interpolados por software)                         |
| **Micrófono integrado**    | Sí, con reducción de ruido                                              |
| **Longitud del cable**     | Aproximadamente 1.5 metros                                              |
| **Montaje**                | Clip universal (para monitores y laptops)                               |
| **Sistemas compatibles**   | Windows, macOS, Linux (incluyendo Raspberry Pi OS)                      |
| **Estándar de video**      | UVC (USB Video Class)                                                   |
| **Requisitos de energía**  | Alimentación por USB (bajo consumo)                                     |
| **Uso típico**             | Videollamadas, vigilancia, visión por computadora, educación, proyectos |

# Raspberry Pi 5 – Especificaciones Técnicas

| Característica               | Detalle                                                                 |
|------------------------------|-------------------------------------------------------------------------|
| **Modelo**                   | Raspberry Pi 5                                                          |
| **Procesador (CPU)**         | Broadcom BCM2712, Quad-core ARM Cortex-A76 @ 2.4 GHz                    |
| **Arquitectura**             | ARMv8-A (64 bits)                                                       |
| **GPU**                      | VideoCore VII                                                           |
| **RAM**                      | 8 GB LPDDR4X-4267                                                       |
| **Almacenamiento**           | microSD + Soporte para almacenamiento externo vía USB 3.0               |
| **Puertos USB**              | 2 × USB 3.0, 2 × USB 2.0                                                |
| **Red Ethernet**             | Gigabit Ethernet (con Wake-on-LAN)                                      |
| **Wireless**                 | Wi-Fi 802.11ac (2.4 GHz y 5.0 GHz), Bluetooth 5.0                       |
| **Vídeo y Display**          | 2 × micro-HDMI (hasta 4Kp60)                                            |
| **Cámara y Display CSI/DSI** | 2 × MIPI (1 para cámara, 1 para display), cada uno de 4 líneas          |
| **GPIO**                     | 40 pines                                                                |
| **PCIe**                     | PCIe 2.0 x1 vía conector FFC                                            |
| **Alimentación**             | USB-C (5V, 5A)                                                          |
| **RTC**                      | Reloj de tiempo real con soporte de batería externa                     |
| **Temperatura de operación** | 0°C a 60°C                                                              |
| **Dimensiones**              | 85.6 mm × 56.5 mm × 18 mm                                               |




# Interacciones

- Ver dispositivos conectados
	> v4l2-ctl --list-devices


# REFERENCIAS

[1] https://eclipse.dev/kanto/docs/how-to-guides/build-yocto-image-raspberry-pi/
[2] https://anavi.org/article/298/
