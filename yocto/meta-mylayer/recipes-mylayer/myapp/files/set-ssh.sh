#!/bin/sh

USUARIO_PC="lesmes"
IP_PC="192.168.100.1"

# Generar clave si no existe
if [ ! -f ~/.ssh/id_rsa ]; then
  echo "Generando clave SSH..."
  ssh-keygen -t rsa -b 2048 -N "" -f ~/.ssh/id_rsa
fi

# Copiar clave pública al PC usando cat + ssh
echo "Copiando clave pública a ${USUARIO_PC}@${IP_PC}..."
PUBKEY=$(cat ~/.ssh/id_rsa.pub)

ssh ${USUARIO_PC}@${IP_PC} "mkdir -p ~/.ssh && echo '${PUBKEY}' >> ~/.ssh/authorized_keys && chmod 700 ~/.ssh && chmod 600 ~/.ssh/authorized_keys"
