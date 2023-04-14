def imprimeRetangulo(a, l):
    for i in range(0,a):
        for n in range(0, l):
            print('*', end = "")
        print()
            
sn = input('Deseja imprimir um retângulo? (s/n)')
while (sn == 's'):
    a = int(input('\n Altura do retângulo: '))
    l = int(input('Largura do retângulo: '))
    print('')
    while (l < a):
        print('Entrada inválida. \n')
        a = int(input('\n Altura do retângulo: '))
        l = int(input('Largura do retângulo: '))
    imprimeRetangulo(a, l)
    print('')
    sn = input(' Deseja imprimir outro retângulo? (s/n) ')

        
        
    
    