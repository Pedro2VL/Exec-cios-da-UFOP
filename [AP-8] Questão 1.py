def calculaComprimento(x):
    c = ((x["B"]["X"] - x["A"]["X"]) ** 2 + (x["B"]["Y"] - x["A"]["Y"]) ** 2) ** 0.5
    r = round(c,2)
    return r

x = []
n = int(input('Informe a quantidade de retas: '))
for i in range(n):
    print(f'Reta {i+1}:')
    xa = float(input('- Coordenada X de A: '))
    ya = float(input('- Coordenada Y de A: '))
    xb = float(input('- Coordenada X de B: ')) 
    yb = float(input('- Coordenada Y de B: '))
    a = {"X": xa,"Y": ya}
    b = {"X": xb,"Y": yb}
    reta={"A":a, "B":b}
    x.append(reta)

print('Medidas das retas:')
for l in range(len(x)):
    r = calculaComprimento(x[l])
    print(f'- Reta {l + 1}: {r:.2f}')