API criada com o objetivo de aplicar e ampliar conhecimentos em Python e Flask

-FlaskAPI

-Integração com MongoDB

-Pool de conexões com MondoDB

-Sistema de autenticação de login e senha para geração de tokens

-Token de acesso que expira em um determinado tempo setado 

-Token obrigatorio para uso dos serviços 

-Chekagem de tokens via cache para minimizar consultas ao banco de dados

-Responses padronizados em todos os serviços

Serviços:

      -Autenticação de usuarios 
      
      -Calculo de juros simples
      
      -Calculo de juros compostos (considerando aportes mensais na aplicação)
      
      -Consulta de indices de inflação IPCA e IGPM por data (Banco de dados proprio construido em mongoDB)
      
      -Correção de um determinado valor de dinheiro por IPCA ou IGPM para um determinado periodo de tempo
