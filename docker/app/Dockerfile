# Utiliza una imagen base de Python 3.10
FROM python:3.10

# Establece un directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos de tu aplicación al contenedor
COPY . /app

# Instala las dependencias de la aplicación
RUN pip install -r requirements.txt

# Ejecuta migraciones de Django
#CMD ["python", "manage.py", "migrate"]