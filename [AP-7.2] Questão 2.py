from biblioteca import*
def comparaVetores(an, at):
    c = []
    for i in range(0, len(an)):
        if an[i] == at[i]:
            c.append('E')
        elif an[i] < at[i]:
            c.append('A')
        else:
            c.append('R')
    return c
def classificaEstado(c):
    r = 0
    a = 0
    e = 0
    for i in range(0, len(c)):
        if c[i] == 'R':
            r += 1
        elif c[i] == 'A':
            a += 1
        elif c[i] =='E':
            e += 1
    if r < a:
        return 'Classificação do estado: Onda Vermelha'
    elif r > a:
        return 'Classificação do estado: Onda Verde'
    else:
        return 'Classificação do estado: Onda Amarela'

an = inputVetor('Número de mortes na semana anterior: ', int)
at = inputVetor('Número de mortes na semana atual: ', int)
if len(an) != len(at):
    print(f'Número de elementos incompatível ({len(an)} != {len(at)})')
else:
    c = comparaVetores(an, at)
    print('Classificações das macro-regiões:')
    print(c)
    r = 0
    a = 0
    e = 0
    onde = classificaEstado(c)
    print(onde)