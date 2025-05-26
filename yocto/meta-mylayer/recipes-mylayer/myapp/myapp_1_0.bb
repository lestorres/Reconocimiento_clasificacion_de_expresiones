SUMMARY = "Aplicación personalizada para RPi5"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://${COMMON_LICENSE_DIR}/MIT;md5=0835ade698e0bcf8506ecda2f7b4f302"

SRC_URI = " \
    file://calibracion_server.py \
    file://cliente.py \
    file://captura.py \
    file://prueba_foto.py \
    file://prueba_video.py \
    file://my_video.mp4 \
    file://test_image.png \
    file://set-ip.sh \
    file://set-ssh.sh \
    file://myapp-init.service \
    file://model/ferplus_model_pd_best.tflite \
    file://proyecto2/facedetection.py \
    file://proyecto2/model.tflite \
    file://proyecto2/cascade_frontalface_default.xml \
"

S = "${WORKDIR}"

do_install() {
    install -d ${D}${bindir}/myapp

    # Archivos principales
    install -m 0755 ${WORKDIR}/calibracion_server.py ${D}${bindir}/myapp/
    install -m 0755 ${WORKDIR}/cliente.py ${D}${bindir}/myapp/
    install -m 0755 ${WORKDIR}/captura.py ${D}${bindir}/myapp/
    install -m 0755 ${WORKDIR}/prueba_foto.py ${D}${bindir}/myapp/
    install -m 0755 ${WORKDIR}/prueba_video.py ${D}${bindir}/myapp/
    install -m 0755 ${WORKDIR}/set-ip.sh ${D}${bindir}/myapp/
    install -m 0755 ${WORKDIR}/set-ssh.sh ${D}${bindir}/myapp/
    install -m 0644 ${WORKDIR}/test_image.png ${D}${bindir}/myapp/
    install -m 0644 ${WORKDIR}/my_video.mp4 ${D}${bindir}/myapp/

    # Carpeta model/
    install -d ${D}${bindir}/myapp/model
    install -m 0644 ${WORKDIR}/model/ferplus_model_pd_best.tflite ${D}${bindir}/myapp/model/

    # Carpeta proyecto2/
    install -d ${D}${bindir}/myapp/proyecto2
    install -m 0644 ${WORKDIR}/proyecto2/facedetection.py ${D}${bindir}/myapp/proyecto2/
    install -m 0644 ${WORKDIR}/proyecto2/model.tflite ${D}${bindir}/myapp/proyecto2/
    install -m 0644 ${WORKDIR}/proyecto2/cascade_frontalface_default.xml ${D}${bindir}/myapp/proyecto2/

    # Servicio systemd
    install -d ${D}${systemd_system_unitdir}
    install -m 0644 ${WORKDIR}/myapp-init.service ${D}${systemd_system_unitdir}/
}

SYSTEMD_SERVICE:${PN} = "myapp-init.service"
inherit systemd
