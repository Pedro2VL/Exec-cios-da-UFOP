from biblioteca import*

m = inputMatriz('Digite os elementos da matriz: ', int)
l, c = dimMatriz(m)
if l != c:
        print('A matriz não é identidade.')
else:
    v = []
    for i in range(0, l):
        j = []
        for t in range(0, c):
            if i==t:
                j.append(1)
            else:
                j.append(0)
        v.append(j)
    print()
    if m == v:
        print('A matriz é identidade.')
    else:
        print('A matriz não é identidade.')