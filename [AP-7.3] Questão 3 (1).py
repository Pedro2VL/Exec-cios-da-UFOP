from biblioteca import*

m = inputMatriz('Digite os elementos da matriz: ', int)
l, p = dimMatriz(m)
print()
c = int(input('Digite a coluna que será alterada: '))
while c < 0 or c > (p - 1):
    c = int(input('Digite uma coluna válida: '))
print()
for i in range(0, len(m)):
    m[i][c] = m[i][c] * 2
print('Matriz alterada:')
for i in range(0, len(m)):
    for t in range(0, len(m[i])):
        if (i + 1) < len(m):
            if (t + 1) != len(m[i]):
                print(m[i][t], end = ', ')
            else:
                print(f'{m[i][t]}; ', end = '')
        elif (i + 1) == len(m):
            if (t + 1)  != len(m[i]):
                print(m[i][t], end = ', ')
            elif (t + 1) == len(m[i]):
                print(m[i][t])
            
        


