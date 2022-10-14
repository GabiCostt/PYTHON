def aumentar(preço = 0, taxa = 0, formato=False):
    res = preço + (preço * taxa/100)
    return res if not formato else moeda(res)  


def diminuir(preço = 0, taxa = 0, formato=False):
    res = preço - (preço * taxa/100)
    return res if not formato else moeda(res) 


def dobro(preço = 0, formato=False):
    res = preço * 2
    return res if not formato else moeda(res)


def metade(preço = 0, formato=False):
    res = preço / 2
    return res if not formato else moeda(res)


def moeda(preço = 0, moeda = 'R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')


def resumo(preço = 0, taxa=0):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço Analizado: {moeda(preço):>13}')
    print(f'Dobro: {dobro(preço, True):>23}')
    print(f'Metade: {metade(preço, True):>22}')
    print(f'Aumento: {aumentar(preço, taxa, True):>21}')
    print(f'Diminuição: {diminuir(preço, taxa, True):>18}')
    print('-'*30)
  