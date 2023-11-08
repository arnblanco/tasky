# Utiliza una imagen base de Python 3.10
FROM python:3.10-alpine

# Establece un directorio de trabajo en el contenedor
RUN mkdir /app
WORKDIR /app

# Instala las dependencias de la aplicación
COPY /requirements.txt /app/
RUN pip install -r requirements.txt

#Copy Entry Point
COPY /docker/app/entrypoint.sh /app/
RUN chmod 755 entrypoint.sh

COPY . /app/

ENTRYPOINT ["sh", "entrypoint.sh"]