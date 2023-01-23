from flask import Flask
from mongoengine import connect, Document, StringField, IntField
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

#Pool de conexões para o mongoDB utilizado
client_mongo = connect(host=os.getenv('string_de_conexao'), connect=False, maxPoolSize=500, db=os.getenv('database')) 

#Definição da classe Usuario que representa a coleção "usuarios_api" do banco de dados
class Usuario(Document):
    _id = IntField()
    usuario = StringField()
    senha = StringField() 
    ultimo_token_gerado = StringField() 
    data_geracao_ultimo_token = StringField() 
    meta = {'collection': 'usuarios_api'}

app = Flask(__name__)