#ex035
'''print('\33[33m-=-\33[m' * 20)
print('Analizador de Triângulos')
print('\33[33m-=-\33[m' * 20)

s1 = float(input('Primeiro Seguimento: '))
s2 = float(input('Segundo Seguimento: '))
s3 = float(input('Terceiro Seguimento: '))

if s1 < s2 + s3 and s2 < s1 + s3 and s3 <s1 + s2:
    print('Os seguimentos acima PODEM FORMAR um trinângulo.')
else:
    print('Os seguimentos acima NÃO PODEM FORMAR um triângulo.')'''





#ex034
'''salario = float(input('Qual o salario?: R$'))

if salario <= 1250:
    novo = salario + (salario * 0.15)
else:
    novo = salario + (salario * 0.1)

print('O salario que era de R${:.2f}, agora passa a ser de R${:.2f}'.format(salario, novo))'''




#ex033
'''a = int(input('Primeiro Valor: '))
b = int(input('Segundo Valor: '))
c = int(input('Terceiro Valor: '))

if a < b and a < c:
    menor = a
if b < a and b < c:
    menor = b
if c < b and c < a:
    menor = c

if a > b and a > c:
    maior = a
if b > a and b > c:
    maior = b
if c > a and c >b:
    maior = c

print('O MAIOR valor é {}'.format(maior))
print('O menor valor é {}'.format(menor))'''






#032
'''from datetime import date
ano = int(input('Que ano quer analizar? Digite 0 para analizar o ano atual: '))

if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO.'.format(ano))
else:
    print('O ano {} não é BISSEXTO.'.format(ano))'''





#ex031
'''n = int(input('Qual a distancia da viagem?: '))

if n <= 200:
    preco = 0.50 * n
else:
    preco = 0.45 * n

print('O preço da sua passagem custará R${:.2f}'.format(preco))'''






#ex030
'''n = int(input('Digite um número: '))
resultado = n % 2

if (resultado == 0):
    print('O número {} é PAR.'.format(n))
else:
    print('O número {} é IMPAR.'.format(n))'''






#ex029
'''n  = int(input('Qual a velocidade atual do carro?: '))
preco = n - 80

if (n <= 80):
    print('Tenha um bom dia! Dirija com segurança.')
else:
    print('VOCÊ FOI MULTADO. VOCÊ EXCEDEU O LIMITE PERMITIDO QUE É DE 80KM/H.')
    print('Você terá que pagar R$7,00 por cada km/h excedido. Sendo assim você terá que pagar R${:.2f}'.format(preco * 7))'''





#ex028
'''from random import randint
from time import sleep
computador = randint(0, 5)
print('-=-' * 20)
print('Estou pensando em um numero de 0 a 5, tente adivinhar!')
print('-=-' * 20)
jogador = int(input('Em qual numero eu estou pensando?: '))
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('Parabens, você ganhou!!!!')
else: 
    print('GANHEI! Eu pensei no número {} e não no número {}.'.format(computador, jogador))'''