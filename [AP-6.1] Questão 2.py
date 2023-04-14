def Fatorial(n):
    p = 1
    while n > 0:
        p = p * n
        n = n -1
    return p

n = int(input('Informe o número que deseja calcular o Fatorial: '))

while n < 0:
    n = int(input('Número inválido, defina outro: '))
    
f = Fatorial(n)
print(f'O Fatorial de {n} é: {f}')
        
    