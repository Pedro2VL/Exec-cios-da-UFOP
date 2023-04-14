print('Caixa aberto!\n')
s = 0
st = 0
sn = ''
qp = 0
while (sn != 'sim'):
    s = 0
    q = int(input('Quantidade de itens do pedido: '))
    for i in range(1, q + 1):
        p = float(input(f'. Preço do item {i}: '))
        s = s + p
        st = st + p
    d = input('. Cobrar delivery? ')
    if d == 'sim':
        s = s + 15
        st = st + 15
    print(f'. Valor do pedido: R$ {s:.2f}.')
    sn = input('Fechar o caixa? ')
    qp = qp + 1
    print()
print('Caixa fechado!')
print(f'Número de pedidos: {qp}.')
print(f'Valor total vendido: R$ {st:.2f}.')

    