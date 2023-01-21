from src import app
from src.calculadoraJuros.views.JurosView import JurosView 
from src.autenticacao.views.autenticacaoView import AutenticacaoView

JurosView.register(app, route_base='/juros/')
AutenticacaoView.register(app, route_base='/autenticacao/')





