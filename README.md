# Contador De Puntos
### Requisitos:
- Cualquier Tipo de Camara USB o Camara Preinstalada en Laptop (Recommendacion: Camara con Calidad de 720p)
- Descargar el archivo "Ejemplo.py" que se encuentra en este repositorio
- Instalar Python version 3.10.6
### Pasos para Utilizar el Programa:
Descargar el archivo "Ejemplo.py" que se encuentra en la seccion de arriba de esta pagina.

Primero instalaremos la version apropiada de Python para ultizar el programa. Abajo le proporcionamos el link para realizar la descarga desde la pagina oficial de Python. (Descargue el archivo que coresponda con su sistema operativo Windows/MacOS)

https://www.python.org/downloads/release/python-3106/

Para confirmar que si se instalo correctamente puedes:
1. Oprimir en el teclado |Boton de Windows + R|
2. Escribir "cmd"
3. Oprimir "Enter"
4. En la ventana de CMD que se acaba de abrir ingresar el siguente commando y oprimir "Enter"
   
Aqui esta el commando:

    py -3.10 --version

6. Deberias de ver "Python 3.10.6" desplegado en la venta, como en la siguente imagen.
<img width="580" height="167" alt="{C9F7049A-1AF3-4453-9017-A616A7EBEACF}" src="https://github.com/user-attachments/assets/82c70b48-a5ec-487b-99ee-39d11d867c84" />

Al confirmar la instalacion de Python, siguente debemos crear un carpeta nueva para nuestro programa. La puede crear donde usted guste pero por simplicidad la puede crear un su escritorio. Al crear la carpeta, podemos dejar oprimido "Shift" y hacer click derecho en la carpeta y buscar por la opcion "Abrir con Powershell".

Dentro de la ventana de Powershell vamos a ingresar el siguente commando y oprimir "Enter": 

    python -m venv venv

El commando creo varias carpetas y ocupamos posicionarnos en la carpeta correcta que no permita activar nuestro programa.
Ingresaremos este commando:

    cd venv

Despues utilizaremos otro commando para entrar a otra carpeta:

    cd Scripts

Foto para verificar que estes en la carpeta correcta:

<img width="626" height="257" alt="{6BD48CE1-715F-4815-95AE-896EB8B60A16}" src="https://github.com/user-attachments/assets/e536cce8-c1de-4524-b853-6d4fe10244bc" />

Despues de confirmar que estas en la carpeta indicada usaremos otro commando para activar nuestro entorno virtual, donde nuestro programa realizara todas sus funciones:

    activate

Ya que ingreses el commando anterior estaremos dentro de un entorno virtual y ahora podemos iniciar la instalacion de otros programas para que nuestro programa tenga su funcionalidad completa. No te preocupes esto se instalara dentro del entorno virtual y no directamente en su dispositivo.

    python.exe -m pip install --upgrade pip
    python -m pip install --upgrade pip setuptools wheel 
    pip install mediapipe==0.10.9 
    pip install opencv-python

Ahora nos vamos a regresar a la carpeta principal que creamos. Para hacer eso simplemente ingrese este commando dos veces:

    cd ..

Al llegar a la carpeta inicial que creamos puede correr este commando para ejecutar el programa!

    python Ejemplo.py

Ya que inicie el programa puede levantar una mano para comprobar que funcione el programa!




