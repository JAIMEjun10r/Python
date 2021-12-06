import random
import os
erros = 0
comentário = '''                =================================================================================
                                            Olá, pequeno gafanhoto! Vamos Brincar!!!                
                ================================================================================='''
print(comentário)
apresentação = str(input('Qual é o seu nome? '))
sorteado = random.randrange(0, 50)
jogador = int(input('Digite um número: '))
while (sorteado != jogador):
    os.system('cls')
    if (sorteado > jogador):
        print('Errou! O número é maior :(')
    elif(sorteado < jogador):
        print('Errou! O número é menor :(')
    erros += 1
    jogador = int(input('Digite um número: '))
print(
    f'Parabéns, {apresentação}! O número é {jogador} e você acertou em {erros + 1} tentativas.')
print('Até a próxima!')