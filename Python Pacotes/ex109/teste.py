import moeda

p = float(input('Preço: R$'))
t = float(input('Taxa de desconconto: '))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'O aumento de {t}% em cima do valor de {moeda.moeda(p)} é de {moeda.aumentar(p, t, True)}')
print(f'O desconto de {t}% em cima do valor de {moeda.moeda(p)} é de {moeda.diminuir(p, t, True)}')
