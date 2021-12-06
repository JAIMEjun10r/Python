celsius = []

print('Digite as temperaturas que você deseja converter de Celsius para fahrenheit')
usu1 = float(input('Digite o primeiro número: '))
celsius.append(usu1)
usu2 = float(input('Digite o segundoo número: '))
celsius.append(usu2)
usu3 = float(input('Digite o terceiro número: '))
celsius.append(usu3)
usu4 = float(input('Digite o quarto número: '))
celsius.append(usu4)
usu5 = float(input('Digite o quinto número: '))
celsius.append(usu5)
fahrenheit = [((float(9) / 5) * temp + 32) for temp in celsius]
print(fahrenheit)