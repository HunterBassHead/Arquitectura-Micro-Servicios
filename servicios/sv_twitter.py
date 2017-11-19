# -*- coding: utf-8 -*-
#!/usr/bin/env python
#----------------------------------------------------------------------------------------------------------------
# Archivo: sv_tweets.py
# Tarea: 2 Arquitecturas Micro Servicios.
# Autor(es): Edgar Pereida, Luis olivas, Alan, Miguel ibarra, Jesus Montalvo
# Version: 1.0 noviembre 2017
# Descripción:
#
#   Este archivo crea un servico para obtener y almacenar los cometarios de https://twitter.com/
#   
#   
#
#                                        sv_tweets.py
#           +-----------------------+-------------------------+----------------------------+
#           |  Nombre del elemento  |     Responsabilidad     |      Propiedades           |
#           +-----------------------+-------------------------+----------------------------+
#           |                       |  - Obtner y guardar     | - Utiliza el API de        |
#           |    obtener y guarda   | comentarios de twitter  |   Twitter                  | 
#           |    comentarios        |       en una bd         | - Obtine y guarda en una db|
#           |     en Twitter        |                         |   los tweets y comentarios |
#           |                       |                         |   mas recientes de la serie|
#           |                       |                         |   o pelicula en cuestión.  |
#           |                       |                         |                            |
#           +-----------------------+-------------------------+----------------------------+
#
#   Ejemplo de gurdar : Abrir navegador e ingresar a http://localhost:8085/api/v1/tweets/set?t=matrix movie
#
import os
import sys
from flask import Flask, abort, render_template, request
import urllib, json
import settings_tweets
import conexion
import tweepy
import json
from tweepy import OAuthHandler



app = Flask (__name__)

@app.route("/api/v1/tweets/set", methods=['GET'])
def set_information():
        #autentifica el sistema en twitter
        auth = OAuthHandler(settings_tweets.CONSUMER_KEY,settings_tweets.CONSUMER_SECRET)
        auth.set_access_token(settings_tweets.ACCESS_TOKEN,settings_tweets.ACCESS_TOKEN_SECRET)
        api = tweepy.API(auth)
        #obtener variable del url
        title = request.args.get("t")
        api = tweepy.API(auth)
        #Numero de tweets que se van a obtener
        max_tweets=200
        query=title
        response = []
        #Borrar lo que se encunetre en la base de datos
        conexion.dropDB()
        #verificar que no este vacio la entrada del navegador
        if title is not None:
            #obtener los tweets
            searched_tweets = [status._json for status in tweepy.Cursor(api.search,  q=query).items(max_tweets)]
            #recorrer los tweets
            for tweet in searched_tweets:
                #filtar los tweets en ingles 
                if tweet['lang'].rstrip('\n') == "en":
                    #uso de la api json SentimentAnalysis
                    url_sentiment= urllib.urlopen("http://localhost:8086/api/v1/SentimentAnalysis?t=" + decode(tweet['text']).replace("\\n",""))
                    json_sentiment = url_sentiment.read()
                    #guardar los tweets y el analisis de sentimientos en la base de datos
                    conexion.insertDB(tweet['text'],json_sentiment)
            return ('', 204)       
        else:
            abort(400)


def decode(path):
    """
    Convierte una cadena de texto al juego de caracteres utf-8 eliminando los caracteres que no estén permitidos en utf-8
    @type: str, unicode, list de str o unicode
    @param path: puede ser una ruta o un list() con varias rutas
    @rtype: str
    @return: ruta codificado en UTF-8
    """
    if type(path) == list:
        for x in range(len(path)):
            if not type(path[x]) == unicode:
                path[x] = path[x].decode("utf-8", "ignore")
            path[x] = path[x].encode("utf-8", "ignore")
    else:
        if not type(path) == unicode:
            path = path.decode("utf-8", "ignore")
        path = path.encode("utf-8", "ignore")
    return path


if __name__ == '__main__':
    # Se define el puerto del sistema operativo que utilizará el servicio
    port = int(os.environ.get('PORT', 8085))
    # Se habilita la opción de 'debug' para visualizar los errores
    app.debug = True
    # Se ejecuta el servicio definiendo el host '0.0.0.0' para que se pueda acceder desde cualquier IP
app.run(host='0.0.0.0', port=port)