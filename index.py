import os

operacoes = [
    {'name': 'Soma', 'func': lambda x, y: x + y, 'char': '+'},
    {'name': 'Subtração', 'func': lambda x, y: x-y, 'char': '-'},
    {'name': 'Multiplicação', 'func': lambda x, y: x*y, 'char': '*'},
    {'name': 'Divisão', 'func': lambda x, y: x/y, 'char': '/'},
    {'name': 'Exponenciação', 'func': lambda x, y: x ** y, 'char': '^'},
]


execute = 1


while execute == 1:
    os.system('clear')
    index = 0
    print('\n\n## CALCULADORA ##\n\n')
    for item in operacoes:
        print(f'{index} : {item["name"]}')
        index += 1

    operacao = int(input('\n\n\nEscolha a opeação que deseja realizar: '))

    print(f'\n>>>  {operacoes[operacao]["name"]}: ')

    num1 = float(input('Qual o primeiro valor ? '))
    num2 = float(input('Qual o segundo valor ? '))

    result = operacoes[operacao]['func'](num1, num2)

    print(
        f'\n\n{num1:.1f} {operacoes[operacao]["char"]} {num2:.1f} = {result:.1f}\n\n'
    )

    execute = int(input('Deseja fazer outra operação? \n 1 - SIM, 0 - NÃO'))

os.system('clear')
print('\n\n\n########## VOCE ESCOLHEU SAIR !!!!!!! ##########\n\n\n\n\n')
