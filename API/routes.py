# handels requests, validates inputs, calls database layers

from flask import Flask, Blueprint, jsonify
import database

api = Blueprint('api', __name__)

@api.route('/')
def home():
    return 'URL webpage for backend database, you are not meant to see this page :O'

@api.route('/view', methods=["GET"])
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

# Delete an entire row from the tbale (i.e. deleting a user account)
# Will NOT reset auto-increment to preserve unique ID
@api.route('/rm/<int:item_id>', methods=["DELETE"])
def rm_item(item_id):
    conn = database.db_connect()
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM test WHERE id = %s", (item_id,))
        conn.commit()
        cursor.close()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()
    return '', 204

# Add a new row to the table (i.e. adding a new user account)
@api.route('/post/<name>', methods=["POST"])
def post_item(name):
    conn = database.db_connect()
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO test (name) values (%s)", (name,))
        conn.commit()
        cursor.close()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()
    return '', 204