# BOT de Discord

El bot está desarrollado como una herramienta multfuncional para brindar una experencia mejorada a los usuarios dentro de la plataforma Discord. Este bot permite interacuar con la API de Hive y los endpoints, con la finalidad de extraer y enviar datos. 

## Pasos de preparación del proyecto

Sigue estos pasos para preparar y ejecutar el proyecto:

1. Clona el repositorio en tu máquina local:

### Clonar con SSH:

```
git clone git@github.com:alberto0607/bot-discord-hp.git
```

### Clonar con HTTPS:

```
git clone https://github.com/alberto0607/bot-discord-hp.git
```
2. Entra a la carpeta del proyecto:

```
cd bot-discord-hp
```

3. Crea un entorno virtual para el proyecto:

```
python -m venv env

ó

python3 -m venv env
```

4. Activa el entorno virtual:

- En Windows:

```
venv\Scripts\activate
```

- En Linux o macOS:

```
source env/bin/activate
```

5. Instala las dependencias del proyecto desde el archivo `requirements.txt`:

```
pip install -r requirements.txt
```

6. Renombra el archivo `.env-example` a `.env` y configura las variables de entorno según tus necesidades. Asegúrate de proporcionar los valores correctos para las variables.


## Uso del proyecto

Una vez que hayas configurado el entorno y las variables de entorno, puedes ejecutar el proyecto a partir del archivo `main.py`.

Puedes ejecutar el proyecto de la siguiente manera:

```
python main.py
```

Antes, recuerda crear la instancia del bot en https://discord.com/developers/applications, hacer todas las configuraciones necesarias e initarlo a tu servidor de Discord.

## Contribuciones

Las contribuciones son bienvenidas. Si encuentras errores, mejoras o nuevas características que se puedan agregar al proyecto, no dudes en enviar una solicitud de extracción.
También puedes dejar un comentario en mi blog, [visitar aquí.]()

## Licencia

Este proyecto se ofrece bajo los principios del software libre y el código abierto, lo que significa que puedes utilizarlo, modificarlo y distribuirlo de acuerdo con las libertades que ofrece este tipo de licencias. Se proporciona sin garantía alguna, y la responsabilidad recae en el usuario que lo utilice. Te invitamos a aprovechar al máximo las ventajas del software libre y a contribuir a su comunidad.
