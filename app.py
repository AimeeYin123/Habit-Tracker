import os
from flask import Flask
from routes import pages
from pymongo import MongoClient
from dotenv import load_dotenv
import pymongo
import certifi
import ssl
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

conn_str = "mongodb+srv://aimee19950406:Qazwsxedc135!@cluster0.3y2u2iz.mongodb.net/tracker?retryWrites=true&w=majority"
ssl_context = ssl.create_default_context(cafile=certifi.where())
client = pymongo.MongoClient(conn_str, server_api=ServerApi('1'), tlsCAFile=certifi.where())


load_dotenv()


def create_app():
    app = Flask(__name__)
    client = MongoClient(os.environ.get("MONGODB_URL"))
    app.db = client.get_default_database()

    app.register_blueprint(pages)
    return app