from biblioteca import*
def calculaConsumos(c, q):
    k = []
    for i in range(0, len(q)):
        p = []
        for t in range(0, len(q[i])):
            s = round(q[i][t]/c[t], 2)
            p.append(s)
        k.append(p)
    return k
def calculaMedias(k):
    v = []
    for i in range(0, len(k[0])):
        s = 0
        for t in range(0, len(k)):
            s = s + k[t][i]
        v.append(round(s/len(k), 2))
    return v

print('Teste de consumo')
c = inputVetor('Capacidade dos tanques: \n>>> ', int)
if len(c) == 0:
    print('É necessário pelo menos um automóvel')
else:
    q = inputMatriz('Quilometragens dos condutores:\n>>> ', int)
    if len(q) == 0:
        print('Deve haver pelo menos um condutor')
    elif len(c) != len(q[0]):
        print('Quantidade de automóveis incompatível')
    else:
        k = calculaConsumos(c, q)
        print(f'Consumos km/l: ')
        for i in range(0, len(k)):
            print(k[i])
        print('Medias dos consumos por automovél:')
        v = calculaMedias(k)
        print(v)
        
