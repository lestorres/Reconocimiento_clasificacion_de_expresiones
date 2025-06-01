# Auditor

### Sesión 1: Fecha - 01 de Mayo de 2025
    
#### Actividad 1:
        - Asignación del rol a auditor
        - Encargado del repositorio git
        - Revisión de entrega documentos, redacción y ortografía
        

#### Actividad 2:
        - Creación del repositorio git
        - Desarrollo de plantillas readme para las secciones de la propuesta
         

### Sesión 2: Fecha - 03 de Mayo de 2025

#### Actividad 1:
        - Revisión del diagrama de Gantt de la propuesta


 
### Sesión 3: Fecha - 05 de Mayo de 2025

#### Actividad 1:
        - Consultas en clase al profesor sobre Vista Funcional, Integración y bitácoras 



### Sesión 4: Fecha - 09 de Mayo de 2025

#### Actividad 1:
        - Elaboración de dependencias, vista funcional e integración
        - Coordinación de la branches del repositorio con la directora
        - Revisión de artículos para la justificación y propuesta 

### Sesión 5: Fecha - 11 de Mayo de 2025
    
#### Actividad 1:
        - Revisión del planteamiento del problema, y la inserción de imagenes
    
#### Actividad 2:

        - Realización de la justificación y referencias
    
#### Actividad 3:
        - Uso de herramienta de mermaid para diagramas de flujo


### Sesión 6: Fecha - 12 de Mayo de 2025
    
#### Actividad 1:
        - Desplazamiento de entrega de la propuesta a Jueves 14
    
#### Actividad 2:

        - Revisión de final de la justificación y calidad de graficas en mermaid

        
        

### Sesión 7: Fecha - 13 de Mayo de 2025
#### Actividad 1:
        - Error de interpretación de la entrega de la propuesta
#### Actividad 2:
        - Consulta de profesor sobre formato de entrega
        - Confirmación  de entrega en -pdf, 
        - Coordinación con directora para cambio de formato para .md a .pdf

#### Actividad 3:

        - Ajuste de formato de .md a .pdf satisfactorio

  

### Sesión 8: Fecha - 14 de Mayo de 2025
#### Actividad 1:
        - Revisión Final del propuesta

#### Actividad 2:
       - Entrega de la propuesta vía correo electronico



### Sesión 9: Fecha - 16 de Mayo de 2025

#### Actividad 1:
        - Dependencias para image core-image-minimal para raspberry

        - Aparece un error en la primera corrida del bitbake
            

```plaintext
Error de conflicto de paquetes (SOLUCIONADO)

Durante la construcción de core-image-minimal, ocurrió un conflicto entre dos paquetes:

packagegroup-core-ssh-dropbear requiere dropbear.

Pero dropbear conflicta con openssh que también se está tratando de instalar.

El sistema no puede instalar ambos (dropbear y openssh) al mismo tiempo debido a este conflicto.


Solución, usar el paquete SSH para protocolo de comunicación
```
 
### Sesión 10: Fecha - 17-18 de Mayo de 2025
#### Actividad 1:

        - Error de image-core-minimal (SOLUCIONADO)
```plaintext
Se presenta un error en donde al usar el Raspberry imager, se flasheaba la SD pero al conectarlo con las raspberry en físico, esta imagen no contaba con el bootloader bien instalado.
```
    **Solución** :  Cocinar image-core-base con las mismas capas de la minimal, se aprendió a cambiar la extensión .wic a -img para que el imager detectara la imagen y flasear correctamente a la raspberry pi. Se usaron las referencias [1] y [2]  como guía.


### Sesión 11: Fecha - 19 de Mayo de 2025
#### Actividad 1:
       
        -  Solicitud con la directora de la cámara tipo USB para el proyecto.
       

#### Actividad 2:

        - Primer Flasheo de la imagen exitoso, logró cargar correctamente el bootloader.
    
#### Actividad 3:
        - Registrar avance en un tutorial para facilidad de aprendizaje.
    
#### Actividad 4:
        
        - Revisar dependencia de las capas de tensorflow y añadir open Multimedia a la imgagen

### Sesión 12: Fecha - 20 de Mayo de 2025
    
#### Actividad 1:
        - Integración de Meta-multimedia y Meta-tensorflow a la imagen exitoso.
#### Actividad 2:
        - Actualización de bitácora de auditor.

### Sesión 14: Fecha - 22 de Mayo de 2025
#### Actividad 1:
        - Revisión de documentanción de modelos de edge IA suministrados por parte de la investigadora.
        - En este punto el tema esta en la precisión del modelo, todos lo modelos recortados daban precisiones entre el 60% al 87%, la mejor precisión lo daba [1], quien ya contaba con un modelo lite de tensorflow para arm.

    Referencias
        [1] vicksam, “fer-model: Detecting emotions in face images,” GitHub, 2025. [Online]. Available: https://github.com/vicksam/fer-modelGitHub
        

### Sesión 15: Fecha - 22-23 de Mayo de 2025
#### Actividad 1:
        - Revisión de informacion sumistrada de investigadora para envio por ssh.
        - Correción de código de envio de datos por ssh de la parte técnica.
        -En este punto, el problema era definir lo que interpretabamos como remoto, porque algo inalambrico es remoto, pero también puede ser remoto y con cable, que fue lo que se eligió a implementar.

### Sesión 16: Fecha - 24 de Mayo de 2025
#### Actividad 1:
        - Revisión de la integración entre software y hardware.
        - Correción de errores de errores de captura de video.
        - Acá se comenzó a configurar la mediante un video de prueba de captura de rostros de parte del modelo, se hizo compatible con video y con cámara.
### Sesión 17: Fecha - 25 de Mayo de 2025
    
#### Actividad 1:
        - Correción de errores de errores de captura de video, ya se hicieron pruebas con cámara y ya captura con video se recomienda hacer una calibración con el modelo, con una primera corrida y con la detección de felicidad antes de tener de obtener el set definitivo.
#### Actividad 2:
        - Hacer documentación y acomodar github.
        - Crear pdf's de bitacoras para la entrega.

### Sesión 18: Fecha - 26 de Mayo de 2025
#### Actividad 1 :
        - Reviciones finales.
        - Entrega de la demostración del proyecto.
##### NOTA :
         - Extensión de la entrega del proyecto.


### Sesión 19: Fecha - 26 de Mayo de 2025
#### Actividad 1 :
    - Planeamiento e integración de funciones adicionales de la interfaz de usuario.
    - Esquema de trabajo de funciones finales de la interfaz y la demostración.

### Sesión 20: Fecha - 31 de Mayo de 2025

#### Actividad 1 :
    - Revisión de las nuevas funciones de la interfaz de usuario.
    - Acomodo de repositorio git integrando características de la nueva interfaz de usuario.
    - Actualización de las bitácoras.


    
