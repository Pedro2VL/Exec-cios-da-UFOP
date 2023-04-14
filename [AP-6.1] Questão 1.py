def avaliaTubo(ct, cd, m):
    if ct <= cd + m and ct >= cd - m:
        return True
    else:
        return False
    
cd = float(input('Comprimento de cortes dos tubos: '))
m = float(input('Margem de erro aceitável: '))
q = int(input('Quantidade de tubos demandada: '))
#ct = 0
n = 0
tr = 0
tt = 0
#l = ''
while tt < q:
    ct = float(input('Comprimento do tubo cortado: ')) 
    l = avaliaTubo(ct, cd, m)
    if l == True:
        tt = tt + 1
        n = n + 1
    else:
        print('Acima da margem de erro, tubo rejeitado')
        n = n + 1
        tr = tr + 1
print('Fim da produção, demanda atendida.')
print(f'Total de tubos cortados: {n}')
print(f'Total de tubos rejeitados: {tr}')
