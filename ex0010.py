#Crie um programa que leia quanto dinheiro uma pessoa tem em sua carteira e mostre quantos dolares ela pode comprar.
#Considerando dolar a US$1,00 = RS$3,27

num = float(input('Quantos reais voce tem em sua carteira?'))
c = num / 3.27
print('Com seu valor em reais estipulado voce consegue comprar {:.2f} dolares!.'.format(c))

