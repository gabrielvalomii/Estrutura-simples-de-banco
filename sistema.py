saldo = 1000
cont = 0
cadastro = [[], [], []]
Lnome =[]
Lsenha = []
Lemail = []

opção = str(input('não pussuo um cadastro[s/n]: '))
if opção == 's':
    nome = str(input('insira seu nome de usuario: '))
    senha = int(input('incira sua senha:'))
    if nome in Lnome and senha in Lsenha:
        print('login realizado com sucesso')
    else:
        print('usuario não registrado')
        
elif opção == 'n':
    print('faça seu cadastro agora')
    digitenome = str(input('digite seu nome: '))
    Lnome.append(digitenome)
    digitesenha = int(input('digite seu senha '))
    Lsenha.append(digitesenha)
    digiteemial = str(input('digite seu emial: '))
    Lemail.append(digiteemial)
    print('cadastro realizado com sucesso')
            
def inicio():
    print('-='*30)
    print('BEM VINDO AO SISTEMA MATRIX')
    print('-='*30)

def menu():
    print('[1]Digite 1 para ver saldo de sua conta: \n'
          '[2]digite 2 para sacar saldo: \n'
          '[3]digite 3 para desbloquear telefone: \n'
          '[4]digite 4 para sair: \n'
          '[5]depositar mais saldo.\n'
          '[6]simulaão de investimento \n'
          '[7]simulado de financimento')

inicio()
menu()

escolha = int(input('digite um numero de 1 a 7: '))
while True:
    if escolha == 1:
        print(f'seu saldo da conta é {saldo}')
    if escolha == 2:
        escolha2 = int(input('qual o valor que deseja sacar: '))
        if escolha2 >= saldo or escolha2 <= 0:
            print('saldo insuficiente por favor tente outra quantia!')
        elif escolha2 <= saldo:
            saldo = saldo - escolha2
            print(f'seu saldo atual e de {saldo}') 
    if escolha == 3:
        telefone = int(input('difite seu telefone: '))
        cadastro[0].append(3)
        print('telefone cadastrado com sucesso')
        print(cadastro)
    if escolha == 4:
        print('Até logo')
    if escolha == 5:
        deposito = int(input('digite o valor do deposito: '))
        if deposito > 0:
            saldo = saldo + deposito
            print(f'seu saldo agora e de {saldo}')
    if escolha == 6:
        print('este banco vai render apenas 0,5 do seu dinehiro')
        rendimento = saldo * 0.5
        saldo = saldo + rendimento
        print(f'seu novo saldo e de {saldo}')
        break
    if escolha == 7:
        financimento = int(input('qual o valor que vc deseja financiar: '))
        vezes = int(input('em quantas parcelas: '))
        juros = financimento * 0.1
        parcelas = juros / vezes
        print(f'seu financeamento sera de {juros} com o valor de {parcelas} por mes.')
        break 