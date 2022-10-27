from PySimpleGUI import *
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