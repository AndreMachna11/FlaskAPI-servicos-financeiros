from src import client_mongo
import secrets
import datetime as dt
from datetime import datetime

class AutenticacaoService():

    def login(self,usuario,senha):
        
        db = client_mongo['ServicosFinanceiros']
        collection = db['usuarios_api']
        usuario = list(collection.find({"usuario":usuario}))
        
        if not usuario:
            return 'USUARIO NAO ENCONTRADO'

        if usuario[0]['senha'] != senha:
            return 'SENHA ERRADA'

        token = secrets.token_hex(32)

        filter = {"_id": usuario[0]['_id']}
        update = {"ultimo_token_gerado": token,"data_geracao_ultimo_token":str(dt.datetime.now())}
        collection.find_one_and_update(filter, {'$set': update},upsert=True)

        return token

    def verifica_validade_token(self,token):
        
        db = client_mongo['ServicosFinanceiros']
        collection = db['usuarios_api']
        usuario = list(collection.find({"ultimo_token_gerado":token}))
        
        print(usuario)

        if not usuario:
            return 'TOKEN INVALIDO'

        data_geracao_ultimo_token = str(usuario[0]['data_geracao_ultimo_token']).split('.')[0]

        data_geracao_ultimo_token = datetime.strptime(data_geracao_ultimo_token, '%Y-%m-%d %H:%M:%S')
        
        difference = dt.datetime.now() - data_geracao_ultimo_token

        if difference.total_seconds() > 86400:
            return 'TOKEN EXPIRADO'

        return True


