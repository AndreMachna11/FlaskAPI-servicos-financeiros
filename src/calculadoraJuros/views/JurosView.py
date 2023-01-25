from flask_classful import FlaskView, route
from flask import request
import json
from src.calculadoraJuros.service.JurosService import JurosService
from src.autenticacao.service.autenticacaoService import AutenticacaoService
from src import GeraResponse

class JurosView(FlaskView):
    route_base = 'juros'

    @route('/jurosCompostos',methods=['GET', 'POST'])
    def calcula_juros_compostos(self):
        
        #Instancia que gerará o response
        RESPONSE = GeraResponse()

        #Acessa dados enviados no corpo da requisição
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

        #Verificação de existencia e validade da variavel "valor_inicial"
        try:
            valor_inicial = body['valor_inicial']
            try:
                valor_inicial = float(valor_inicial)
            except:
                return RESPONSE.gera_response(400,"VALOR INICIAL INVALIDO",{}) 
        except:
            return RESPONSE.gera_response(400,"VALOR INICIAL NAO ENVIADO NO CORPO DA REQUISICAO",{}) 

        #Verificação de existencia e validade da variavel "valor_mensal"
        try:
            valor_mensal = body['valor_mensal']
            try:
                valor_mensal = float(valor_mensal)
            except:
                return RESPONSE.gera_response(400,"VALOR MENSAL INVALIDO",{}) 
        except:
            return RESPONSE.gera_response(400,"VALOR MENSAL NAO ENVIADO NO CORPO DA REQUISICAO",{}) 

        #Verificação de existencia e validade da variavel "taxa"
        try:
            taxa = body['taxa']
            try:
                taxa = float(taxa.strip('%'))
            except:
                return RESPONSE.gera_response(400,"TAXA DE JUROS INVALIDA",{}) 
        except:
            return RESPONSE.gera_response(400,"TAXA DE JUROS NAO ENVIADA NO CORPO DA REQUISICAO",{}) 
        
        #Verificação de existencia e validade da variavel "periodo"
        try:
            periodo = body['periodo']
            try:
                periodo = int(periodo)
            except:
                return RESPONSE.gera_response(400,"PERIODO DE TEMPO INVALIDO",{}) 
        except:
            return RESPONSE.gera_response(400,"PERIODO DE TEMPO NAO ENVIADO NO CORPO DA REQUISICAO",{})
        
        #Verificação de existencia e validade da variavel "periodo_em"
        try:
            periodo_em = body['periodo_em']
            if periodo_em.upper() == 'ANOS' or periodo_em.upper() == 'MESES':
                pass
            else:
                return RESPONSE.gera_response(400,"periodo_em INVALIDO",{}) 
        except:
            return RESPONSE.gera_response(400,"periodo_em NAO ENVIADO NO CORPO DA REQUISICAO",{})

        #Verificação de existencia e validade da variavel "taxa_em"
        try:
            taxa_em = body['taxa_em']
            if taxa_em.upper() == 'ANUAL' or taxa_em.upper() == 'MENSAL':
                pass
            else:
                return RESPONSE.gera_response(400,"taxa_em INVALIDO",{}) 
        except:
            return RESPONSE.gera_response(400,"taxa_em NAO ENVIADO NO CORPO DA REQUISICAO",{})

        #Chamada do Serviço e montagem da resposta em json
        try:
            JUROS = JurosService()
            montante_final,valor_total_aportado,valor_recebido_em_juros = JUROS.calcula_juros_compostos(valor_inicial,valor_mensal,taxa,periodo,periodo_em,taxa_em)
            
            dict_retorno = {
                "montante_final" : str(montante_final),
                "valor_total_aportado": str(valor_total_aportado),
                "valor_recebido_em_juros" : str(valor_recebido_em_juros)
            }
            return RESPONSE.gera_response(200,"SUCESSO",dict_retorno)
        except:
            return RESPONSE.gera_response(500,"ERRO INTERNO",{})
    
    @route('/jurosSimples',methods=['GET', 'POST'])
    def calcula_juros_simples(self):

        #Instancia que gerará o response
        RESPONSE = GeraResponse()

        #Acessa dados enviados no corpo da requisição e no cabeçalho
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

        #Verificação de existencia e validade da variavel "valor_presente"
        try:
            valor_presente = body['valor_presente']
            try:
                valor_presente = float(valor_presente)
            except: 
                return RESPONSE.gera_response(400,"VALOR PRESENTE INVALIDO",{})
        except:
            return RESPONSE.gera_response(400,"VALOR PRESENTE NAO ENVIADO NO CORPO DA REQUISICAO",{})
        

        #Verificação de existencia e validade da variavel "taxa"
        try:
            taxa = body['taxa']
            try:
                taxa = float(taxa)
            except:
                return RESPONSE.gera_response(400,"TAXA DE JUROS INVALIDA",{})
        except:
            return RESPONSE.gera_response(400,"TAXA DE JUROS ENVIADO NO CORPO DA REQUISICAO",{})
        
        #Verificação de existencia e validade da variavel "periodo"
        try:
            periodo = body['periodo']
            try:
                periodo = float(periodo)
            except:
                return RESPONSE.gera_response(400,"PERIODO DE TEMPO INVALIDO",{})
        except:
            return RESPONSE.gera_response(400,"PERIODO DE TEMPO NAO ENVIADO NO CORPO DA REQUISICAO",{})

        #Chamada do Serviço e montagem da resposta em json
        try:
            JUROS = JurosService()
            valor_futuro = JUROS.calcula_juros_simples(valor_presente,taxa,periodo)

            dict_retorno = {"valor_futuro" : str(valor_futuro)}
            return RESPONSE.gera_response(200,"SUCESSO",dict_retorno)
        except:
            return RESPONSE.gera_response(500,"ERRO INTERNO",{})


