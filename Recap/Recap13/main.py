import random
import string

'''
Crie um sistema de gerenciamento de contas bancárias com os seguintes requisitos:

- Crie uma classe abstrata chamada Conta.
- O método sacar deve ser abstrato.
- Crie as classes ContaCorrente e ContaPoupanca que herdam de Conta.
- Ambas devem implementar o método sacar de forma diferente:
    - ContaCorrente permite saque até um limite negativo (ex: -500).
    - ContaPoupanca não permite saldo negativo.
- O atributo saldo deve ser protegido.
- O atributo numero_conta deve ser fortemente privado e gerado automaticamente.
- Implemente métodos getter e setter para o atributo numero_conta.
- Implemente um método para depositar em ambas as contas.
- Crie um menu para:
    - Criar contas (corrente ou poupança)
    - Depositar
    - Sacar
    - Consultar saldo
    - Listar todas as contas

'''

class Conta:
    _contador_id = 0
  
    def __init__(self, titular:str = None, senha:str = None,):
        self.id = Conta._contador_id
        Conta._contador_id += 1
        self.__numero_conta = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))        
        self._saldo = 30.0
        self.titular = titular
        self.senha = senha

    def __str__(self):
        return f"A conta: {self.__numero_conta} tem o titular: {self.titular}"
    
    def sacar(self, valor:float):
        if valor > 0:
            self._saldo -= valor
            print(f"Voce sacou: {valor} da sua conta, agora voce tem: {self._saldo} de saldo restante")
        else:
            print("Voce nao pode sacar uma quantia menor que 0")
      
        
    

    def depositar(self, valor:float):
        if valor > 0.0:
            self._saldo += valor
            print(f"Voce acaba de depositar {valor} na sua conta, agora voce tem {self._saldo} de saldo")
        else:
            print("Voce so pode depositar uma quantia que seja maior que zero")


    def get_numero_conta(self) -> str:
        print(self.__numero_conta)
        return self.__numero_conta

    def set_numero_conta(self, valor:str):    
        if valor == self.__numero_conta:
            print("Voce deve digitar um numero de conta diferente da sua atual.")
        else:
            self.__numero_conta = valor
            print(f"Agora sua conta se indentifica com o numero {valor}")
      
    

    def consultar_saldo(self):
        print(f"Voce tem um total de: {self._saldo} de saldo na sua conta")


class ContaCorrente(Conta):
    def __init__(self, titular = None, senha = None):
        super().__init__(titular, senha)
        self.limite = -500

    def __str__(self):
        print('A conta é do tipo conta corrente')
        return super().__str__()
    
    def sacar(self, valor):
        x = self._saldo - valor
        if x >= self.limite:
            super().sacar(valor)
            print(f"E seu limite de saque é: {self.limite}, nao esqueca!")
        else:
            print("Voce ja chegou no seu limite de saldo!")
       

    def depositar(self, valor):
        return super().depositar(valor)
    
    def get_numero_conta(self):
        return super().get_numero_conta()
    
    def set_numero_conta(self, valor):
        return super().set_numero_conta(valor)
    
    def consultar_saldo(self):
        return super().consultar_saldo()
    
class ContaPoupanca(Conta):
    def __init__(self, titular = None, senha = None):
        super().__init__(titular, senha)

    def __str__(self):
        print('A conta é do tipo conta poupanca')
        super().__str__()

    def sacar(self, valor):
        if valor < self._saldo:
            x = self._saldo - valor
            print(f'Voce nao pode sacar esse valor, voce tem somente: {self._saldo} de saldo na conta')
        else:
            super().sacar(valor)
    
    def depositar(self, valor):
        return super().depositar(valor)
    
    def get_numero_conta(self):
        return super().get_numero_conta()
    
    def set_numero_conta(self, valor):
        return super().set_numero_conta(valor)
    
    def consultar_saldo(self):
        return super().consultar_saldo()
    
    







    
        



contas = []
contasCorrente = []
contasPoupanca = []

def menu():
    while True:
        print("\n--- MENU ---")
        print("1. Cadastrar Conta")
        print("2. Entrar na Conta")
        print("3. Exibir todas as Contas")
        print("6. Sair")
        
        resposta = int(input("Escolha uma opcao: "))
        if resposta == 1:

            print("1. Conta corrente")
            print("2. Conta poupanca")
            tipoconta = int(input('Qual o tipo de conta que voce deseja criar?'))

            if tipoconta == 1:
                titular = str(input("Qual o nome do titular da conta? "))
                senha = str(input("Qual a senha da conta? "))
                existe = False
                for i in contasCorrente:
                    if i.titular == titular:
                        print('Ja temos uma conta com esse titular')
                        existe = True
                        break
                if existe == False:
                    x = ContaCorrente(titular, senha)
                    contas.append(x)
                    contasCorrente.append(x)
                    print(x)

            elif tipoconta == 2:
                titular = str(input("Qual o nome do titular da conta? "))
                senha = str(input("Qual a senha da conta? "))
                existe = False
                for i in contasPoupanca:
                    if i.titular == titular:
                        print('Ja temos uma conta com esse titular')
                        existe = True
                        break
                if existe == False:
                    x = ContaPoupanca(titular, senha)
                    contas.append(x)
                    contasPoupanca.append(x)
                    print(x)
            else:
                print("Digite somente alguma das opcoes acima")


        elif resposta == 2:
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
                    print(f"\n--- MENU DE {conta.titular} ---")
                    print("1. Sacar quantia")
                    print("2. Depositar quantia")
                    print("3. Ver numero da conta")
                    print("4. Alterar numero da conta")
                    print("5. Verificar saldo")
                    print("6. Sair")
                    opcaoconta = int(input("Digite a opcao que deseja: "))
                    if opcaoconta == 1:
                        valor = float(input("Digite o valor que deseja sacar: "))
                        conta.sacar(valor)
                    elif opcaoconta == 2:
                        valor = float(input("Digite o valor que deseja depositar:"))
                        conta.depositar(valor)
                    elif opcaoconta == 3:
                        conta.get_numero_conta()
                    elif opcaoconta == 4:
                        x = conta.get_numero_conta()
                        print(f"O numero atual da sua conta é: {x}")
                        num_conta_novo = str(input("Digite o novo numero da sua conta: "))
                        existe = False
                        for i in contas:
                            if i.get_numero_conta() == num_conta_novo:
                                existe = True

                        if existe == False:
                            conta.set_numero_conta(num_conta_novo)
                    elif opcaoconta == 5:
                        conta.consultar_saldo()
                    elif opcaoconta == 6:
                        break
                    else:
                        print("Digite somente alguma das opcoes acima")

        elif resposta == 3:
            for i in contas:
                print("------------")
                print(i)
                print("------------")
        elif resposta == 6:
            break
        else:
            print("Digite somente alguma das opcoes acima")









if __name__ == "__main__":
    menu()

