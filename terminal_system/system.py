from comandos import *

def menu():
    while True:
        print("Protótipo Sistema Terminal Rosa's Consultoria, o que deseja?\n",
        "(1)Cadastrar Consultor\n",
        "(2)Cadastrar Cliente\n",
        "(3)Criar Contrato\n",
        "(4)Visualizar Consultores\n",
        "(5)Visualizar Consultor\n",
        "(s)Sair do Sistema\n")
        inp = input()
        if inp == 1:post_consultor()
        if inp == 2:put_cliente()
        if inp == 3:get_contrato()
        if inp == 4:get_consultores()
        if inp == 5: get_consultor()
        if inp == s:break
        else:print('Comando Inválido')