#ex021
#nao funcionou
'''import pygame
pygame.init()
pygame.mixer.music.load('lets groove tonight.mp3')
pygame.mixer.music.play()
pygame.event.wait()'''



#ex020
'''from random import shuffle
a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')
lista = [a1, a2, a3, a4]
shuffle(lista)
print('A ordem de apresentação será: ')
print(lista)'''



#ex019
'''from random import choice
a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')
lista = [a1, a2, a3, a4]
print('O aluno sorteado foi o(a) {}.'.format(choice(lista)))'''



#ex018
'''import math
angulo = float(input('Digite o ângulo que você deseja: '))
seno =  math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('O ângulo de {:.2f} tem o SENO de {:.2f}'.format(angulo, seno))
print('O ângulo de {:.2f} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
print('O ângulo de {:.2f} tem a TANGENTE de {:.2f}'.format(angulo, tangente))'''



#ex017
'''from math import hypot
op = float(input('Cateto oposto: '))
adj = float(input('Cateto adjacente: '))
print('O comprimento da hipotenusa de um triangulo retangulo é {:.2f}.'.format(hypot(op, adj)))'''

#ex016
'''import math
n = float(input('Digite um um numero real: '))
print('O numero fracionario é {} e o seu número inteiro é {:.0f}.'.format(n, math.floor(n)))'''