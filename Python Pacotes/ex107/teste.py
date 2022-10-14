import moeda

p = float(input('Preço: R$'))
t = float(input('Taxa de desconconto: '))
print(f'A metade de R${p:.2f} é R${moeda.metade(p):.2f}')
print(f'O dobro de R${p:.2f} é R${moeda.dobro(p):.2f}')
print(f'O aumento de {t}% em cima do valor de R${p:.2f} é de R${moeda.aumentar(p, t):.2f}')
print(f'O desconto de {t}% em cima do valor de R${p:.2f} é de R${moeda.diminuir(p, t):.2f}')