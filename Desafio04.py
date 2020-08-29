from time import sleep
def len():
  print('=='*40)
len()
print('                          QUESTIONÁRIO SOBRE PYTHON')
len()
score = 0
print('''
Q-1 O que e Python?
a) Um conjunto de ferramentas de edição
b) Um jogo
c) Uma liguagem de programação
''')
questao1 = input().lower()
if questao1 == 'c':
  print('Resposta certa!')
  score += 1
else:
  print('Resposta Incorreta!.')

print('''
Q-2 Qual a outra tradução para o nome python?
a) Cobra
b) Pipa
c) código
''')
questao2 = input().lower()
if questao2 == 'a':
  print('Resposta certa!')
  score += 1
else:
  print('Resposta Incorreta!.')

print('''
Q-3 Qual comando eu uso para importa módulos em Python?
a) int
b) import
c) sqrt
''')
questao3 = input().lower()
if questao3 == 'b':
  print('Resposta certa!')
  score += 1
else:
  print('Resposta Incorreta!.')

print('''
Q-4 Qual exemplo é um valor boleano?
a) 2.0
b) 5
c TRUE / FALSE
''')
questao4 = input().lower()
if questao4 == 'c':
  print('Resposta certa!')
  score += 1
else:
  print('Resposta Incorreta!.')

print('''
Q-5 Qual a função para imprima algo na tela?
a) print
b) float
c)input
''')
questao5 = input().lower()
if questao5 == 'a':
  print('Resposta certa!')
  score += 1
else:
  print('Resposta Incorreta!.')
sleep(0.5)
len()
print('Calculando os pontos...')
sleep(0.5)
len()
sleep(1)
print(f'Sua pontuação foi de {score} pontos. ')
sleep(1)


if score == 5:
  print('Parabéns, continue assim!')
else:
  print('Estude mais da próxima vez!!')
