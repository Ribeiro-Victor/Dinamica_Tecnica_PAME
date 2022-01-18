from classes import Cliente, Consultor, Contrato

s=None
contratos={}
clientes = {}
consultores = {}

#Bloco de funções do Menu principal
def post_consultor():
    username = input("Username\n")
    password = input("Password\n")
    c = Consultor(username, password)
    consultores[c.id] = c
    print("Consultor adicionado ao sistema!")
    return None

def put_cliente():
    username = input("Username\n")
    password = input("Password\n")
    c = Cliente(username, password)
    clientes[c.id] = c
    print("Cliente adicionado ao sistema!")
    return None
          
def get_contrato():
    title = input("Title\n")
    description = input("Description\n")
    end_period = input("End Period\n")

    if len(clientes)==0 or len(consultores)==0:
        print("Não há clientes e/ou consultores cadastrados.")
        return None
    else:
        cliente = clientes[input('Id do cliente:\n')]
        consultor = consultores[input('Id do consultor:\n')]
    
    contrato = Contrato(title,end_period,description=description,associates=f'{cliente}/{consultor}')
    contratos[f'{contrato.id}']=contrato
    print("Contrato adicionado ao sistema!")
    return None

def put_contrato():
    try:contrato = contratos[input("Id do Contrato:\n")]
    except KeyError:
        print("Não existe contrato com esse id")
    contrato.conclude_contract()

def get_consultores():
    print("Consultor Log")
    for consultor in consultores.values():
        consultor.view()
    print("----------------------------")

def get_consultor():
    print("Consultor Log")
    print()
    id = input("Id do consultor")
    consultores[id].view()
    print("----------------------------")

def get_clientes():
    print("Clientes Log")
    for cliente in clientes.values():
        cliente.view()
    print("----------------------------")