#Crie um algoritimo que leia um numero e mostre o seu dobro, triplo e raiz quadrada.
num = int(input('Digite um numero:'))
dobro = num * 2
triplo = num * 3
raizq = num ** (1/2)
print('O numero escolhido foi: {}! Seu dobro e {}, seu triplo e {} e a raiz quadrada dele e {:.2f}!'.format(num, dobro, triplo, raizq))
