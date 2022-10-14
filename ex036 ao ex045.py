#ex045
#from random import randint
#itens = ('Pedra', 'Papel', 'Tesoura')
#computador = randint(0, 2)
 
#print('''[ 0 ] Pedra
#[ 1 ] Papel
#[ 2 ] Tesoura''')

#jogador = int(input('Escolha um Opção: '))

#print('O computador escolheu {}.'.format(itens[computador]))
#print('Você escolheu {}.'.format(itens[jogador]))

#if computador == 0:
#    if jogador == 0:
#        print('DEU EMPATE')
#    elif jogador == 1:
#        print('VOCÊ GANHOU')
#    elif jogador == 2:
#        print('VOCÊ PERDEU')
#    else:
#        print('OPÇÃO INVALIDA')
#elif computador == 1:
#    if jogador == 0:
#        print('VOCÊ PERDEU')
#    elif jogador == 1:
#        print('DEU EMPATE')
#    elif jogador == 2:
#        print('VOCÊ GANHOU')
#    else:
#        print('OPÇÃO INVALIDA')
#elif computador == 2:
#    if jogador == 0:
#        print('VOCÊ GANHOU')
#    elif jogador == 1:
#        print('VOCÊ PERDEU')
#    elif jogador == 2:
#        print('DEU EMPATE')
#    else:
#        print('OPÇÃO INVALIDA')






#ex044
#print('\33[33m-=\33[m' * 25)
#print('\33[33m                  Loja do Gabriel         \33[m')
#print('\33[33m-=\33[m' * 25)

#compra = float(input('Valor da compra: R$'))

#print('''[ 1 ] À Vista em Dinheiro/Cheque
#[ 2 ] À Vista no Cartão
#[ 3 ] 2x no Cartão
#[ 4 ] 3x ou mais no Cartão''')

#escolha = int(input('Escolha a opção que você gostaria de pagar: '))

#while escolha <= 0 or escolha > 4:
#    print('OPÇÃO ESCOLHIDA INVALIDA!')
#    escolha = int(input('Escolha a opção que você gostaria de pagar: '))
    
#if escolha == 1:
#    print('O valor da compra que erá de R${:.2f}, com 10% de desconto ficará no valor de R${:.2f}.'.format#(compra, compra - (compra * 0.10)))
#elif escolha == 2:
#    print('O valor da compra que erá de R${:.2f}, com 5% de desconto ficará no valor de R${:.2f}.'.format(compra, compra - (compra * 0.05)))
#elif escolha == 3:
#    print('O valor da compra que é de R${:.2f}, ficará 2x de R${:.2f} cada SEM JUROS.'.format(compra, compra / 2))
#elif escolha == 4:
#    parcelas = int(input('Vezes a ser parcelada (Limite de até 10x): '))
#    if parcelas > 0 and parcelas <= 10:
#        print('O Valor da compra que erá de R${:.2f} ficará {}x de R${:.2f} COM JUROS.'.format(compra, parcelas, #(compra + (compra * 0.20)) / parcelas))
#        print('Sua compra será de R${:.2f} no total.'.format(compra + (compra * 0.20)))
#    while parcelas <= 0 or parcelas > 10:
#        print('QUANTIDADE DE PARCELAS INVALIDA!')
#        parcelas = int(input('Vezes a ser parcelada (Limite de até 10x): '))
#        if parcelas > 0 and parcelas <= 10:
#            print('O Valor da compra que erá de R${:.2f} ficará {}x de R${:.2f} COM JUROS.'.format(compra, #parcelas, (compra + (compra * 0.20)) / parcelas))
#            print('Sua compra será de R${:.2f} no total.'.format(compra + (compra * 0.20)))

#print('\33[33m-=\33[m' * 25)
#print('\33[33m                  FIM DO PROGRAMA         \33[m')
#print('\33[33m-=\33[m' * 25)






#ex043
'''peso = float(input('Qual é o seu peso? (KG) '))
altura = int(input('Qual a sua altura? (CM) ')) / 100

if peso > 0 and altura > 0:
    imc = peso / (altura ** 2)
    if imc < 18.5:
        print('Você está ABAIXO DO PESO!')
    elif imc < 25:
        print('Você está com um PESO IDEAL.')
    elif imc < 30:
        print('Você está com SOBREPESO!')
    elif imc < 40:
        print('Você está com OBESIDADE!')
    elif imc >= 40:
        print('Você está com OBESIDAE MORBIDA!')

    print('\33[33mSeu imc é de {:.1f}\33[m'.format(imc))
else:
    print('DADOS INVALIDOS! VERIFIQUE-OS E TENTE NOVAMENTE!')'''





