#FROM IMAGEN-BASE
FROM python:3.10

# ARG CARPETA=/app
# Esto es un argumento que se puede suministrar al creador de la imagen
ARG CARPETA=/app
ENV CARPETA=$CARPETA

#USER root

# ADD es igual al copy... como pille un fichero zip, lo descomrime
#ADD ./src /app
#COPY source(relativo al host) target(relativa al contenedor)
COPY ./src /$CARPETA

#RUN COMANDOS QUE SE EJECUTAN AL CREAR LA IMAGEN DEL CONTENEDOR
RUN pip3 install PAQUETE/S

WORKDIR /$CARPETA

# CMD COMANDO QUE SE EJECUTARA AL CREAR UN CONTENEDOR DESDE ESTA IMAGEN
# WORKDIR
# ENTRYPOINT comando a ejecutar por defecto
# CMD parametros de ese comando. A falta de entry point, el CMD se interpreta como : COMANDOS + PARAMETROS

#ENTRYPOINT python3
#CMD app/programa.py

CMD ["python3", "app/programa.py"]


# Datos informativos
VOLUME "/log"
VOLUME ["log",$CARPETA]
VOLUME ["/data"]
EXPOSE 8080

LABEL maintainter="Ivan Osuna"
