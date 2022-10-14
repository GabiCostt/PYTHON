#ex114 -- SITE ESTA ACESSIVEL --
'''import urllib
import urllib.request

# Tenta abrir um site, se falhar, dara um print "O site não esta acessivel", se for bem sucedido, 
# dara um print "O site esta acessivel".
try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('O site não esta acessivel')
else:
    print('O site esta acessivel')'''




#ex113 -- FUNÇÕES APROFUNDADAS EM PYTHON  --
'''def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('Error: Valor invalido, tente novamente.')
            continue
        except KeyboardInterrupt:
            print('O usuario preferiu não informar este número.')
        else:
            return n 

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('Error: Valor invalido, tente novamente.')
            continue
        else:
            return n

numI = leiaInt('Digite um número Inteiro: ')
print(f'O número inteiro digitado foi {numI}')
print('-'*40)
numR = leiaFloat('Digite um número Real: ')
print(f'O número Real digitado foi {numR}')'''
