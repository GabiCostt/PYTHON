#ex056
'''somaidade = 0
mediaidade = 0
idademaior = 0
nomemaior = 0
idademenor = 0


for p in range(1,5):
    print('-----{}ª Pessoa-----'.format(p))
    nome = str(input('Nome: ')).strip().lower().capitalize()
    idade = int(input('Idade: '))
    sexo = str(input('Gênero [M/F]: ')).strip().upper()
    mediaidade += idade / 4

    if sexo == 'M' and idade > idademaior:
        idademaior = idade
        nomemaior = nome

    if sexo == 'F' and idade < 20:
        idademenor += 1


print('A media de idade do grupo é de {:.0f} anos.'.format(mediaidade))

if idademaior > 0:
    print('O homem mais velho do grupo é o {} e ele tem {:.0f} anos de idade.'.format(nomemaior, idademaior))
else:
    print('Não há nenhum homem no grupo.')

if idademenor > 0:
    print('Há {:.0f} mulhere(s) no grupo com menos de 20 anos.'.format(idademenor))
else:
    print('Não há mulher no grupo.')

print('===== FIM =====')'''




#ex055
'''maiorp = 0
menorp = 0

for c in range(1,6):
    peso = float(input('Peso da {}ª pessoa(Kg): '.format(c)))

    if c == 1:
        maiorp = peso
        menorp = peso
    else:
        if peso > maiorp:
            maiorp = peso
        
        if peso < menorp:
            menorp = peso

print('O maior peso lido foi de {}Kg.'.format(maiorp))
print('O menor peso lido foi de {}Kg.'.format(menorp))'''





#ex054
'''from datetime import date
atual = date.today().year
M = 0
m = 0

print('Ano de nascimento da:')
for c in range(1,8):
    nasc = int(input('{}ª pessoa: '.format(c)))
    idade = atual - nasc
    if idade < 18:
        m += 1
    else:
        M += 1

print('{} pessoas são menores de idade. \n{} pessoas são MAIORES de idade.'.format(m, M))'''




#ex052
'''n = int(input('Digite um número: '))
total = 0

for c in range(1, n+1):
    if n % c == 0:
        print('\33[33m', end=' ')
        total += 1
    else:
        print('\33[31m', end=' ')

    print(c, end='  ')


if total == 2:
    print('\n\33[mO número {} É PRIMO.'.format(n))
else:
    print('\n\33[mO número {} NÃO É PRIMO.'.format(n))

print('\33[mO número {} é dividido por {} números.'.format(n, total))'''






#ex051
'''t = int(input('Digite o Primerio Termo: '))
r = int(input('Digite a Razão: '))
decimo = t + (10 - 1) * r

for c in range(t, decimo + r, r):
    print('{}'.format(c), end=' - ')

print('ACABOU')'''





#ex050
'''soma = 0

for c in range(1, 7):
    n = int(input('Digite o {}ª valor: '.format(c)))
    
    if n % 2 == 0:
        soma += n

print('A soma dos valores é {}.'.format(soma))'''



#ex049
'''n = int(input('Digite um número para ver sua tabuada: '))

for c in range(1, 11):
    print('{} x {:2} = {:2}'.format(n, c, n * c))'''




#ex048
'''soma = 0
cont = 0

for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        cont += 1

print('A soma de todos os {} valores é {}..'.format(cont, soma))'''




#ex047
'''for c in range(2, 51, 2):
    print(c)'''



#ex046
'''from time import sleep

for c in range(10, -1, -1):
    print(c)
    sleep(1)

print('BUM! BUM! POOW!')'''
