FROM python:3.10-alpine

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Establece un directorio de trabajo en el contenedor
RUN mkdir /app
WORKDIR /app

# Instala las dependencias de la aplicación
COPY /requirements.txt .
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install --no-cache-dir -r requirements.txt

COPY . .

#Copy Entry Point
COPY /docker/app/entrypoint.sh .
RUN chmod 755 ./entrypoint.sh

ENTRYPOINT ["sh", "/app/docker/app/entrypoint.sh"]