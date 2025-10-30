primeiro_numero = int(input("Digite o primeiro número: "))
segundo_segundo = int(input("Digite o segundo número: "))
operacao = input("Digite a operação desejada! \n+ para adição, \n- para subtração, \n* para multiplicação, \n/ para divisão \n: ")

resultado = None

if operacao == "+":
    resultado = primeiro_numero + segundo_segundo
elif operacao == "-":
    resultado = primeiro_numero - segundo_segundo
elif operacao == "*":
    resultado = primeiro_numero * segundo_segundo
elif operacao == "/":
    resultado = primeiro_numero / segundo_segundo
else:
    print("Digite uma operação válida para eu calcular.")

if resultado:
    print(f"O resultado da operação é {resultado}")
