# -*- coding: utf-8 -*-
#!/usr/bin/env python
#----------------------------------------------------------------------------------------------------------------
# Archivo: sv_SentimentAnalysis.py
# Tarea: 2 Arquitecturas Micro Servicios.
# Autor(es): Edgar Pereida, Luis olivas, Alan, Miguel ibarra, Jesus Montalvo
# Modificada por: 
# Version: 1.0 noviembre 2017
# Descripción:
#
#   Este archivo analiza los comentarios y regresa la polaridad
#   
#   
#
#                                        sv_tweets.py
#           +-----------------------+-------------------------+----------------------------+
#           |  Nombre del elemento  |     Responsabilidad     |      Propiedades           |
#           +-----------------------+-------------------------+----------------------------+
#           |                       |  -analiza y regresa los | - Analiza los comentarios  |
#           |    Procesador de      |    comentarios          |    con textblob            | 
#           |    comentarios        |                         | - regrea los porsentajes   |
#           |     en con una        |                         |   de cada polaridad        |
#           |    api(textblob)      |                         |                            |
#           |                       |                         |                            |
#           |                       |                         |                            |
#           +-----------------------+-------------------------+----------------------------+
#
#   Ejemplo de uso: Abrir navegador e ingresar a http://localhost:8086/api/v1/SentimentAnalysis?t=i love you
#   Ejemplo de uso : Abrir navegador e ingresar a http://localhost:8085/api/v1/SentimentAnalysis/get movie
#
import os
import sys
from flask import Flask, abort, render_template, request
import urllib, json
import conexion
from textblob import TextBlob

app = Flask (__name__)


@app.route("/api/v1/SentimentAnalysis", methods=['GET'])
def analysis():
	text = request.args.get("t")
	print text
	analysis = TextBlob(text)
	    # set sentiment
	if analysis.sentiment.polarity > 0:
		return 'positive'
	elif analysis.sentiment.polarity == 0:
		return 'neutral'
	else:
		return 'negative'


@app.route("/api/v1/SentimentAnalysis/get")
def get_information():

    positive=0;
    neutral=0;
    negative=0;
    #obtener y recorrer los el analisis de sentimientos para contarlos 
    for r in conexion.selectDB():
        if r == "neutral":
            neutral+=1

        if r == "positive":
            positive+=1

        if r == "negative":
            negative+=1
    #sacar el porsentaje para mostarlo 
    suma=positive+neutral+negative
    positive=float("{0:.2f}".format((float(positive)/float(suma))*100))
    neutral=float("{0:.2f}".format((float(neutral)/float(suma))*100))
    negative=float("{0:.2f}".format((float(negative)/float(suma))*100))
    my_json_string = json.dumps({"positive":str(positive)+"%","neutral":str(neutral)+"%","negative":str(negative)+"%"})
    omdb = json.loads(my_json_string)
    return json.dumps(omdb)

if __name__ == '__main__':
    # Se define el puerto del sistema operativo que utilizará el servicio
    port = int(os.environ.get('PORT', 8086))
    # Se habilita la opción de 'debug' para visualizar los errores
    app.debug = True
    # Se ejecuta el servicio definiendo el host '0.0.0.0' para que se pueda acceder desde cualquier IP
app.run(host='0.0.0.0', port=port)