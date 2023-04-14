def realizaCalculos(n, r):
    pi = 0
    for i in range(0, n):
        pi = pi + (-1)**i*(4/((2*i)+1))
    return round(pi, 5), round((4/3)*pi*r**3, 5)
n = int(input('Número de termos: '))
r = int(input('Raio da esfera: '))
p1, p2 = realizaCalculos(n, r)
print(f'pi = {p1}.')
print(f'Volume da esfera = {p2}.')