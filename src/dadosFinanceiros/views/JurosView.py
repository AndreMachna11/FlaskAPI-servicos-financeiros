from flask_classful import FlaskView, route
from flask import request
import json
from src.dadosFinanceiros.service.JurosService import JurosService
from src.autenticacao.service.autenticacaoService import AutenticacaoService

class JurosView(FlaskView):
    route_base = 'juros'

    @route('/jurosSimples',methods=['GET', 'POST'])
    def calcula_juros_simples(self):

        #Acessa dados enviados no corpo da requisição
        body = request.get_json()

        #Verificação de existencia e validade da variavel "valor_presente"
        try:
            valor_presente = body['valor_presente']
            try:
                valor_presente = float(valor_presente)
            except:
                return '400 - VALOR PRESENTE INVALIDO'
        except:
            return '400 - VALOR PRESENTE NÃO ENVIADO NO CORPO DA REQUISIÇÃO'
        

        #Verificação de existencia e validade da variavel "taxa"
        try:
            taxa = body['taxa']
            try:
                taxa = float(taxa)
            except:
                return '400 - TAXA DE JUROS PRESENTE INVALIDA'
        except:
            return '400 - TAXA DE JUROS NÃO ENVIADA NO CORPO DA REQUISIÇÃO'
        

        #Verificação de existencia e validade da variavel "periodo"
        try:
            periodo = body['periodo']
            try:
                periodo = float(periodo)
            except:
                return '400 - PERIODO DE TEMPO INVALIDO'
        except:
            return '400 - PERIODO DE TEMPO NÃO ENVIADO NO CORPO DA REQUISIÇÃO'

        #Chamada do Serviço e montagem da resposta em json
        try:
            JUROS = JurosService()
            valor_futuro = JUROS.calcula_juros_simples(valor_presente,taxa,periodo)

            dict_retorno = {"valor_futuro" : str(valor_futuro)}
            return json.dumps(dict_retorno)
        except:
            return '500 - ERRO INTERNO'


        return str(valor_futuro)

    
    @route('/jurosCompostos',methods=['GET', 'POST'])
    def calcula_juros_compostos(self):
        
        #Acessa dados enviados no corpo da requisição
        body = request.get_json()
        headers = request.headers
        
        try:
            token = headers['token']
        except:
            return '400 - TOKEN INVALIDO'

        AUTENTICADOR = AutenticacaoService()
        valida_token = AUTENTICADOR.verifica_validade_token(token)

        if valida_token != True:
            if valida_token == 'TOKEN EXPIRADO':
                return '400 - TOKEN EXPIRADO'
            else:
                return '400 - TOKEN INVALIDO'

        #Verificação de existencia e validade da variavel "valor_presente"
        try:
            valor_presente = body['valor_presente']
            try:
                valor_presente = float(valor_presente)
            except:
                return '400 - VALOR PRESENTE INVALIDO'
        except:
            return '400 - VALOR PRESENTE NÃO ENVIADO NO CORPO DA REQUISIÇÃO'

        #Verificação de existencia e validade da variavel "taxa"
        try:
            taxa = body['taxa']
            try:
                taxa = float(taxa)
            except:
                return '400 - TAXA DE JUROS PRESENTE INVALIDA'
        except:
            return '400 - TAXA DE JUROS NÃO ENVIADA NO CORPO DA REQUISIÇÃO'
        
        #Verificação de existencia e validade da variavel "periodo"
        try:
            periodo = body['periodo']
            try:
                periodo = float(periodo)
            except:
                return '400 - PERIODO DE TEMPO INVALIDO'
        except:
            return '400 - PERIODO DE TEMPO NÃO ENVIADO NO CORPO DA REQUISIÇÃO'
        
        #Chamada do Serviço e montagem da resposta em json
        try:
            JUROS = JurosService()
            valor_futuro = JUROS.calcula_juros_compostos(valor_presente,taxa,periodo)  
            
            dict_retorno = {"valor_futuro" : str(valor_futuro)}
            return json.dumps(dict_retorno)
        except:
            return '500 - ERRO INTERNO'

