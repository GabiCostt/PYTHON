#ex027
'''nome = str(input('Qual o seu nome completo?: ')).strip()
nome2 = nome.split()
print('Prazer em te conhecer {}!'.format(nome2[0]))
print('Seu primeiro nome é {}.'.format(nome2[0]))
print('Seu ultimo nome é {}.'.format(nome2[len(nome2) - 1]))'''






#ex026
'''frase = str(input('Digite uma frase: ')).strip()

print('A letra A aparece {} vezes na frase.'.format(frase.lower().count('a')))
print('A letra A aparece pela primeira vez na posição {}.'.format(frase.lower().find('a') + 1))
print('A letra A aparece pela ultima vez na posição {}.'.format(frase.lower().rfind('a') + 1))'''





#ex025
'''nome = str(input('Qual o seu nome completo?: ')).strip()
print('Seu nome tem Silva?: {}'.format('silva' in nome.lower()))'''




#ex024
'''cidade = str(input('Em qual cidade você nasceu?: ')).strip()
print(cidade[0:5].lower() == 'santo')'''





#ex023
'''num = int(input('Digite um numero inteiro: '))

print('Analizando o numero {}'.format(num))
print('Unidade: {}'.format(num // 1 % 10))
print('Dezena: {}'.format(num // 10 % 10))
print('Centena: {}'.format(num // 100 % 10))
print('Milhar: {}'.format(num // 1000 % 10))'''





#ex022
'''nome = str(input('Qual o seu nome?: ')).strip()

print('Analizando seu nome...')
print('Seu nome em MAIUSCULO é {}.'.format(nome.upper()))
print('Seu nome em minusculo é {}.'.format(nome.lower()))
print('Seu nome completo tem ao todo {} letras.'.format(len(nome) - nome.count(' ')))
print('seu primeiro nome tem {} letras.'.format(nome.find(' ')))'''