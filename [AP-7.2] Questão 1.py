from biblioteca import*
def calculaLucros(vc, vq, lc, lq):
    l = []
    for i in range(0, len(vc)):
        l.append(round((vc[i]*lc)+(vq[i]*lq), 2))
    return l

vc = inputVetor('Vendas de coxinhas: ', int)
vq = inputVetor('Vendas de quibes: ', int)
if len(vc)!=len(vq):
    print('Dados de vendas inválidos')
else:
    lc = float(input('Lucro por unidade de coxinha: R$ '))
    lq = float(input('Lucro por unidade de quibe: R$ '))
    l = calculaLucros(vc, vq, lc, lq)
    print(f'Lucros: {l}')
    mx = l[0]
    mi = l[0]
    for i in range(0,len(l)):
        if l[i] > mx:
            mx = round(l[i], 2)
        if l[i] < mi:
            mi = round(l[i], 2)
    print(f'Maior lucro: R$ {mx:.2f}')
    print(f'Menor lucro: R$ {mi:.2f}')