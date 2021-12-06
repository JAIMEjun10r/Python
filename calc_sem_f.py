print('Bem vindo')
print('1. Somar   2. Multiplicar    3. Subtrair  4. Dividir')
usuario = int(input('Digite o número da opção: '))
if usuario == 1:
    ususoma = int(input('Digite o primeiro número da soma: '))
    ususoma2 = int(input('Digite o segundo número da soma: '))
    resulsoma = ususoma + ususoma2
    print(resulsoma)
elif usuario == 2:
    usumult = int(input('Digite o primeiro número da multiplicação: '))
    usumult2 = int(input('Digite o segundo número da soma: '))
    resultmult = usumult + usumult2
    print(resultmult)
elif usuario == 3:
    ususub = int(input('Digite o primeiro número da subtração: '))
    ususub2 = int(input('Digite o segundo número da subtração: '))
    resulsub = ususub - ususub2
    print(resulsub)
elif usuario == 4:
    usudiv = int(input('Digite o primeiro número da divisão: '))
    usudiv2 = int(input('Digite o segundo número da soma: '))
    resuldiv = usudiv / usudiv2
    print(resuldiv)
else:
    print('Essa opção não existe')