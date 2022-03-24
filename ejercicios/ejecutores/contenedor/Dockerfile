FROM python:3.10

ARG CARPETA=/app
ARG PROGRAMA=programa.py
ENV PROGRAMA="$PROGRAMA"

COPY ./*.py $CARPETA/

WORKDIR $CARPETA

ENTRYPOINT ["/bin/sh","-c","python3"]
CMD [ "$PROGRAMA "]

LABEL maintainter="Ivan Osuna <ivan.osuna.ayuste@gmail.com>"
