mn = float(input('Meta nacional: R$ '))
l = 0
num = 1
while (l < mn):
    n = input(f'. Nome do estado {num}: ')
    m = float(input('. Meta estadual: R$ '))
    c = 1
    le = 0
    while (le < m):
        v = float(input(f'.. Vendas na cidade {c}: R$ '))
        le = le + v
        c = c + 1
    num = num + 1
    l = l + le
    print(f'.. Meta do estado {n} cumprida!')
    print(f'.. Total do estado: R$ {le:.2f}.')
print('Meta nacional cumprida!')
print(f'Total nacional: R$ {l:.2f}.')