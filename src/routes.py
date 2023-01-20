from src import app
from src.dadosFinanceiros.views.IndicesInfacaoView import IndicesInfacaoView
from src.dadosFinanceiros.views.JurosView import JurosView 
from src.autenticacao.views.autenticacaoView import AutenticacaoView

IndicesInfacaoView.register(app, route_base='/indicesDeInflacao/')
JurosView.register(app, route_base='/juros/')
AutenticacaoView.register(app, route_base='/autenticacao/')





