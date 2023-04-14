n1 = input('Nome do candidato 1: ')
u1 = int(input('Número do candidato 1:'))
n2 = input('Nome do candidato 2:')
u2 = int(input('Número do candidato 2:'))
n = int(input('Quantidade de eleitores: '))
while (n < 3):
    print('A quantidade de eleitores é inferior a 3')
    n = int(input('Quantidade de eleitores: '))
print('')
print('## Votação Iniciada')
s1 = 0
s2 = 0
iv = 0
for i in range(0, n):
    nc = int(input('Número do candidato que deseja votar:'))
    if nc == u1:
        s1 = s1 + 1
    elif nc == u2:
        s2 = s2 + 1
    else:
        iv = iv + 1
print('##Votação Encerrada')
print('')
print(f'Votos válidos: {((s1+s2)/n)*100:.2f}% ({s1+s2} votos)')
print(f'Votos inválidos: {(iv/n)*100:.2f}% ({iv} votos)')
if s1 == 0 and s2 == 0:
    print(f'Votos para {n1}: 0.00% ({s1} votos)')
    print(f'Votos para {n2}: 0.00% ({s2} votos)')
else:
    print(f'Votos para {n1}: {(s1/(s1+s2))*100:.2f}% ({s1} votos)')
    print(f'Votos para {n2}: {(s2/(s1+s2))*100:.2f}% ({s2} votos)')


        