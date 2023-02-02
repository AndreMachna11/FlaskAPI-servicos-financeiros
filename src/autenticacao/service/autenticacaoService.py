from src import client_mongo, Usuario
import secrets
import datetime as dt
from datetime import datetime
import json
import hashlib
from src import cache_tokens

class AutenticacaoService():

    def login(self,user,password):
       
        #Abre uma conexão da pool e busca um usuario no banco de dados
        with client_mongo.start_session() as session:
            with session.start_transaction():
                usuario = Usuario.objects(usuario = user)
        client_mongo.close()

        #Trata o retorno do banco de dados
        usuario = usuario.to_json()
        usuario = json.loads(usuario)

        #Verifica se o usuario existe
        if not usuario:
            return 'USUARIO NAO ENCONTRADO'

        #Verifica se a senha está correta
        if usuario[0]['senha'] != hashlib.md5((password).encode()).hexdigest():
            return 'SENHA ERRADA'

        #Gera um token aleatorio de 64 caracteres
        token = secrets.token_hex(32)

        #Registra mo banco de dados a hora de geração e o token escolhidos
        with client_mongo.start_session() as session:
            with session.start_transaction():
                usuario = Usuario.objects(_id = usuario[0]['_id']).modify(set__data_geracao_ultimo_token = str(dt.datetime.now()),set__ultimo_token_gerado = token)
        client_mongo.close()

        return token

    def verifica_validade_token(self,token):
        
        #Checka se o token existe entre os token existentes gerados para usuarios validos
        try:
            validade = cache_tokens[token]
        except:
            return 'TOKEN INVALIDO'
        
        #Checka se além de exitir ele foi gerado dentro das ultimas 24 horas
        difference = dt.datetime.now() - validade
        if difference.total_seconds() > 86400:
            del cache_tokens[token]
            return 'TOKEN EXPIRADO'

        return True