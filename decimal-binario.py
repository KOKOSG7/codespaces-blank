fin = 0
while fin == 0:
    decimal = int(input("Numero: "))
    if decimal <= 0:
        decimal = "0"
    binario = ""
    while decimal > 0:
        resto = int(decimal % 2)
        decimal = int(decimal / 2)
        binario = str(resto) + binario
    resultado = binario
    print(resultado)
    input1 = input("Desea hacer otro calculo? Y/N: ")
    cont = input1.upper()
    if cont == "Y":
        print("------------------------------")
    elif cont == "N":
        fin = 1