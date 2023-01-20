from flask import Flask
import pymongo
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

client_mongo = pymongo.MongoClient(os.getenv('string_de_conexao'))
app = Flask(__name__)