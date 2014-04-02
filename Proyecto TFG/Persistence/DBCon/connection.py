# -*- coding: utf-8 -*-
import mysql.connector
from mysql.connector import errorcode


def dbconnect():
    cnx = None
    try:
        cnx = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='database')
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Usuario o contraseña erroneos.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("La base de datos no existe.")
        else:
            print(err)
    return cnx


def dbdisconect(cnx):
    cnx.close()
