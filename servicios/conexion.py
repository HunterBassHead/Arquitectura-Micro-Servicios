#!/usr/bin/python
# -*- coding: utf-8 -*-

import pymysql


def insertDB(tweet,Sentiment):
    # Crea Conexion a la base de datos MySql.
    db = MySQLdb.connect("localhost","tweets","tweets","tweets" )
    cursor = db.cursor()
    sql = "insert into tweets (tweets,Sentiment) values ('%s','%s')" %(tweet,Sentiment)
    try:
        #La sentecia se ejecuta
        cursor.execute(sql)
        #commit que hace los cambios en la base de datos.
        db.commit()
    except:
        #regresa la base de datos como estaba.
        db.rollback()
    #La conexion se cierra  
    db.close()


def dropDB():
    # Crea Conexion a la base de datos MySql.
    db = MySQLdb.connect("localhost","tweets","tweets","tweets" )
    cursor = db.cursor()
    sql2="DELETE FROM tweets"
    try:
        #La sentecia se ejecuta
        cursor.execute(sql2)
        #commit que hace los cambios en la base de datos.
        db.commit()
    except:
        #regresa la base de datos como estaba.
        db.rollback()
    #La conexion se cierra  
    db.close()

def selectDB():
    x=[]
    #Crea la conexion a mysql
    con = MySQLdb.connect("localhost","tweets","tweets","tweets" )

    cur = con.cursor()
    sql = "SELECT * FROM tweets"
    cur.execute(sql)
    results = cur.fetchall()
    #recorrer filas de lo que regresa la base de datos
    for r in results:
        x.append(r[1])
    return x
