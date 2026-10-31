# handels requests, validates inputs, calls database layers

from flask import Flask, Blueprint, jsonify
import database

api = Blueprint('api', __name__)

@api.route('/')
def home():
    return 'Hello, World'

@api.route('/test')
def get_item():
    conn = database.db_connect()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id, name FROM test")
        rows = cursor.fetchall()
        cursor.close()
    finally:
        conn.close()
    return jsonify(rows)