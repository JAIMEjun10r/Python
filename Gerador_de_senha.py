import string
import random
import os

min_mai = string.ascii_letters
digitos = string.digits
pontuacao = string.punctuation 
while 1:
    tamanho = int(input('Qual o comprimento da senha que você gostaria de gerar? '))
    contador = int(input('Quantas senhas você gostaria? '))
    os.system('cls')
    for x in range(0,contador):
        password = ''
        for x in range(0,tamanho):
            char_senha = random.choice(min_mai + digitos + pontuacao)
            password = password + char_senha     
        print('Sua senha é: ', password)