#ex042
'''print('\33[33m-=-\33[m' * 20)
print('Analizador de Triângulos')
print('\33[33m-=-\33[m' * 20)

s1 = float(input('Primeiro Seguimento: '))
s2 = float(input('Segundo Seguimento: '))
s3 = float(input('Terceiro Seguimento: '))

if s1 < s2 + s3 and s2 < s1 + s3 and s3 <s1 + s2:
    print('Os seguimentos acima PODEM FORMAR um trinângulo ', end='')
    if s1 == s2 == s3:
        print('EQUILÁTERO')
    elif s1 != s2 != s3 != s1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Os seguimentos acima NÃO PODEM FORMAR um triângulo.')'''







#ex041
'''from datetime import date
atual = date.today().year #2022
ano = int(input('Ano de nascimento: ')) #1921
idade = atual -  ano
datai = atual - 101 #2022 - 101 = 1921

if ano <= datai:
    print('DATA DIGITA INVALIDA!')
    print('Só é aceitada datas de {} para cima.'.format(datai + 1))


txt1 = 'Você tem {} anos de idade.'.format(idade)
if idade < 10:
    print(txt1)
    print('Você está classificado(a) com MIRIM.')
elif idade < 15:
    print(txt1)
    print('Você está classificado(a) como INFANTIL.')
elif idade < 20:
    print(txt1)
    print('Você está classificado(a) como JUNIOR.')
elif idade < 26:
    print(txt1)
    print('Você está classificado(a) como SÊNIOR.')
elif idade <= 100:
    print(txt1)
    print('Você está classificado(a) como MASTER.')'''

    




#ex040
'''n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2

print('Sua media foi de {:.1f}'.format(media))
if media < 5:
    print('VOCÊ FOI REPROVADO')
elif media >= 5 and media <= 6.9:
    print('VOCÊ FICOU DE RECUPERAÇÃO')
elif media >= 7:
    print('VOCÊ FOI APROVADO')
else:
    print('[ERRO] VERIQUEFIQUE OS DADOS E TENTE NOVAMENTE!')'''





#039 incompleto
'''from datetime import date
atual = date.today().year
nasc = int(input('Data de Nascimento: '))
idade = atual - nasc

print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))

if idade == 18:
    print('Você deve se alistar IMEDIATAMENTE!')
elif idade < 18:
    print('Ainda falta {} anos para você se alistar.'.format(18 - idade))
    saldo = 
    print('Seu alistameto será em {}.'.format(atual )
elif idade > 18:
    print('Já passaram {} anos para o alistamento.'.format(idade - 18))
    print('Seu alistameto foi em {}.'.format(atual - (18 - idade)))'''




#038
'''n1 = float(input('Primeiro número: '))
n2 = float(input('Segundo número: '))

if n1 > n2:
    print('O PRIMEIRO VALOR é o MAIOR')
elif n2 > n1:
    print('O SEGUNDO VALOR é o MAIOR')
elif n1 == n2:
    print('Os dois números são iguais.')'''






#037
'''n = int(input('Digite um número inteiro: '))
print('[ 1 ] Converter para BINARIO')
print('[ 2 ] Converter para OCTAL')
print('[ 3 ] Converter para HEXADECIMAL')
opcao = int(input('Digite sua opção: '))
if opcao == 1:
    print('A conversão de {} para BINARIO é {}.'.format(n, bin(n)[2:]))
elif opcao == 2:
    print('A conversão de {} para OCTAL é {}.'.format(n, oct(n)[2:]))
elif opcao == 3:
    print('A conversão de {} para HEXADECIMAL é {}.'.format(n, hex(n)[2:]))
else:
    print('OPÇÃO INVALIDA!')'''





#036
'''casa = float(input('Qual o valor da casa?: R$'))
salario = float(input('Qual o seu salario?: R$'))
anos = int(input('Quantas parcelas?: '))
prestacao = casa / (anos * 12)
salariopercent = salario * 0.30

print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}'.format(casa, anos, prestacao))
if prestacao <= salariopercent:
    print('O emprestimo pode ser CONCEDIDO!')
elif prestacao > salariopercent:
    print('O emprestimo NEGADO!')
else:
    print('DADOS INVALIDOS. VERIFIQUE-OS E TENTE NOVAMENTE.')'''