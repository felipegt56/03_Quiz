print('''
Q1 - No python, como se chama uma 'caixa' usada  para armazenar dados?
a - texto
b - variavel
c - uma caixa de sapato
''')
resposta = input().lower()

if resposta == 'a':
  print('Não - Texto e um tipo de dado :( ')
elif resposta == 'b':
  print('Correto!! :) ')
elif resposta == 'c':
  print('Não seja bobinho! :( ')
else:
  print('Voçê não escolheu a, b ou c! :(')
