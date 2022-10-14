import moeda

p = float(input('Preço: R$'))
t = float(input('Taxa de desconconto: '))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'O aumento de {t}% em cima do valor de {moeda.moeda(p)} é de {moeda.moeda(moeda.aumentar(p, t))}')
print(f'O desconto de {t}% em cima do valor de {moeda.moeda(p)} é de {moeda.moeda(moeda.diminuir(p, t))}')
