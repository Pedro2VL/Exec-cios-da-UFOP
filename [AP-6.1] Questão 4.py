i = 1
while i > 0:
    n = int(input('Digite um número: '))
    d = 1
    i = n
    s = 0
    while n > 1:
        if i % d == 0:
            s = s + d
            d = d + 1
            n = n - 1
        else:
            n = n - 1
            d = d + 1
    if n + d - 1 > 0:
        if s == n + d - 1:
            print(f'{n + d - 1} == {s}: número é perfeito ')
        else:
            print(f'{n + d - 1} <> {s}: número não é perfeito')


    

    
    