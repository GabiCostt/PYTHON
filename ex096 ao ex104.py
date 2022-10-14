#ex104 -- VALIDANDO ENTRADA DE DADOS EM PYTHON --
'''def LeiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('ERRO! DADOS INVALIDOS!')
        if ok:
            break
    return valor

n = LeiaInt('Digite um número: ')
print(f'Você acabou de digitas número {n}')'''





#ex102 -- FUNÇÃO PARA FATORIAL -- 
'''def fatorial(n, show=False):
    f = 1
    for c in range(n, 0, -1):
        if show == True:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='') 
        f *= c
    return f    
print(fatorial(5, show=False))'''





#ex101 -- FUNÇÕES PARA VOTAÇÃO --
'''def voto(nasc):
    from datetime import date
    ano = date.today().year
    idade = ano - nasc
    if idade < 16:
        return f'Você tem {idade} anos de idade: Não vota.'
    elif idade < 18 or idade >= 60:
        return f'Você tem {idade} anos de idade: Voto Opicional.'
    else:
        return f'Você tem {idade} anos de idade: Voto Obrigatorio.'
nasc = int(input('Ano de nascimento: '))
print(voto(nasc))'''





#ex100 -- FUNÇÕES PARA SORTEAR E SOMAR -- 
'''from random import randint

def sorteio(lista):
    print('-='*30)
    print('Os valores sorteados foram: ', end='')
    for c in range(0, 5):
        n = randint(0, 10)
        lista.append(n)
    for n in lista:
        print(n, end='  ')
    print()
    print('-='*30)
    

def somaPar(lista):
    soma = 0
    print('-='*30)
    print('A soma dos número pares é: ', end='')
    for n in lista:
        if n % 2 == 0:
            soma += n
    print(soma, end=' ')



numeros = list()
sorteio(numeros)
somaPar(numeros)'''





#ex099 -- FUNÇÃO QUE DESCOBRE O MAIOR -- 
'''def maior(* num):
    maior = 0
    print(f'Analizando os {len(num)} valores passados que são: ', end='')
    for n in num:
        print(n, end=' ')
        if maior == 0:
            maior = n
        else:
            if n > maior:
                maior = n
    print(f'\nO maior valor digitado é o {maior}')
    print('-='*30)




maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()'''





#ex098 -- FUNÇÃO DE CONTADOR -- == USANDO FLUSH == 
'''from time import sleep
def cont():
    print('-='*30)
    print('Contando de 1 a 10 de 1 em 1.')
    for c in range(1, 11):
        print(c, end=' ', flush=True)
        sleep(0.5)
    print()
        
def cont2():
    print('-='*30)
    print('Contando de 10 a 0 de 2 em 2.')
    for c in range(10, -1, -2):
        print(c, end=' ', flush=True)
        sleep(0.5)
    print()

def pers():
    print('-='*30)
    inicio = int(input('Inicio: '))
    fim = int(input('Fim: '))
    passo = int(input('Passo: '))

    print(f'Contando de {inicio} ao {fim} de {passo} em {passo}')
    if inicio < fim:
        for c in range(inicio, fim+1, passo):
            print(c, end=' ')
    elif inicio > fim:
        for c in range(inicio, fim-1, -passo):
            print(c, end=' ')


    
cont()
cont2()
pers()'''






#ex097 -- UM PRINT ESPECIAL -- 
'''def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)

escreva('eae gabriel, blz')
escreva('coe')
escreva('oieeeee')'''





#ex096 -- FUNÇÃO QUE CALCULA ÁREA --
'''def area():
    largura = float(input('Largura(m): '))
    comprimento = float(input('Comprimento(m): '))
    print(f'A área de {largura}x{comprimento} é {largura * comprimento}m²')

print('-='*30)
area()'''

