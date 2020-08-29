print('''
Q1 - A expressão (2**3) + (3 * 2 *(100/1)) % 2 é igual a:
a - 8.0
b - 8
c - FALSE
''')

resposta = str(input()).lower()

if resposta == 'a':
  print('SIM - resposta correta, o número 8.0  e do tipo Ponto Flutuante. ')
elif resposta == 'b':
  print('ERRADO - A resposta teria que ser do tipo Flutuante e não inteiro.')
elif resposta == 'c':
  print('Estude mais, a resposta não e do tipo boleano.')
else:
  print('Opção invalida, escolhe entre a, b ou c.')
