from flask_classful import FlaskView, route
from flask import request
import json
from src.autenticacao.service.autenticacaoService import AutenticacaoService

class AutenticacaoView(FlaskView):
    route_base = 'autenticacao'

    @route('/login',methods=['GET', 'POST'])
    def gera_token(self):

        headers = request.headers

        try:
            usuario = headers['usuario']
        except:
            return '400 - USUARIO NAO ENVIADO'
        
        try:
            senha = headers['senha']
        except:
            return '400 - SENHA NAO ENVIADA'

        try:
        
            AUTENTICADOR = AutenticacaoService()
            token = AUTENTICADOR.login(usuario,senha)

            if len(token) == 64:
                dict_retorno = {"token" : token}
                return json.dumps(dict_retorno)
            else:
                return token
        except:
            return '500 - ERRO INTERNO'

    
        
        


