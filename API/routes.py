# handels requests, validates inputs, calls database layers

from flask import Flask, Blueprint, jsonify
import database

api = Blueprint('api', __name__)

@api.route('/')
def home():
    return 'URL webpage for backend database, you are not meant to see this page :O'

# View users
@api.route('/view_users', methods=["GET"])
def get_users():
    conn = database.db_connect()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        cursor.close()
    finally:
        conn.close()
    return jsonify(rows)

# View sensors
@api.route('/view_sensors', methods=["GET"])
def get_sensors():
    conn = database.db_connect()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM sensor_types")
        rows = cursor.fetchall()
        cursor.close()
    finally:
        conn.close()
    return jsonify(rows)

# Add a new user to the database
@api.route('/new_user/<name>', methods=['POST'])
def add_user(name):
    conn = database.db_connect()
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name) values (%s);", (name,))
        conn.commit()
        cursor.close()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()
    return '', 204

# Add a new sensor to the database
@api.route('/new_sensor/<name>/<unit>', methods=['POST'])
def new_sensor(name, unit):
    conn = database.db_connect()
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO sensor_types (name, unit) values (%s, %s);", (name,unit,))
        conn.commit()
        cursor.close()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()
    return '', 204

@api.route('/new_read/<user_id>/<sensor_type_id>/<value>', methods=['POST'])
def new_read(user_id, sensor_type_id, value):
    conn = database.db_connect()
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO readings (user_id, sensor_type_id, value, rec_time) values (%s, %s, %s,NOW(3));", (user_id,sensor_type_id,value))
        conn.commit()
        cursor.close()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()
    return '', 204