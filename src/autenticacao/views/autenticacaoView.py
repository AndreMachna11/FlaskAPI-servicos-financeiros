from flask_classful import FlaskView, route
from flask import request
import json
from src.autenticacao.service.autenticacaoService import AutenticacaoService
from src import GeraResponse

class AutenticacaoView(FlaskView):
    route_base = 'autenticacao'

    @route('/login',methods=['GET', 'POST'])
    def gera_token(self):
        
        #Instancia que gerará o response
        RESPONSE = GeraResponse()

        #Le os dados enviados no cabeçalho da requisição
        headers = request.headers

        #Verifica se a informação "usuario" foi enviada
        try:
            usuario = headers['usuario']
        except: 
            return RESPONSE.gera_response(400,"USUARIO NAO ENVIADO",{})
        
        #Verifica se a informação senha foi enviada
        try:
            senha = headers['senha']
        except:
            return RESPONSE.gera_response(400,"SENHA NAO ENVIADA",{})

        #Chama o serviço que faz a verificação se o usuario informado tem permissão para usar a api e se sim retorna um token valido por 24 horas
        try:
            AUTENTICADOR = AutenticacaoService()
            token = AUTENTICADOR.login(usuario,senha)

            if len(token) == 64:
                body = {
                    "token" : token
                }
                return RESPONSE.gera_response(200,"SUCESSO",body)
            else:
                return RESPONSE.gera_response(400,token,{})
        except:
            return RESPONSE.gera_response(500,"ERRO INTERNO NO SERVIDOR",{})
            

          