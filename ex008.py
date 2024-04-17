#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.
num = float(input('Digite um valor:'))
c = num * 100
m = num * 1000
print('Seu numero escolhido ({} metros), convertido a centimetros e {:.0f} e em milimetros {:.0f}'.format(num, c, m))
