from biblioteca import*
def contabilizarDemandas(v):
    q = [0,0,0,0]
    for i in range(0, len(v)):
        if v[i] >= 85:
            q[0] = q[0] + 1
        elif v[i] < 85 and v[i] >= 65:
            q[1] = q[1] + 1
        elif v[i] < 65 and v[i] >= 45:
            q[2] = q[2] + 1
        elif v[i] < 45 and v[i] >= 18:
            q[3] = q[3] + 1
    return q   
def avaliaAtendimento(c, vc):
    s = 0
    for i in range (0, len(c)):
        if c[i] <= vc[i]:
            s += 1
    if s == 4:
        return True
    else:
        return False
        
        
v = inputVetor('Defina as idades dos habitantes: ', int)
print('Demandas a serem atendidas por faixa etária: ')
q = contabilizarDemandas(v)
print(f'. >= 85.........: {q[0]}')
print(f'. < 85 e >= 65.: {q[1]}')
print(f'. < 65 e >= 45.: {q[2]}')
print(f'. >= 18.........: {q[3]}')
vc = inputVetor('Defina as disponibilidades de vacinas: ', int)
vf = avaliaAtendimento(q, vc)
if vf == True:
    print('A quantidade de vacinas é suficiente.')
else:
    print('Infelizmente, precisaremos de mais vacinas.')