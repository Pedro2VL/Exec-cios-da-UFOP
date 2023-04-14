from biblioteca import*
def estatNotas(v):
    vm = v[0]
    vi = v[0]
    s = v[0]
    for i in range(1, len(v)):
        s += v[i]
        if v[i] > vm:
            vm = v[i]
        if v[i] < vi:
            vi = v[i]
    return round(vm, 1), round(vi, 1), round(s/len(v), 1)
        
v = inputVetor('Notas: ', float)
vm, vi, s = estatNotas(v)
print(f'Maior nota: {vm}')
print(f'Menor nota: {vi}')
print(f'Nota média: {s}')