from biblioteca import*

m = inputMatriz('Digite os elementos da matriz: ', int)
l, c = dimMatriz(m)
print()
if l != c:
    print('A matriz não é quadrada.')
else:
    print('Elementos da dioagonal principal:')
    d = []
    for i in range(0,l):
        d.append(m[i][i])
    print(d[0], end='')
    for i in range(1, len(d)):
        print(f', {d[i]}', end='')
    