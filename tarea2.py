

def palindromo(numero):
    cadena = str(numero)
    listanum = list(cadena)
    largolist = len(listanum)
    cpermitido = '1' '2' '3' '4' '5' '6' '7' '8' '9' '0' '-'
    numcontrol = []
    x = largolist - 1
    if listanum[0] == '-':
        numcontrol.insert(0, listanum[0])
    while x >= 0:
        if(listanum[x] in cpermitido):
            if listanum[x] == '-':
                pass
            else:
                numcontrol.append(listanum[x])
        else:
            print('error cadena ingresada no es un entero')
            return False
        x = x - 1
    if numcontrol == listanum:
        print('numero es palindromo')
        return True
    else:
        print('numero no es palindromo')
        return False


def array(minimo, maximo):
    if(minimo > maximo):
        print('parametros no validos')
        return False
    else:
        array = []
        escalon = (maximo - minimo)/99
        array.append(minimo)
        x = minimo + escalon
        while x <= maximo:
            array.append(x)
            x = x + escalon
        array.append(maximo)
        return array


def archivo():
    # j = input("Ingrese el nomnre del archivo: ")
    # tex= open('texto.txt', 'r')
    tex = open('texto .txt', 'r')
    carga = tex.read()
    print(carga)
    i = str(input("Qué desea buscar: "))
    # i=str('abc')
    print(carga.count(i))
    tex.close()
