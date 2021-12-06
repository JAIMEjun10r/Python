import math as ma
import os

def soma(a,b):
    return a + b
    
def subtracao(c,d):
    return c - d

def multipli(e,f):
    return e * f

def divisao(g,h):

    return g / h
def loga(i):
    return ma.log10(i)

def raiz_quadrada(j):
    return(ma.sqrt(j))



print('                    Bem vindo!                         ')
comentario ='''
   1. Somar
   2. Subtrair
   3. Multiplicar
   4. Dividir
   5. Logarítimo
   6. Raiz quadrada
   7. Porcentagem
   8. Fatorial'''
print(comentario)
primeiro = input('Escolha um número: ')

if primeiro == '1':
    a = int(input('Digite o primeiro número: '))
    b = int(input('Digite o segundo número: '))
    print(soma(a,b))
elif primeiro == '2':
    c = int(input('Digite o primeiro número: '))
    d = int(input('Digite o segundo número: '))
    print(subtracao(c,d)) 
elif primeiro == '3':
    e = int(input('Digite o primeiro número: '))
    f = int(input('Digite o segundo número: '))
    print(multipli(e,f)) 
elif primeiro == '4':
    g = int(input('Digite o primeiro número: '))
    h = int(input('Digite o segundo número: '))
    print(divisao(g,h)) 
elif primeiro == '5':
    i = int(input('Digite o número que você deseja saber o logaritimo: '))
    print(loga(i))
elif primeiro == '6':
    j = int(input('Digite o número que você deseja saber a raiz quadrada: '))
    print(raiz_quadrada(j))