#Tutorial yocto project para Raspberry pi 5

## Paso 1.  Crear directorio fuente

mkdir yocto-rpi5
cd yocto-rpi5

## Paso 2. Clonar poky

git clone https://github.com/yoctoproject/poky.git
cd poky

## Paso 3.  Pasarse al branch scarthgap

git branch -a
git checkout -t origin/scarthgap -b my-scarthgap

## Paso 4. Agregar  meta-layers

´´´plaintext

yocto-rpi5/
├── poky/                      ← poky ( branch scarthgap)
├── meta-raspberrypi/          ← capa para RPi
├── meta-openembedded/         ← capas openembedded
└── build-rpi5/                ← entorno de compilación
´´´



### Paso 4.1. Agregar meta-raspberrypi layer
git clone git://git.yoctoproject.org/meta-raspberrypi
cd meta-raspberrypi
git checkout scarthgap

### Paso 4.2. Agregar meta-openembedded layer
git clone https://github.com/openembedded/meta-openembedded.git
cd meta-openembedded
git checkout scarthgap

## Paso 5. añadir y mostrar layers

### Iniciar entorno de build
cd ~/yocto-rpi5/poky
source oe-init-build-env ../build-rpi5


bitbake-layers add-layer ../meta-raspberrypi
bitbake-layers add-layer ../meta-openembedded/meta-oe
bitbake-layers add-layer ../meta-openembedded/meta-python
bitbake-layers add-layer ../meta-openembedded/meta-networking

´´´plaintext
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
´´´


bitbake-layers show-layers




## Paso 6. Moficar local_conf dentro de 

nano conf/local.conf

### Paso 6.1. Añadir


´´´bash
#--------Limitar threads---------
BB_NUMBER_THREADS = "8"
PARALLEL_MAKE = "-j8"

#---------------------------------------
MACHINE = "raspberrypi5"
IMAGE_INSTALL:append = " openssh"
ENABLE_UART = "1"
´´´


# Paso 7. A cocinar

bitbake core-image-minimal



# TARGET





# REFERENCIAS

https://eclipse.dev/kanto/docs/how-to-guides/build-yocto-image-raspberry-pi/
