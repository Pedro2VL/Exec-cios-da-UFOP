def calculaJ(ce, m):
    j = 0
    if ce > 10000:
        j = 7
        jd = ce*0.07*m
        return jd, j
    else:
        j = 10
        jd = ce*0.1*m
        return jd , j
    
c = 1
ce = 0

c = float(input('Capital Total para empréstimo: '))
while c > ce:   
    ce = float(input('Capital emprestado: '))
    if ce > c:
        print(f'Empréstimo negado, capital total é de R${c:.2f}')
    else:
        m = int(input('Quantidade de meses para quitação: '))
        jd, tx = calculaJ(ce, m)
        print(f'Taxa de juros aplicada: {tx}%.')
        print(f'Juros devido: {jd:.2f}.')
        print(f'Valor total: {jd + ce:.2f}.')
        c = c - ce
        ce = 0
