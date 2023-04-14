import math
def calculaF(x,y):
    if x<=30:
        f = x**2 + 2*y - 3
    elif 30 < x <=60:
        f = math.sin(0.0175 * x)*math.cos(0.0175 * y)
    elif 60 < x <= 90:
        f = 1/x**-2 + y
    else:
        f = math.pi
    return round (f,2)

Ini = int(input('Valor inicial: '))
while -150 > Ini or Ini > 50:
    Ini = int(input('Valor inicial: '))
Fim = int(input('Valor final: '))
while Ini >= Fim:
    Fim = int(input('Valor final: '))
Passo = int(input('Passo: '))
while Passo <= 0:
    Passo = int(input('Passo: '))
print('\nx \ y |', end='')
for y in range (Ini,Fim+1,Passo):
    print(f'{y:10.0f}',end='')
print()
print('---------------------------')
for x in range (Ini,Fim+1,Passo):
    print(f'{x:5.0f} |',end='')
    for y in range (Ini,Fim+1,Passo):
        print(f'{calculaF(x,y):10.2f}',end='')
    print()