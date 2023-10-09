fin = 0
while fin == 0:
    decimal = int(input("Numero: "))
    if decimal <= 0:
        decimal = "0"
    # Aquí almacenamos el resultado
    binario = ""
    # Mientras se pueda dividir...
    while decimal > 0:
        # Saber si es 1 o 0
        resto = int(decimal % 2)
        # E ir dividiendo el decimal
        decimal = int(decimal / 2)
        # Ir agregando el número (1 o 0) a la izquierda del resultado
        binario = str(resto) + binario
    resultado = binario
    print(resultado)
    input1 = input("Desea hacer otro calculo? Y/N: ")
    cont = input1.upper()
    if cont == "Y":
        print("------------------------------")
    elif cont == "N":
        fin = 1