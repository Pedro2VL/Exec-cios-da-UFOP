nome = input('Informe o nome do juiz: ')
n = int(input('Quantidade de partidas: '))
print('')
si = 0
sf = 0
sc = 0
st = 0
for i in range(1, n + 1):
    print(f'Partida {i}: ')
    m = int(input('. Impedimentos.......: '))
    f = int(input('. Faltas.............: '))
    c = int(input('. Cartões............: '))
    t = float(input('. Tempo de acréscimo.: '))
    si = si + m
    sf = sf + f
    sc = sc + c
    st = st + t
    print('')
print(f'Estatística do juiz {nome}:')
print(f'. Impedimentos.......: {round(si/n, 2):.2f}.')
print(f'. Faltas.............: {round(sf/n, 2):.2f}.')
print(f'. Cartões............: {round(sc/n, 2):.2f}.')
print(f'. Tempo de acrescimo.: {round(st/n, 2):.2f}.')