# TARGET del proyecto

## Camara Logitech Webcam C170 - Especificaciones Técnicas

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

## Raspberry Pi 5 – Especificaciones Técnicas

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



# Flujo de trabajo de yocto project para la aplicación en la Raspberry Pi 5

## Paso 1.  Crear directorio fuente
```bash
mkdir yocto-rpi5
cd yocto-rpi5
```

## Paso 2. Clonar poky y seleccionar kirkstone
```bash
git clone https://github.com/yoctoproject/poky.git
cd poky
git checkout -b kirkstone origin/kirkstone
```
## Paso 3. Agregar  meta-layers

#### Organizacon de los directorio
```plaintext
yocto-rpi5/
├── poky/                      ← poky (branch kirkstone)
├── meta-raspberrypi/          ← capa para RPi
├── meta-openembedded/         ← capas openembedded
├── meta-tensorflow/           ← capa tensorflow
├── meta-mylayer/              ← capa personalizada
└── build-rpi5/                ← entorno de compilación
```


### Paso 3.1. Agregar meta-raspberrypi layer en el directorio `~/yocto-rpi5`
```bash
git clone git://git.yoctoproject.org/meta-raspberrypi
cd meta-raspberrypi
git checkout kirkstone
```
### Paso 3.2. Agregar meta-openembedded layer
```bash
git clone https://github.com/openembedded/meta-openembedded.git
cd meta-openembedded
git checkout kirkstone
```

### Paso 3.3. Agregar meta-tensorflow
```bash
git clone https://git.yoctoproject.org/meta-tensorflow
cd meta-tensorflow
git checkout kirkstone
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

Sobre el directorio meta-mylayer se debe copiar la capa "meta-mylayer" del repositorio de git.  Al final las rutas deben tener los siguientes directorios:

```bash
yocto-rpi5/
├── build-rpi5/
│   ├── bazel/
│   ├── bitbake-cookerdaemon.log
│   ├── cache/
│   ├── conf/
│   ├── downloads/
│   ├── sstate-cache/
│   └── tmp/
├── meta-mylayer/
│   ├── conf/
│   │   └── layer.conf
│   ├── COPYING.MIT
│   ├── README
│   └── recipes-mylayer/
├── meta-openembedded/
├── meta-raspberrypi/
├── meta-tensorflow/
├── models/
└── poky/
```
El modelo tflite utilizado se encuentra en [3]. 


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

- Al hacer `bitbake-layers show-layers` se debe desplegar algo como esto, estas son las dependencias necesarias para la imagen de yocto de la aplicación:

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



### Paso 6. Añadir paquetes necesarios en el local.conf

## Paso 6.1. Moficar local.conf 

Con el el archivo dentro del repositorio  `Reconocimiento_clasificacion_de_expresiones/yocto/conf`, se debe añadir al local_conf del proyecto lo siguiente, se puede reemplazar el archivo o copiar el siguiente contenido.

```bash
nano conf/local.conf
```

```bash
#--------Limitar threads---------
BB_NUMBER_THREADS = "8"
PARALLEL_MAKE = "-j8"

#--------------------------------0----------------------------------

MACHINE = "raspberrypi5"
INIT_MANAGER = "systemd"
LICENSE_FLAGS_ACCEPTED = "synaptics-killswitch commercial"

DISTRO_FEATURES += "ssh"

SYSTEMD_AUTO_ENABLE = "1"

#Paquetes
IMAGE_INSTALL:append = " \
  openssh \
  v4l-utils \
  opencv \
  python3 \
  python3-numpy \
  python3-requests \
  python3-opencv \
  tensorflow-lite \
  vim \
  myapp \
"
```

# Paso 7. A cocinar!

En este punto se cuenta con todo lo necesario y se puede cocinar.

```bash
bitbake core-image-base
```

# Paso 8. Imagen 
Una vez cocinada la imagen se debe descomprimir
Para descomprimir la imagen generada:
```bash
bzip2 -dc core-image-minimal-raspberrypi5.rootfs-20250519232619.wic.bz2 > ../core-image-minimal-raspberrypi5.rootfs-20250519232619.wic
```
Mediante la aplicación de Raspberry Pi Imager, se seleciona el modelo y la imagen descomprimida para flashear la tarjeta SD.

# Paso 9. Configuración Inicial (Primer Arranque)

Desde la PC Linux se debe ejecutar como administrados el ejecutable:


```bash
sudo ./ip-set.sh
```
Que contiene la configuración necesaria para el arranque: 
```bash
sudo ip addr add 192.168.100.1/24 dev eth0
sudo ip link set eth0 up
```
Luego mediante ping se puede determinar la conexión con la raspberry Pi

```bash
sudo ping 192.168.100.2
```
 Una vez configurada la conexión, se debe encender la Raspberry PI y conectarse mediante ssh de la siguiente manera:
 
```bash
ssh root@192.168.100.2
```

Una vez dentro de la Raspberry PI, se debe ejecutar lo siguiente dentro de `/usr/bin/myapp`

```bash
./set-ssh.sh
```
Que contiene las llaves necesarias para la transferencia de archivos.


Desde Raspberry Pi 5

```bash

sudo ip addr add 192.168.100.2/24 dev eth0
sudo ip link set eth0 up

```
También se pueden hacer las interacciones de:

- Ver dispositivos conectados (cámara Usb)
	> v4l2-ctl --list-devices
 

Al final se busca obtener una arquitectura como esta:

<img src="../imag/arquitectura2.png?raw=true" alt="arqui" width="500"/>

# Paso 10. Interfaz

Desde la PC Linux:

Abrir el archivo interfaz_completa.py e interactuar con el modelo.

```bash
python3 interfaz_completa.py
```


# REFERENCIAS

[1] Eclipse Foundation, "How to Build a Yocto Image for Raspberry Pi," Eclipse Kanto Documentation. [Online]. Available: https://eclipse.dev/kanto/docs/how-to-guides/build-yocto-image-raspberry-pi/.

[2] T. Stoev, "Running TensorFlow Lite image classification on Raspberry Pi with ANAVI Infrared pHAT," ANAVI Technology Blog, Aug. 2021. [Online]. Available: https://anavi.org/article/298/. 

[3] vicksam, fer-model: Facial expression recognition using Keras and OpenCV, GitHub repository. [Online]. Available: https://github.com/vicksam/fer-model. 
