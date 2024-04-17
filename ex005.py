#Faca um programa que leia um numero inteiro e mostre na tela seu antecessor e seu sucessor.
num = int(input('Digite um numero:'))
sub = num - 1
a = num + 1
print('O numero escolhido foi {0}! Seu numero antecessor e {1} e seu numero superior e {2}!'.format(num, sub, a))

#Outra forma de fazer sem precisar ficar armazenando as variaveis sub e a.
#num = int(input('Digite um numero:'))
#print('O numero escolhido foi {0}! Seu numero antecessor e {1} e seu numero superior e {2}!'.format(num, (num - 1), (num + 1)))
