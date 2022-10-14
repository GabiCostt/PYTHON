nome = (input('Qual o seu nome? '))
idade = int(input('{}, qual a sua idade? '.format(nome)))
peso = float(input('{}, qual o seu peso? '.format(nome)))

print('Olá {}, você tem {} anos de idade e seu peso é de {}, correto?'.format(nome, idade, peso))