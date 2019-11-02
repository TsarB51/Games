import os
from time import sleep
print('===> *Historia Python* <===')
print('''Precione <1> para INICIAR!:
Precione <2> para INFORMAÇÕES!: ''')
iniciar = int(input('Escolha: '))
os.system('cls')

if iniciar == 1:
    nome_player = str(input('Seu nome: '))
    print('''A historia inicia em 1xxx, você
é um fazendeiro muito humilde, que tem sua
fazenda bem pequena.''')
    sleep(3)

    print('''Um dia você foi para a cidade comprar
algumas coisas.''')
    sleep(3)

    print('''Mas quando você estava comprando a cidade
é atacada por piratas.''')

    print('''<1> Correr para uma casa aleatoria.
<2> Correr para o palacio.
<3> Roubar o que você estava comprando.''')
    inicio_ataque = int(input('Escolha: '))
    if inicio_ataque == 1:
        print('test')
    os.system('pause')
    
else:
    os.system('pause')
