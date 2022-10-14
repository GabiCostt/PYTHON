#ex086 -- MATRIZ EM PYTHON -- 
'''matriz = [[0, 0, 0], [0, 0, 0] , [0, 0, 0]]

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()'''




#ex085 -- LISTAS COM PARES E ÍMPARES --
'''par = list()
impar = list()

for c in range(1, 8):
    num = int(input(f'Digite o {c}ª Valor: '))
    if num % 2 == 0:
        if num not in par:
            par.append(num)
    else:
        if num not in impar:
            impar.append(num)

par.sort()
impar.sort()
print(f'Os número pares são: {par}')
print(f'Os número ímpares são: {impar}')
print('{:-^40}'.format('FIM DO PROGRAMA'))'''





#ex084 -- LISTA COMPOSTA E ANALISE DE DADOS --
'''temp = list()
princ = list()
maior = menor = 0
nmaior = ' '
nmenor = ' '

while True:
    print('-'*40)
    temp.append(str(input('Nome: ')).strip().capitalize())
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        maior = menor = temp[1]
        nmaior = nmenor = temp[0]
    else:
        if temp[1] > maior:
            maior = temp[1]
            nmaior = temp[0]
        if temp[1] < menor:
            menor = temp[1]
            nmenor = temp[0]
    princ.append(temp[:])
    temp.clear()
    print('-'*40)

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]

    if continuar in 'N':
        break

print('='*40)
print(f'A quantidade de pessoas cadastradas são: {len(princ)} pessoa(s).')
print(f'O maior peso foi de', end=' ')
for p in princ:
    if p[1] >= 100:
        print(p[0], end='... ')

print(f'\nO menor peso foi de', end=' ')
for p in princ:
    if p[1] < 100:
        print(p[0], end='... ')'''





#ex082 -- DIVIDINDO VALORES EM VÁRIAS LISTAS --
'''par = list()
impar = list()

while True:
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    
    continuar = str(input('Gostaria de continuar? [S/N]: ')).strip().upper()[0]
    if continuar in 'N':
        break

print(f'A lsta de números digitados é {par + impar}')
print(f'Os número pares digitados foram: {par}')
print(f'Os número ímpares digitados foram: {impar}')'''






#ex081 -- EXTRAINDO DADOS DE UMA LISTA --
'''lista = list()
while True:
    lista.append(int(input('Digite um valor: ')))

    continuar = str(input('Gostaria de continuar? [S/N]: ')).strip().upper()[0]
    if continuar in 'N':
        break

lista.sort(reverse=True)
print(f'Os valores em forma decrescente são: {lista}')
print(f'Foram digitados {len(lista)} valores!')
print('O número 5', end=' ')
if 5 not in lista:
    print('não foi digitado e não está na lista.')
else:
    print('foi digitado e está na lista.')'''






#ex080 -- LISTA ORDENADA SEM REPETIÇÕES --
'''lista = list()
for c in range(0, 5):
    n = int(input('Digie um valor: '))

    if c == 0 or n >= lista[-1]:
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            pos += 1

    
print('-'*30)
print(f'Os valores digitados e ordenados foram: {lista}')'''





#ex079 -- VALORES ÚNICOS EM UMA LISTA --
'''numeros = list()
while True:
    print('-'*30)
    n = int(input('Digite um valor: '))
    
    if n not in numeros:
        numeros.append(n)
    else:
        print('Valor duplicado! Não vou adicionar este número...')

    continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]

    if continuar in 'N':
        break

print(sorted(numeros))
print('Fim do Programa')'''





#ex078 -- MIOR E MENOR VALORES NA LISTA -- ^^ USANDO ENUMARATE ^^ 
'''valores = list()

for v in range(0, 5):
    valores.append(int(input(f'Dgite um valor na posição {v}: ')))

print(f'Os valores digitados foram: {valores}')

print(f'O maior valor digitado foi o número {max(valores)}')
print(f'E aparecem na(s) posição(ões): ', end='')
for i, v in enumerate(valores):
    if v == max(valores):
        print(i, end='... ')

print(f'\nO menor valor digitado foi o número: {min(valores)}')
print(f'E aparecem na(s) posição(ões): ', end='')
for i, v in enumerate(valores):
    if v == min(valores):
        print(i, end='... ')'''