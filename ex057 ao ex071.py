#ex071 ESTUDAR NOVAMENTE, É IMPORTANTE E NAO APRENDI DIREITO
'''print('='*40)
print('{:^40}'.format('BANCO CEV'))
print('='*40)

valor = int(input('Quantidade a ser sacada: R$'))
total = valor
ced = 50
totced = 0

while True: #R$174
    if total >= ced:
        total -= ced
        totced += 1 
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break

print('Fim do programa')'''






#ex070 EXERCICIO IMPORTANTE!!!!
'''print('-------- LOJINHA --------')
total = 0
mais1000 = 0
menor = 0
cont = 0
barato = ' '
while True:
    nome = str(input('Nome do produto: ')).strip()
    preço = float(input('Valor do produto: R$'))
    if preço < 0:
        while preço < 0:
            preço = float(input('Valor do produto: R$'))
    cont += 1
    total += preço
    if preço >= 1000:
        mais1000 += 1

    if cont == 1 or preço < menor:
        menor = preço
        barato = nome



    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar [S/N]?: ')).strip().upper()[0]
    if continuar == 'N':
        break

print(f'O total de compra deu R${total}')
print(f'Tem {mais1000} produtos que custam mais de R$1.000,00')
print(f'O produto mais barato é o(a) {menor}')
print('{:-^40}'.format(' FIM DO PROGRAMA '))'''




#ex069
'''maior = 0
homens = 0
mulher20 = 0

while True:
    print('-'*30)
    idade = int(input('Qual sua Idade?: '))

    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual seu sexo [M/F]?: ')).strip().upper()[0]
    print('-'*30)

    if idade >= 18:
        maior += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulher20 += 1

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Você quer continuar [S/N]?: ')).strip().upper()[0]

    if continuar == 'N':
        break

print(f'Tem {maior} pessoas com mais de 18 anos de idade \nForam cadastrados {homens} homens \nTem {mulher20} mulher(es) com menos de 20 anos de idade.')
print('FIM DO PROGRAMA')'''





#ex068
'''from random import randint

while True:
    print('-'*30)
    computador = randint(0, 100)
    jogador = int(input('Escolha um número: '))
    total = computador + jogador
    pi = str(input('Escolha par ou ímpar [p/i]: ')).strip().upper()[0]
    if pi not in 'PI':
        while pi not in 'PI':
            pi = str(input('Escolha par ou ímpar [p/i]: ')).strip().upper()[0]

    print(f'O computador escolheu o número {computador}')
    if total % 2 == 0 and pi == 'P':
        print(f'A soma deu {total} e é um número PAR')
        print('Você Ganhou!')
    elif total % 2 != 0 and pi == 'I':
        print(f'A soma deu {total} e é um número ÍMPAR')
        print('Você Ganhou!')
    elif total % 2 != 0 and pi == 'P':
        print(f'A soma deu {total} e é um número ÍMPAR')
        print('Você Perdeu!')
        break
    elif total % 2 == 0 and pi == 'I':
        print(f'A soma deu {total} e é um número PAR')
        print('Você Perdeu!')
        break
    print('-'*30)'''





#ex067
'''while True:
    n = int(input('Qual número você quer ver na tabuada?: '))

    print('-'*30)

    if n < 0:
        print('FIM DO PROGRAMA')
        break

    for cont in range(1, 11):
        print(f'{n} x {cont:>2} = {cont * n}')
    print('-'*30)'''





#ex066
'''cont = 0
soma = 0
 
while True:
    num = int(input('Digite um valor [999 para parar]: '))
    if num == 999:
        break
    cont += 1
    soma += num

print(f'A soma dos {cont} valores foi {soma}')'''





#ex065
'''SN = ''
cont = 0
media = 0
maior = 0
menor = 999999999999

while SN != 'N':
    print('=' * 20)
    num = int(input('Digite um valor: '))
    SN = str(input('Quer continuar [S/N]?: ')).strip().upper()[0]
    if SN != 'S' and SN != 'N':
        while SN != 'S' and SN != 'N':
            SN = str(input('Dados invalidos! Quer continuar [S/N]?: ')).strip().upper()[0]
    cont += 1
    media += num
    if num > maior:
        maior = num
    if num < menor:
        menor = num

print('~'*30)
print('A media de todos os número é {:.1f}'.format(media / cont))
print('O maior numero é o {}'.format(maior))
print('O menor número é o {}'.format(menor))
print('~'*30)'''




#ex064
'''n = 0
s = 0
qn = 0

while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    s += n
    qn += 1

print('Você digitou {} números e a soma entre eles foi {}.'.format(qn - 1, s - 999))'''





#ex060
'''n = int(input('Digite um número para calcular seu fatorial: '))
c = n
f = 1

print('Fatorial: {}! = '.format(n), end='')

while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
    
print('{}'.format(f))'''






#059
'''from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))

print('===== O que você gostaria de fazer com esses valores? =====')
print('[ 1 ] Somar \n[ 2 ] Mutiplicar \n[ 3 ] O Maior \n[ 4 ] Novos números \n[ 5 ] Sair do programa')

escolha = str(input('>>> Sua escolha: '))

while escolha:
    if escolha == '1':
        print('>>> Resultado: {} + {} = {}'.format(n1, n2, n1+n2))
    elif escolha == '2':
        print('>>> Resultado: {} x {} = {}'.format(n1, n2, n1*n2))
    elif escolha == '3':
        if n1 > n2:
            print('>>> Resultado: O número de maior valor é o {}'.format(n1))
        elif n2 > n1:
            print('>>> Resultado: O número de maior valor é o {}'.format(n2))
        else:
            print('>>> Resultado: Não há número maior que o outro, pois ambos tem o mesmo valor.')
    elif escolha == '4':
        print('Informe os número novamente.')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif escolha == '5':
        print('Finalizando...')
        sleep(1.3)
        break
    else:
        print('Opção Invalida!')
    print('=-='*10)
    print('===== O que você gostaria de fazer com esses valores? =====')
    print('[ 1 ] Somar \n[ 2 ] Mutiplicar \n[ 3 ] O Maior \n[ 4 ] Novos números \n[ 5 ] Sair do programa')
    escolha = str(input('>>> Sua escolha: '))'''






#058
'''from random import randint
computador = randint(0,10)
tentativas = 0

print('Olá, eu sou o Computador!! \nEu pensei em um número de 0 a 10, \nTente adivinha-lo!')

jogador = int(input('Digite um número em que você acha que o Computador pensou: '))

while jogador != computador:
    if jogador < computador:
        print('HMM, você errou! Pensei em um número um pouco maior')
    if jogador > computador:
        print('HMM, você errou! Pensei em um número um pouco menor')
    jogador = int(input('Tente mais um outro número: '))
    tentativas += 1

if jogador == computador:
    print('AAAAEEEE! Você acertou, mas com {} tentativas.'.format(tentativas))'''





#ex057
'''sexo = str(input('Digite o seu sexo [M/F]: ')).strip().upper()[0]

while sexo not in 'MF':
    sexo = str(input('DADOS INVALIDOS! Por favor, insira seu sexo [M/F]: ')).strip().upper()

print('Sexo {} salvo com sucesso.'.format(sexo))'''