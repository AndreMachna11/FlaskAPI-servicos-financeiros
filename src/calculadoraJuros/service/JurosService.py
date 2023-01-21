class JurosService():

    #Serviço que faz o calculo de juros simples
    def calcula_juros_simples(self,valor_presente,taxa,tempo):
        
        valor_futuro = valor_presente + valor_presente*taxa*tempo

        return float(format(valor_futuro,'.2f'))

    #Serviço que faz o calculo de juros compostos
    def calcula_juros_compostos(self,valor_presente,taxa,tempo):
        
        valor_futuro = valor_presente*((1+taxa)**tempo)

        return float(format(valor_futuro,'.2f'))
