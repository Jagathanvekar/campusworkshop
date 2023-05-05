"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chaa8r3hp8u791gsogk0-a.oregon-postgres.render.com",
        database="todoapp_mc0m",
        user="todo",
        password="EymFe700FJfoXSzwSk6z0IVTtVZzw0rd")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
