from random import randint
from time import sleep
print('==' * 30)
print('               JOGO DE ADIVINHAÇÃO           ')
print('==' * 30)
computador = int(input('Vou pensar em um número entre 0 e 5 tente adivinha: '))
escolha = randint(0, 5)
print('Espere um segundo...')
sleep(1)
print('Estou pensado...')
sleep(1)

if computador == escolha:
  jogo = 'GANHOU PARABÉNS'
else:
  jogo = 'PERDEU'
print(f'eu pensei no número {escolha} voçê {jogo}!!!!!')
