#!/bin/bash

function instalarRequisitos(){
    pip install -r ../requirements.txt
}

function entorno(){
    export FLASK_APP="programa:servidor_flask"
    export FLASK_ENV="development"
}

function inicializarBBDD(){
    entorno
    flask db init
}

function migrarBBDD(){
    entorno
    flask db migrate -m 'version1'
    flask db update
}

function run() {
    entorno
    flask run
}
