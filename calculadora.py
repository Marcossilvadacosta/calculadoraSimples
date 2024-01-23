"""Criar calculadora em aula"""

###interação com usúario###
while True:

    number1 = 0
    number2 = 0
    result = 0
    operation = " "

    number1 = int(input("Digite o primeiro número "))
    operation = input("Digite a operação ")
    number2 = int(input("Digite o segundo número "))

    ###Lógica das operações###

    if operation == "+":
            result = number1 + number2
    elif operation == "-":
            result = number1 - number2
    elif operation == "/":
            result = number1 / number2
    elif operation == "*":
            result = number1 * number2
    else:
        result = "operation fail"

    print(str(number1)+" "+str(operation)+" "+str(number2)+"= "+str (result))
          