

''' 49. Crie um programa que leia duas notas (reais), uma letra (A ou P), onde: A refere-se a média 
ARITMÉTICA e P refere-se a média PONDERADA. Em seguida, crie uma função que 
receba estes 3 valores e:
a) identifique qual o tipo de média (A, P)
b) retorne o valor da média, de acordo com o tipo solicitado.
c) OBS: considerar 30% (nota1) e 70% (nota 2)

'''
import math

Valor1 = int(input('Valor 1  : '))
Valor2 = int(input('Valor 2  : '))
Soma = Valor1 + Valor2
print(f"Soma dos valores: {Soma}")

modo = input('\nVocê deseja:\n1 - ARITMÉTICA \n2 - PONDERADA\n: ')
resultado = ''

if (modo == '1'):
    print('ARITMÉTICA ')
    
mediaAritimetica = int((Valor1 + Valor2)/2)
print(f"\nMedia Aritimetica = {mediaAritimetica}")

print(f"Valor 1  + 30% : {Valor1+(Valor1*30/100)}")

print(f"Valor 2  + 70% : {Valor2+(Valor2*70/100)}")


if (modo == '2'):
    print('PONDERADA')
    
    peso = int(input("\nDigite os pesos das notas: "))
    
    mediaPonderada = int(((Soma*peso)+(Soma*peso))/(peso+peso))

    print(f"\nMedia Ponderada = {mediaPonderada:,.1f}\n")

    print(f"Valor 1  + 30% : {Valor1+(Valor1*30/100)}")

    print(f"Valor 2  + 70% : {Valor2+(Valor2*70/100)}")