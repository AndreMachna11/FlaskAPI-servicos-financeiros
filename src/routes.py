from src import app
from src.calculadoraJuros.views.JurosView import JurosView 
from src.autenticacao.views.autenticacaoView import AutenticacaoView
from src.inflacao.views.inflacaoView import InflacaoView

JurosView.register(app, route_base='/juros/')
AutenticacaoView.register(app, route_base='/autenticacao/')
InflacaoView.register(app,route_base='/inflacao/')