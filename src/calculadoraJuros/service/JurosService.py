class JurosService():

    
    def converte_taxa_mensal_para_anual(self,taxa):
        taxa = (1 + taxa) ** (1/12) - 1
        return taxa
    
    def converte_taxa_anual_para_mensal(self,taxa):
        taxa = ((1 + taxa) ** 12 ) - 1
        return taxa
    

    #Serviço que faz o calculo de juros simples
    def calcula_juros_simples(self,valor_presente,taxa,tempo):
        
        valor_futuro = valor_presente + valor_presente*taxa*tempo

        return float(format(valor_futuro,'.2f'))

    #Serviço que faz o calculo de juros compostos
    def calcula_juros_compostos(self,valor_inicial,valor_mensal,taxa,periodo,periodo_em,taxa_em):
        
        taxa = taxa/100

        if periodo_em.upper() == 'ANOS':
            if taxa_em.upper() == 'MENSAL':
                taxa_parcela_1 = self.converte_taxa_mensal_para_anual(taxa)
            else:
                taxa_parcela_1 = taxa    
        elif periodo_em.upper() == 'MESES':
            if taxa_em.upper() == 'ANUAL':
                taxa_parcela_1 = self.converte_taxa_anual_para_mensal(taxa)       
            else:
                taxa_parcela_1 = taxa 
        parcela_1 = valor_inicial*(1+taxa_parcela_1)**periodo
        
        if periodo_em.upper() == 'MESES':
            taxa_parcela_2 = taxa_parcela_1
        else:
            periodo = periodo*12
            taxa_parcela_2 = self.converte_taxa_mensal_para_anual(taxa)

        parcela_2 = valor_mensal*((((1+taxa_parcela_2)**periodo) - 1)/taxa_parcela_2)
        
        montante_final = parcela_1 + parcela_2
        valor_total_aportado = (valor_inicial + (valor_mensal*periodo))
        juros = montante_final - valor_total_aportado

        return montante_final, valor_total_aportado, juros
