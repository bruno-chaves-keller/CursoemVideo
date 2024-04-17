#Faca um programa que leia a largura e a altura de uma parede em metros. Caucule sua area e a quantidade de tinta necessaria para pinta la, sabendo que cada litro de tinta pinta uma area de 2metros.
l = float(input('Qual a largura da sua parede?'))
m = float(input('Quantos metros tem sua parede?'))
c = (l * m) / 2
print('Baseado em suas dimensoes voce precisara de {:.2f} litros de tinta para a pintura total da sua parede.'.format(c))
