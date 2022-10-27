class OperacaoB3():
    def __init__(self, data, codigo, quantidade, valor_unitario, tipo, corretagem):
        self.data = data
        self.codigo = codigo
        self.quantidade = quantidade
        self.valor_unitario = valor_unitario
        self.tipo = tipo
        self.corretagem = corretagem
        # self.data = data
        self.valor_operacao_sem_taxa = self.valor_unitario * self.quantidade
        self.taxaB3 = self.valor_operacao_sem_taxa * (0.03 / 100)
        self.valor_operacao_com_taxa = self.calcular_operacao()

    # Funcionando!
    def calcular_operacao(self):
        if self.tipo.lower() in ['c', 'compra']:
            self.valor_operacao_com_taxa = round(self.valor_operacao_sem_taxa +
                                                 self.corretagem + self.taxaB3, 2)
        elif self.tipo.lower() in ['v', 'venda']:
            self.valor_operacao_com_taxa = self.valor_operacao_sem_taxa - \
                self.corretagem - self.taxaB3
        return self.valor_operacao_com_taxa
