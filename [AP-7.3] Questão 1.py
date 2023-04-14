from biblioteca import*

m = inputMatriz('Matriz de notas: ', float)
ni = m[0][0]
nm = m[0][0]
am = []
ai = []
print()
for i in range(0, len(m)):
    for t in range(0,len(m[i]) ):
        if m[i][t] < ni:
            ni = m[i][t]
        elif m[i][t] > nm:
            nm = m[i][t]
for i in range(0, len(m)):
    for t in range(0, len(m[i])):
        if m[i][t] == ni:
            ai.append(i)
        elif m[i][t] == nm:
            am.append(i)
print(f'Menor nota: {ni}')
print(f'Alunos com a menor nota:')
for i in range(0, len(ai)):
    print(f'. {ai[i]}')
print(f'')
print(f'Maior nora: {nm}')
print(f'Alunos com a maior nota:')
for i in range(0, len(am)):
    print(f'. {am[i]}')

