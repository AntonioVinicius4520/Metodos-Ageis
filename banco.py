import sqlite3

from op_B3 import OperacaoB3


class BancoOperacao():
    def __init__(self):
        self.con = sqlite3.connect("operacaoB3.db")
        self.cur = self.con.cursor()

    # Testando!
    def cadastrar_acao(self, data, codigo, quantidade, valor_unitario, tipo,
                       corretagem, valor_op_sem_taxa, taxa_b3,
                       valor_op_com_taxa):
        dados_operacao = [(data, codigo.upper(), quantidade, valor_unitario,
                           tipo, corretagem, valor_op_sem_taxa, taxa_b3,
                           valor_op_com_taxa)]

        self.cur.executemany('''INSERT INTO acao
                                (data, codigo, quantidade, valor_unitario,
                                tipo_op, corretagem, valor_operacao_sem_taxa,
                                taxa_b3, valor_operacao_com_taxa) VALUES
                                (?, ?, ?, ?, ?, ?, ?, ?, ?)''', dados_operacao)

        self.con.commit()

    # Testando!
    def pesquisar_acao(self, codigo):
        lista_pesquisa = []
        for row in self.cur.execute(f"SELECT * FROM acao WHERE codigo='{codigo}'"):
            lista_pesquisa.append(row)
        return lista_pesquisa

    def mostrar_acoes(self):
        lista_acao = []
        for row in self.cur.execute("SELECT * From acao ORDER BY id DESC"):
            lista_acao.append(row)
        return lista_acao

    def deletar_acao(self, id):
        self.cur.execute(f"DELETE FROM acao WHERE id={id}")
        self.con.commit()

    def calcular_media_acoes(self):
        lista_valores = []
        for row in self.cur.execute(
                "SELECT valor_operacao_com_taxa FROM acao"):
            lista_valores.append(row[0])
        return round(sum(lista_valores)/len(lista_valores), 2)

    def atualizar_acao(self, campo, alteracao, id):
        if campo in ['tipo_op', 'codigo', 'data']:
            self.cur.execute(
                f"UPDATE acao SET {campo} = '{alteracao}' WHERE id={id} ")
        else:
            self.cur.execute(
                f"UPDATE acao SET {campo} = {alteracao} WHERE id={id} ")
        self.con.commit()
        acao = self.coletar_e_recalcular_acao(id)
        self.cur.execute(f"""UPDATE acao SET
                                data = '{acao.data}',
                                codigo = '{acao.codigo}',
                                quantidade = {acao.quantidade},
                                valor_unitario = {acao.valor_unitario},
                                tipo_op = '{acao.tipo}',
                                corretagem = {acao.corretagem},
                                valor_operacao_sem_taxa = {acao.valor_operacao_sem_taxa},
                                taxa_b3 = {acao.taxaB3},
                                valor_operacao_com_taxa = {acao.valor_operacao_com_taxa}
                            WHERE id={id}
                        """)
        self.con.commit()

    def coletar_e_recalcular_acao(self, id):
        dados_acao = []
        for row in self.cur.execute(f"SELECT * From acao WHERE id={id}"):
            for dados in row:
                dados_acao.append(dados)
        acao = OperacaoB3(dados_acao[1], dados_acao[2], dados_acao[3],
                          dados_acao[4], dados_acao[5], dados_acao[6])
        return acao
