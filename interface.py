from PySimpleGUI import *
from op_B3 import *
from banco import *
theme('Darkblue12')
def janela_update():
    campo=['data', 'codigo', 'quantidade', 'valor_unitario' , 'tipo_op', 'corretagem']
    layout=[
        [Text('AtUALIZAÇÃO DE DADOS')],
        [Text('Campos: '), DropDown(campo, key='Update', default_value='data')],
        [Text('Alteração: '), Input(key='alterar', do_not_clear= False)],
        [Text('ID: '), Input(key='ids', size=(10, 10), do_not_clear=False)],
        [Text(key='Atualizar')],
        [Button('UPDATE')]
    ]
    return Window('ATUALIZAÇÃO DE DADOS', layout=layout, finalize=True)


def criar_tabela():
    headings2=['ID','DATA', 'CÓDIGO', 'QUANTIDADE', 'VALOR UNITARIO', 'TIPO OPERAÇÃO', 'CORRETAGEM', 'VALOR OPERAÇÃO SEM TAXA', 'TAXA B3', 'VALOR DA OPERAÇÃO']
    valores_tabela2=[]
    layout=[[Text('Pesquisar ação:'),Input(key='Pesquisa', size=(20, 20), do_not_clear=False), Button('Search')],
        [Text('Deletar ação: '),Input(key='Deleta',size=(10,10), do_not_clear=False), Button('Delete')],
        [Text(key='Tabela'),Table(values= valores_tabela2, headings= headings2,key= 'tabela',auto_size_columns= False, def_col_width= 15)],
        [Button('Mostrar Tabela'),Button('Cadastro de operações') ,Button('Fazer Alterções')]
    ]
    return Window('Tabela', layout=layout, finalize=True)

def cadastro():
    tipo=['compra', 'venda']
    layout=[
        [Text('Cadatro das operações', text_color='black' )],
        [Text('Data: ', text_color='black'),Input(size=(10,10),key='Date', do_not_clear=False)],
        [Text('Código:',  text_color='black',),Input(size=(10, 10), key='código', do_not_clear=False)],
        [Text('Quantidade:',  text_color='black'),Input(key='quantidade', do_not_clear=False)],
        [Text('Valor unitario: ',  text_color='black'),Input(key='valor_unitario',do_not_clear=False)],
        [Text('Tipo de operação',  text_color='black'),DropDown(tipo,size=(10,10),key= 'Tipo_de_operação', default_value= 'compra')],
        [Text('Corretagem: ',  text_color='black'),Input(key='corretagem', do_not_clear=False)],
        [Button('Salvar'), Button('Fechar Programa'), Button('Mostrar Tabela')],
        [Text(key='Valor da operação')],
    ]
    return Window('SHELBY STOCKS', layout= layout, finalize=True)

#João Emanuel
janela1, janela2, janela3= cadastro(), criar_tabela(), None

while True:
    window, eventos, valores= read_all_windows()
    if window == janela1 and eventos == WIN_CLOSED:
        janela1.close()
    if window == janela1 and eventos == 'Fechar Programa':
        break
    if window == janela2 and eventos == 'Cadastro de operações':
        janela1 = cadastro()
    if window == janela1 and eventos == 'Mostrar Tabela':
        janela2= criar_tabela()
    if window == janela1 and  eventos == 'Salvar':
        quantidades= valores['quantidade']
        valor_unit= valores['valor_unitario']
        corretagens= valores['corretagem']
        if valores['Date'] == '' or valores['código'] == '' or valores['quantidade'] == '' or valores['Tipo_de_operação'] == '' or valores['valor_unitario'] == '' or valores['corretagem'] == '' :
            popup('Você não completou todos os campos')
        else:
            try:
                valor= int(quantidades)
                valor2= float(valor_unit)
                valor3= float(corretagens)
            except:
                popup('Quantidade, valor unitario e corretagem inválido. Digite novamente')
            else:
                datas= valores['Date']
                codigos= valores['código']
                tipo_operacao= valores['Tipo_de_operação']
                banco= BancoOperacao()
                acao= OperacaoB3(datas,codigos, valor, valor2, tipo_operacao, valor3)
                banco.cadastrar_acao(acao.data, acao.codigo, acao.quantidade, acao.valor_unitario,
                            acao.tipo, acao.corretagem, acao.valor_operacao_sem_taxa,
                            acao.taxaB3, acao.valor_operacao_com_taxa)
    if window == janela2 and eventos == WIN_CLOSED:
        janela2.close()
    if window == janela2 and eventos == 'Mostrar Tabela':
        banco2= BancoOperacao()
        valor= [banco2.mostrar_acoes()]
        valores_tabela2= []
        janela2['tabela'].update(valores_tabela2)
        for acao in valor:
            for dados in acao:
                valores_tabela2.append(dados)
        janela2['tabela'].update(valores_tabela2)

            
    if window == janela2 and eventos == 'Search':
        codi= valores['Pesquisa']
        banco3= BancoOperacao()
        lista_pesquisa= banco3.pesquisar_acao(codi)
        valores_tabela2= []
        janela2['tabela'].update(valores_tabela2)
        for i in lista_pesquisa:
            valores_tabela2.append(i)
        janela2['tabela'].update(valores_tabela2)

    if window == janela2 and eventos == 'Delete':
        id= valores['Deleta']
        if id == '':
            popup('Você não colocou nenhuma informação')
        else:
            try:
                valor= int(id)
            except:
                popup('Valor não é inteiro')
            else:
                banco4= BancoOperacao()
                banco4.deletar_acao(id)
                popup(f'A ação que possui o id {id} foi deletado',auto_close= True ,auto_close_duration=2)
                janela2['tabela'].update(valores_tabela2)
    if window == janela2 and eventos == 'Fazer Alterções':
        janela3= janela_update()

    if window == janela3 and eventos == WIN_CLOSED:
        janela3.close()

    if window == janela3 and eventos == 'UPDATE':
        campo2= valores['Update']
        alterar= valores['alterar']
        id2= valores['ids']
        if alterar == '' or id2 == '':
            popup('Você não completou  todos os campos')
        else:
            banco5= BancoOperacao()
            banco5.atualizar_acao(campo2, alterar, id2)
            valor= [banco5.mostrar_acoes()]
            valores_tabela2= []
            janela2['tabela'].update(valores_tabela2)
            for acao in valor:
                for dados in acao:
                    valores_tabela2.append(dados)
            janela2['tabela'].update(valores_tabela2)