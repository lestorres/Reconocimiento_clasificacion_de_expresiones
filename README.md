# II Proyecto: EdgeAI - Sistema Embebido para el reconocimiento y clasificación de expresiones faciales


## 🎬 Tema del Proyecto: Sistema Embebido de Análisis de Emociones en Sala de Cine

## 👥 Integrantes
- **Carolina** – Investigadora, Directora de Proyecto
- **Lesmes** – Líder Técnico, Auditor

## 🧠 Descripción breve
Este proyecto propone un sistema embebido en red, instalado en una sala de cine, para detectar emociones en los espectadores mediante Edge AI y Raspberry Pi.

## 📄 Documentación 

### 📄 Propuesta de proyecto
- [Propuesta](docs/Informe_Final.md)

## Bitácoras de Roles
- [Directora](bitacoras/directora.md)
- [Investigadora](bitacoras/investigadora.md)
- [Auditor](bitacoras/auditor.md)
- [Líder Técnico](bitacoras/lider_tecnico.md)

## Demotración Final
- [Demostración de funcionalidad](docs/demostracion.md)

- [Detalles de Hardware](yocto/README.md)

- [Detalles de la Interfaz](interfaz/README.md)

## 🌱 Ramas de trabajo
- `main`
- `yocto`
- `bitacoras`

## Directorios del Repositorio
El Repotorio cuenta con los siguientes directorios>

```bash
Reconocimiento_clasificacion_de_expresiones/
├── bitacoras/		--> Bitácoras
├── docs/		--> Documentacion del proyecto
├── imag/		--> Imágenes utilizas
├── interfaz/		--> Detalles de la interfaz de Usuario  
│   ├── interfaz_completa.py
│   ├── ip-set.sh
│   ├── README.md
│   └── ventana_ui.py
├── yocto/		--> Detalles de Hardware e imagen de yocto
│   ├── conf/
│   ├── meta-mylayer/
│   │   └── recipes-mylayer/
│   │       └── myapp/
│   │           ├── captura.py
│   │           ├── cliente.py
│   │           ├── myapp_1_0.bb
│   │           ├── myapp-init.service
│   │           ├── set-ip.sh
│   │           └── set-ssh.sh
│   └── README.md
├── LICENSE
└── README.md

````

## 🚀 Clonar el repositorio

```bash
git clone https://github.com/lestorres/Reconocimiento_clasificacion_de_expresiones.git
```

