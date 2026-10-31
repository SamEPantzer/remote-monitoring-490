# handels MySQL connections

import mysql.connector
import pymysql
import config

def db_connect():
    return pymysql.connect(
        host="localhost",
        user="root",
        password=config.root_pass,
        database="capstone",
        cursorclass=pymysql.cursors.DictCursor,
    )