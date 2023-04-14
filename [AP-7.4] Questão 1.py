from biblioteca import*
def notasAlunos(g, m):
    n = []
    for i in range(0, len(m)):
        s = 0
        for t in range(0,len(m[i])):
            if g[t] == m[i][t]:
                s += 1
        s = round((s * 10)/len(g), 1)
        n.append(s)
    return n

print('Notas de BCC701')
g = inputVetor('Digite o gabarito:\n>>> ', str)
m = inputMatriz('Digite as respostas dos alunos:\n>>> ', str)
if len(m) == 0:
    print('Nenhum aluno para avaliar')
elif len(g) != len(m[0]):
    print('Quantidade de questões incompatível')
else:
    n = notasAlunos(g, m)
    print(f'Notas dos alunos: \n{n}')
    