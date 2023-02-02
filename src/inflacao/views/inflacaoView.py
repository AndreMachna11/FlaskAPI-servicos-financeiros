from flask_classful import FlaskView, route
from flask import request
from src.autenticacao.service.autenticacaoService import AutenticacaoService
from src.inflacao.service.inflacaoService import InflacaoService
from src import GeraResponse

class InflacaoView(FlaskView):
    route_base = 'inflacao'

    @route('/indice',methods=['GET'])
    def retorna_ipca_historico_ou_mes(self):
        
        #Instancia que gerará o response
        RESPONSE = GeraResponse()

        #Le os dados enviados no cabeçalho da requisição
        body = request.get_json()
        headers = request.headers

        #Verificação de Existencia do token no cabeçalho
        try:
            token = headers['token']
        except:
            return RESPONSE.gera_response(400,"TOKEN NAO ENVIADO",{}) 

        #Verificando Validade do Token Informado no cabeçalho
        try:
            AUTENTICADOR = AutenticacaoService()
            valida_token = AUTENTICADOR.verifica_validade_token(token)

            if valida_token != True:
                if valida_token == 'TOKEN EXPIRADO':
                    return RESPONSE.gera_response(400,"TOKEN EXPIRADO",{})
                else:
                    return RESPONSE.gera_response(400,"TOKEN INVALIDO",{})
        except:
            return RESPONSE.gera_response(500,"ERRO INTERNO",{})
    

        #Verificação de existencia e validade da variavel "data"
        try:
            data = body['data']
            if data != 'all':
                if len(data) != 7:
                    return RESPONSE.gera_response(400,"DATA INVALIDA - USE O FORMATO YYYY-MM",{}) 
                if '-' not in data:
                    return RESPONSE.gera_response(400,"DATA INVALIDA - USE O FORMATO YYYY-MM",{})
                try:
                    mes = float(data.split('-')[-1]) 
                    if mes < 0 or mes > 12:
                        return RESPONSE.gera_response(400,"MES INVALIDO",{})
                except:
                    return RESPONSE.gera_response(400,"MES INVALIDO",{})
            else:
                pass
        except:
            return RESPONSE.gera_response(400,"DATA NAO ENVIADO NO CORPO DA REQUISICAO",{}) 
        

        #Verificação de existencia e validade da variavel "indice"
        try:
            indice = str(body['indice'])
            if len(indice) != 4:
                return RESPONSE.gera_response(400,"INDICE INVALIDO - USE O FORMATO YYYY",{})
        except:
            return RESPONSE.gera_response(400,"INDICE NAO ENVIADO NO CORPO DA REQUISICAO",{}) 

        #Chamada do Serviço e montagem da resposta em json
        try:
            INFLACAO = InflacaoService()
            indices = INFLACAO.retorna_indices_inflacao(data,indice)
            
            dict_retorno = {
                "indices" : indices
            }

            return RESPONSE.gera_response(200,"SUCESSO",dict_retorno)
        except:
            return RESPONSE.gera_response(500,"ERRO INTERNO",{})






