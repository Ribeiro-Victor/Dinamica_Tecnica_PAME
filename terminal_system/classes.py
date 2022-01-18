from random import randint
import datetime
import hashlib

class IdGenerator:
    def __init__(self,):
        '''Essa classe serve como uma forma de geração dos ids dos usuários, 
        e não necessita ser avaliada pelos candidatos.'''
        return None
    def generate(self,):
        output_id = ''
        for i in range(10):output_id += str(randint(0,9))
        return output_id

id_generator = IdGenerator()

class Contrato:

    def __init__(self, title, end_period, description = '',associates=''):
        """Essa classe é responsável por inicializar uma instância 
        de um Contrato, dado um certo título (Nome do Projeto), data de termino, descrição, consultor e cliente."""
        ### INICIALIZA A CLASSE DOS CONTRATOS DO SISTEMA
        self.title = int(title) 
        self.associates = associates 
        self.description = descript
        self.id = f'C{id_generator.generate()}' #Este C indica que é um Contrato
        self.created_dt = f'{datetime.datetime.now()}'
        self.end_period = end_period
        self.concluded = 0
        return None

    @staticmethod
    def __review__(self,):
        print("Status:",'\n')
        print("Title:",str(title))
        for i in self.associates: 
            ###Ao efetuar essa operação, o código não mostra os associados do contrato, mas não sei o motivo.
            print("Associates:",i)
        print('\n',self.description)
        print('Concluded':self.concluded)
        return None
    
    def conclude_contract(self): 
        if self.concluded:
            print("Contrato já concluído")
            return None
        self.concluded = 1
        print("Contrato Concluído!")
        return None
    
    def terminate_contract(self):
        inp = input("Você realmente pretende terminar este contrato?",
        '\n (s)Sim',
        '\n (n)Não')
        if inp.lower() == 'S':
            return 1
        else:
            return 0

class User:

    def init(self,username,password):
        '''Essa classe serve como um modelo base para a interação tanto para os Consultores quanto para os Clientes que
        utilizaram o terminal.'''
        self.username = username
        self.password = password
        self.status = 'Blank_User'
        self.id = f'U{id_generator.generate()}' #Este U indica que é um Usuário não definido
        return None
    
    def view(self,user_try,pass_try):
        if self.username == user_try and self.password==pass_try:
            print("Username:",self.username)
            print("Status:", self.status)
            print("Id:", self.id)
            return None
        print("Error, invalid user")

class Consultor(User):
    def __init__(self,username,password):
        super.__init__(username,password)
        self.status = 'Consultant'
        self.id = f'C{id_generator.generate()}' #Este C indica que é um Consultor
        self.projects = []
        return None

class Cliente:
    def __init__(self,username,password):
        super().__init__(username,password)
        self.status = 'Client'
        self.id = f'C{id_generator.generate()}' #Este C indica que é um Cliente
        self.contracts = []
        return None
