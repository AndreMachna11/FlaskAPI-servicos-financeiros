from flask import Flask
from mongoengine import connect, Document, StringField, IntField, FloatField
import os
import json
import datetime
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

#Pool de conexões para o mongoDB utilizado
client_mongo = connect(host=os.getenv('string_de_conexao'), connect=False, maxPoolSize=50, db=os.getenv('database')) 

#Varivel que salva os token´s validos ativos para ser usado quando o usuario ja esta auteticado, diminuindo requisiçoes no banco de dados que conferem se o token usado existe e é valido
cache_tokens = {os.getenv('token_mestre') : datetime.datetime.now() + datetime.timedelta(days=365*100)}

#Classe que padroniza a geração de response dos serviços da api
class GeraResponse():
    def gera_response(self,status_code,message_response,body):

        dict_retorno = {
            "status_code": int(status_code),
            "message_response": str(message_response),
            "body": body
        }       

        return json.dumps(dict_retorno), int(status_code)

#Definição da classe Usuario que representa a coleção "usuarios_api" do banco de dados
class Usuario(Document):
    _id = IntField()
    usuario = StringField()
    senha = StringField() 
    ultimo_token_gerado = StringField() 
    data_geracao_ultimo_token = StringField() 
    meta = {'collection': 'usuarios_api'}

#Definição da classe IndicesInflacao que representa a coleção "indices_inflacao" do banco de dados
class IndicesInflacao(Document):
    _id = StringField()
    data = StringField()
    tipo = StringField()
    valor = FloatField()
    meta = {'collection': 'indices_inflacao'}

app = Flask(__name__)