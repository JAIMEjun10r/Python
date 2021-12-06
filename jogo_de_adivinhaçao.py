from random import randint
from os import system

res = -1
ten = 0

num = randint(0, 50)

while res != num:
    res = int(input("Informe um numero entre 0 e 50\n> "))
    if res == num:
        print("Voce acertou! Mandou ver!")
    else:
        print("Voce errou :(")
        print(res > num and "o numero e menor" or "o numero e maior")
        system("pause")
        system("cls")
        ten += 1

print("Resposta: [{}]\nVocê acertou em {} tentativas".format(res, ten+1))