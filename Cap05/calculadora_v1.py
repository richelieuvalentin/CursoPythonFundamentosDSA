# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso.
# A solução será apresentada no próximo capítulo!

print("\n******************* Calculadora em Python *******************")

print("\n Selecione o número da opção desejada:")

# Cria uma um dicionário onde as chaves representam a opção númerica
# E os valores as respectivas operações
operacoes = {
    1: "Soma",
    2: "Subtração",
    3: "Multiplicação",
    4: "Divisão",
    5: "Potenciação",
}

# Laço for para percorer o dicionário e imprimir as chaves e valores
for k, v in dict.items(operacoes):
    print(k, "-", v)

operacao_usuario = float(input())

#Define as funções para as operações matemáticas
def soma(num1, num2):
    return num1 + num2

def subtracao(num1, num2):
    return num1 - num2

def multiplicacao(num1, num2):
    return num1 * num2

def divisao(num1, num2):
    return num1 / num2

def potenciacao(num1, num2):
    return num1**num2

# Laço while para testar a escolha do usuário
while operacao_usuario not in [k for k in dict.keys(operacoes)]:
    print("\n Operação inválida")
    print("\n Digite novamente")
    operacao_usuario = float(input())

# Recebe do usuário os números para efetuar as operações
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Condiconais para determinar a operação a ser efetuada
if operacao_usuario == 1:
    print("\n RESULTADO: ", num1, "+", num2, "=", soma(num1, num2))

elif operacao_usuario == 2:
    print("\n RESULTADO: ", num1, "-", num2, "=", subtracao(num1, num2))

elif operacao_usuario == 3:
    print("\n RESULTADO: ", num1, "*", num2, "=", multiplicacao(num1, num2))

elif operacao_usuario == 4:
    if num2 == 0:
        print("Divisão por zero, favor reiniciar a calculadora!")
    else:
        print("\n RESULTADO: ", num1, "/", num2, "=", divisao(num1, num2))
else:
    print("\n RESULTADO: ", num1, "**", num2, "=", potenciacao(num1, num2))
