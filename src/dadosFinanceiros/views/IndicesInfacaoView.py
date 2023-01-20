from flask_classful import FlaskView, route
from flask import request


class IndicesInfacaoView(FlaskView):
    route_base = 'indicesDeInflacao'

    @route('/ipca',methods=['GET', 'POST'])
    def retorna_ipca_perioso(self):
        pass
    
    @route('/igpm',methods=['GET', 'POST'])
    def retorna_igpm_perioso(self):
        pass


