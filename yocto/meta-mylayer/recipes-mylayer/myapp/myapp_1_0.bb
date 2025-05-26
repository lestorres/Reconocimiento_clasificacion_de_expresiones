SUMMARY = "Aplicación personalizada para RPi5"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://${COMMON_LICENSE_DIR}/MIT;md5=0835ade698e0bcf8506ecda2f7b4f302"

SRC_URI = " \
    file://cliente.py \
    file://captura.py \
    file://set-ip.sh \
    file://set-ssh.sh \
    file://myapp-init.service \
"

S = "${WORKDIR}"

do_install() {
    install -d ${D}${bindir}/myapp
    install -m 0755 ${WORKDIR}/cliente.py ${D}${bindir}/myapp/cliente.py
    install -m 0755 ${WORKDIR}/captura.py ${D}${bindir}/myapp/captura.py
    install -m 0755 ${WORKDIR}/set-ip.sh ${D}${bindir}/myapp/set-ip.sh
    install -m 0755 ${WORKDIR}/set-ssh.sh ${D}${bindir}/myapp/set-ssh.sh

    install -d ${D}${systemd_system_unitdir}
    install -m 0644 ${WORKDIR}/myapp-init.service ${D}${systemd_system_unitdir}/myapp-init.service
}

SYSTEMD_SERVICE:${PN} = "myapp-init.service"
inherit systemd
