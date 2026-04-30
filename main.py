# def metrosParaCentimetros(metros = 0):
#   return metros * 100
# print(metrosParaCentimetros(int(input("Digite um número: "))))

# def potencia(base, expoente):
#   return base ** expoente

# print(potencia(int(input("Digite a base: ")), int(input("Digite o expoente: "))))

# def mostraNome(nome):
#     return f"Bem-vindo {nome}!"

# print (mostraNome(input("Digite seu nome: ")))

# def verificaNumero(numero):
#     if numero % 2 == 0:
#         return f"{numero} é par!"
#     else:
#         return f"{numero} é ímpar!"

# print(verificaNumero(int(input("Digite um número: "))))

# num = int(input("Digite um número: "))
# i = num
# fat = 1
# while(i >= 1):
#     fat *= i
#     i -= 1
# print(f"{num}! = {fat}")

# def calculaFatorial(num):
#     if num == 1:
#         return True
#     return num * calculaFatorial(num - 1)

# print(calculaFatorial(int(input("Digite um número: "))))








## TRABALHO
# Exercício 01
# def celsiusParaFahrenheit(c):
#   return (c * 1.8) + 32

# def fahrenheitParaCelsius(f):
#   return (f - 32) / 1.8

# print("--- CONVERSOR DE TEMPERATURA ---")
# print("1. Celsius para Fahrenheit \n")
# print("2. Fahrenheit para Celsius \n")
# escolha = input("Escolha a opção (1 ou 2): ")
# if escolha == '1':
#   temp = float(input("Digite a temperatura em °C: "))
#   resultado = celsiusParaFahrenheit(temp)
#   print(f"{temp}°C é igual a {resultado:.2f}°F")
# elif escolha == '2':
#   temp = float(input("Digite a temperatura em °F: "))
#   resultado = fahrenheitParaCelsius(temp)
#   print(f"{temp}°F é igual a {resultado:.2f}°C")
# else:
#   print("Valor inválido!")


# Exercício 02
# def soma(n1, n2, n3):
#     return n1 + n2 + n3

# def media(n1, n2, n3):
#     return soma(n1, n2, n3) / 3

# n1 = int(input("Digite o primeiro número: "))
# n2 = int(input("Digite o segundo número: "))
# n3 = int(input("Digite o terceiro número: "))

# print(f"A soma é: {soma(n1, n2, n3)} \n")
# print(f"A média é: {media(n1, n2, n3)} \n")


# Exercício 03
# num = int(input("Digite o primeiro número: "))
# num2 = int(input("Digite o segundo número: "))
# num3 = int(input("Digite o terceiro número: "))


# def calculaMaior(num, num2, num3):
#   if num > num2 and num > num3:
#     return num
#   elif num2 > num and num2 > num3:
#     return num2
#   elif num3 > num and num3 > num2:
#     return num3
# print(f"O número maior é: {calculaMaior(num, num2, num3)}")


# def calculaMenor(num, num2, num3):
#   if num < num2 and num < num3:
#     return num
#   elif num2 < num and num2 < num3:
#     return num2
#   elif num3 < num and num3 < num2:
#     return num3
# print(f"O número menor é: {calculaMenor(num, num2, num3)}")

# Exercício 05
# def somaImposto(taxaImposto, custo):
#     custo = custo + (custo * taxaImposto / 100)
#     return custo


#programa principal
# custo = float(input("Digite o valor do produto: "))
# taxa = float(input("Digite a taxa de imposto (%): "))

# Exercício 04
# def verifica_numero(n):
#     if n > 0:
#         return 'P'
#     else:
#         return 'N'

# num = float(input("Digite um número: "))
# print("Resultado:", verifica_numero(num))

# Exercício 06
# def somar(a, b):
#   return a + b
# def subtrair(a, b):
#   return a - b
# def multiplicar(a, b):
#   return a * b
# def dividir(a, b):
#   return a / b
# while True:
#   print("----- MENU DE OPERAÇÕES -----")
#   print("1 - Somar")
#   print("2 - Subtrair ")
#   print("3 - Multiplicar")
#   print("4 - Dividir")
#   print("5 - Sair")
#   opcao = input ("\n Escolha uma opção: ")
#   if opcao == '5':
#     break
#   if opcao in ['1', '2', '3', '4']:
#     num1 = int(input("Digite o primeiro número: "))
#     num2 = int(input("Digite o segundo número: "))
#     if opcao == '1':
#       print(f"Resultado: {somar(num1, num2)} \n")
#     elif opcao == '2':
#       print(f"Resultado: {subtrair(num1, num2)} \n")
#     elif opcao == '3':
#       print(f"Resultado: {multiplicar(num1, num2)} \n")
#     elif opcao == '4':
#       print(f"Resultado: {dividir(num1, num2)} \n")
#   else:
#       print("Opção inválida! Tente novamente.\n")

# Exercício 07
# def tabuada(n, i=1):
#   if i > 10:
#     return
#   print(f"{n} x {i} = {n * i}")
#   tabuada(n, i + 1)

# numero = int(input("Digite um número: "))
# tabuada(numero)

# Exercício 08
# raio = float(input("Digite o valor do raio: "))
# def calcular_area_circulo(raio):
#   return 3.14 * raio ** 2
# print(calcular_area_circulo(raio))


# Exercício 09
# num = float(input("Digite sua média: "))

# def calculaMedia(media):
#   if num >= 7:
#     return "Aprovado"
#   elif num >= 5 and num <= 6.9:
#     return "Recuperação"
#   else:
#     return "Reprovado"

# print(calculaMedia(num))


# Exercício 10
# def calcular_area_retangulo(base, altura):
#   area = base * altura
#   return area

# b = float(input("Digite a base: "))
# h = float(input("Digite a altura: "))

# resultado = calcular_area_retangulo(b, h)
