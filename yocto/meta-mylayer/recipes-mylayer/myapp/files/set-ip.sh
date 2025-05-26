#!/bin/sh
ip addr add 192.168.100.2/24 dev eth0
ip link set eth0 up


USERNAME="cine"
PASSWORD="8719"

# Crear usuario con su directorio home
useradd -m -s /bin/bash "$USERNAME"

# Establecer contraseña
echo "$USERNAME:$PASSWORD" | chpasswd

# Agregar a grupos sudo y video
usermod -aG sudo "$USERNAME"
usermod -aG video "$USERNAME"

