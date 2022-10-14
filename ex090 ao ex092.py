#ex092 -- CADASTRO DE TRABALHADOR EM PYTHON --
'''from datetime import date
ano = date.today().year
inf = dict()

inf['Nome'] = str(input('Nome: ')).strip().lower().capitalize()
inf['Idade'] = ano - int(input('Ano de Nascimento: '))
inf['Ctps'] = int(input('Carteira de Trabalho [Digite 0 se não tiver]: '))
if inf['Ctps'] == 0:
    inf['Ctps'] = 'não tem'
else:
    inf['Contratação'] = int(input('Ano de Contratação: '))
    inf['Salário'] = float(input('Salário: '))
    inf['Aposentadoria'] = inf['Idade'] + ((inf['Contratação'] + 35) - ano)

print('-=' * 30)
for k, v in inf.items():
    print(f'  - {k} tem o valor: {v}')'''




#ex091 -- JOGO DE DADOS EM PYTHON --
'''from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1, 6), 'jogador2': randint(1, 6), 'jogador3': randint(1, 6), 
'jogador4': randint(1, 6)}
ranking = list()

print('Valores sorteados:')
for k, v in jogo.items():
    print(f'O {k} tirou {v} no dado')
    sleep(0.8)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-='*30)
print('  == RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'    {i+1}º lugar: {v[0]} com {v[1]}')'''




#ex090 -- DICIONARIO EM PYTHON  --
'''aluno = {}

aluno['nome'] = str(input('Nome: ')).strip().lower().capitalize()
aluno['media'] = float(input('Media da nota: '))

if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'
elif aluno['media'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'

for k, v in aluno.items():
    print(f'O(a) {k} é igual: {v}.')'''
