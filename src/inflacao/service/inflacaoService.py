from src import client_mongo, IndicesInflacao
import json

class InflacaoService():
    def retorna_indices_inflacao(self,data,indice):
        
        if data.lower() != 'all':
            #Abre uma conexão da pool e busca um usuario no banco de dados
            with client_mongo.start_session() as session:
                with session.start_transaction():
                    indice = IndicesInflacao.objects(_id = data + '-01*' + indice.upper())
            client_mongo.close()
        else:
            #Abre uma conexão da pool e busca um usuario no banco de dados
            with client_mongo.start_session() as session:
                with session.start_transaction():
                    indice = IndicesInflacao.objects(tipo = indice.upper())        
            client_mongo.close()

        #Trata o retorno do banco de dados
        indice = indice.to_json()
        indice = json.loads(indice)

        return indice
        