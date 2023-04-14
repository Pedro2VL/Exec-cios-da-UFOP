v = []
x = int(input('Quantidade de alunos: '))
y = int(input('Quantidade de disciplinas: '))
for i in range(x):
    print('')
    print(f'Dados do aluno {i + 1}: ')
    p = 0
    for j in range(y):
        print(f'- Dados da disciplina {j+1}: ')
        n = float(input('- Nota: '))
        f = int(input('- Frequência: '))
        if n > p:
            p = n
            o = f
    x = [p,o]
    v.append(x)
print('')
print('Dados das disciplinas com maiores notas:')
for l in range(len(v)):
    print(f'- Aluno {l+1}: nota = {v[l][0]:.1f}; frequência = {v[l][1]}')