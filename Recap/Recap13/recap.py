import random
import string

class Conta:
    _contador_id = 0
  
    def __init__(self, titular:str = None, senha:str = None,):
        self.id = Conta._contador_id
        Conta._contador_id += 1
        self.__numero_conta =  ''.join(random.choices(string.ascii_letters + string.digits, k=5))
        self._saldo = 0.0
        self.titular = titular
        self.senha = senha

    def __str__(self):
        return f"A conta: {self.__numero_conta} tem o titular: {self.titular}"
    
    def sacar(self, valor:float):
        if valor <= self._saldo:
            self._saldo -= valor
            print(f"Voce sacou: {valor} da sua conta, agora voce tem: {self._saldo} de saldo restante")
      
        else:
            print(f"Voce nao tem saldo suficiente para sacar essa quantia")
        
    

    def depositar(self, valor:float):
        if valor > 0.0:
            self._saldo += valor
            print(f"Voce acaba de depositar {valor} na sua conta, agora voce tem {self._saldo} de saldo")
        else:
            print("Voce so pode depositar uma quantia que seja maior que zero")


    def get_numero_conta(self) -> str:
        print(self.__numero_conta)
        return self.__numero_conta

    def set_numero_conta(self, valor:str, senha:str):
        chances = 3
        while chances:
            try:
                if senha == self.senha:
                    if valor == self.__numero_conta:
                        print("Voce deve digitar um numero de conta diferente da sua atual.")
                        break
                    else:
                        self.__numero_conta = valor
                        print(f"Agora sua conta se indentifica com o numero {valor}")
                        break
                else:
                    chances -= 1
                    print(f"Voce digitou a senha errada, tente novamente, voce ainda tem {chances} chances restantes")
            except:
                print(f"Voce perdeu todas as tentativas tente novamente")
                break

    def consultar_saldo(self):
        print(f"Voce tem um total de: {self._saldo} de saldo na sua conta")


contas = []

def menu():
    while True:
        print("\n--- MENU Conta ---")
        print("1. Cadastrar Conta")
        print("2. Entrar na Conta")
        print("3. Adicionar livro a um autor")
        print("4. Listar livros de um autor")
        print("5. Remover livro de um autor")
        print("6. Sair")
        
        resposta = int(input("Escolha uma opcao: "))
        if resposta == '1':
            titular = str(input("Qual o nome do titular da conta? "))
            senha = str(input("Qual a senha da conta? "))
            existe = False
            for i in contas:
                if i.titular == titular:
                    print('Ja temos uma conta com esse titular')
                    existe = True
                    break
            if existe == False:
                x = Conta(titular, senha)
                contas.append(x)
                print(x)
        elif resposta == '2':
            num_conta = str(input("Digite o numero da sua conta: ")) 
            senha = str(input("Digite sua senha: "))
            conta = None
            for i in contas:
                if i.get_numero_conta() == num_conta:
                    conta = i
            
            acesso = False

            if conta != None:
                chances = 3
                while chances:
                    try:
                        if senha != conta.senha:
                            chances -=1
                            print(f"Voce digitou a senha errada, voce ainda tem {chances} chances")
                        else:
                            print(f"Voce liberou acesso a conta!")
                            acesso = True
                            break
        
                    except:
                        print("Voce nao tem mais chances")
                        break
            else:
                print("Essa conta nao existe")

            if acesso == True:
            
                while True:
                    print(f"\n--- MENU Conta {conta.titular} ---")
                    print("1. Sacar quantia")
                    print("6. Sair")
                    opcaoconta = int(input("Digite a opcao que deseja: "))
                    if opcaoconta == 1:
                        valor = float(input("Digite o valor que deseja sacar: "))
                        conta.sacar(valor)
                        break
                    else:
                        print("Digite somente alguma das opcoes acima")

