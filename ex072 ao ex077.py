#ex077 -- CONTANDO VOGAIS EM TUPLAS --
'''palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')

for p in palavras:
    print(f'\nNa palvra {p.upper()} temos a(s) vogais: ', end='')
    for letras in p:
        if letras.lower() in 'aeiou':
            print(letras, end=' ')'''





#ex076 -- LISTA DE PREÇO COM TUPLAS --
'''listagem = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25, 'Transfiridor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Caneta', 1.50, 'livro', 34.90) 

print('-'*50)
print(f'{"LISTA DE PREÇOS":^50}')
print('-'*50)

for pos in range(len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<40}', end='')
    elif pos % 2 == 1:
        print(f'R${listagem[pos]:>7.2f}')

print('-'*50)'''






#ex075 -- ANÁLISE DE DADOS EM TUPLA --
'''num = (int(input('Digite um valor: ')), 
    int(input('Digite outro valor: ')), 
    int(input('Digite mais um valor: ')), 
    int(input('Digite o ultimo valor: ')))

print(f'Você digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O número 3 apareceu na {num.index(3)+1}ª posição')
else:
    print('O número 3 não aparceu em nenhuma posição')

print(f'Os valores pares que foram digitados foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')'''
        





#ex074 -- MAIOR E MENOR VALOR EM TUPLA --
'''from random import randint
num = (randint(1, 10)), (randint(1, 10)), (randint(1, 10)), (randint(1, 10)), (randint(1, 10))

cont = 1
print('Os valores sorteados foram: ', end=' ')
for n in num:
    print(f'{n}', end='')
    print(', ' if cont <= 3 else '', end='')
    print(' e ' if cont == 4 else '', end='')
    print('.' if cont == 5 else '', end='')
    cont += 1


print(f'\nO número de maior valor é o {max(num)}')
print(f'O número de menor valor é o {min(num)}')'''





#ex073 -- TUPLAS COM TIMES DE FUTEBOL --
'''times = ('Corinthias', 'Palmeiras', 'Santos', 'Gremio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense', 'Atletico', 'Botafogo', 'Atletico-PR', 'Bahia')

print(f'Os times do Brasileirão sao {times}')
print(f'Os cinco primeiros colocados são {times[0:5]}')
print(f'Os quatros ultimo colocados são {times[-4:]}')
print(f'A ordem alfabetica dos times é {sorted(times)}')
print(f'O time Chapecoense esta na {times.index("Chapecoense")+1}ª posição')'''






#ex072 -- NÚMERO POR EXTENSO --
'''cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', ' catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    while True:
        n = int(input('Digite um número de 0 à 20: '))
        if 0 <= n <= 20:
            break
        print('Dados Invalidos', end=' ')

    print(f'Você digito o número {cont[n]}')
    continuar = str(input('Você quer continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break'''