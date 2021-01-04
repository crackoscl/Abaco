import os


tablero = {
    1:" | | ", 2:" | | ", 3:" | | ", 4:" | | ", 5:" | | ", 6:" | | ",
    7:" | | ", 8:" | | ", 9:" | | ", 10:" | | ", 11:" | | ", 12:" | | ",
    13:" | | ", 14:" | | ", 15:" | | ", 16:" | | ", 17:" | | ", 18:" | | ",
    19:" | | ", 20:" | | ", 21:" | | ", 22:" | | ", 23:" | | ", 24:" | | ",
    25:" | | ", 26:" | | ", 27:" | | ", 28:" | | ", 29:" | | ", 30:" | | ",
    31:" | | ", 32:" | | ", 33:" | | ", 34:" | | ", 35:" | | ", 36:" | | ",
    37:" | | ", 38:" | | ", 39:" | | ", 40:" | | ", 41:" | | ", 42:" | | ",
    43:" | | ", 44:" | | ", 45:" | | ", 46:" | | ", 47:" | | ", 48:" | | ",
    49:" | | ", 50:" | | ", 51:" | | ", 52:" | | ", 53:" | | ", 54:" | | "    
}

usuario_intentos = []

def muestra_tablero(tablero):
    print("Bienvenido al Abaco, por favor ingrese numero del 1 al 999.999")
    print("    +-+      +-+     +-+      +-+       +-+       +-+")
    print("   {}    {}   {}    {}     {}     {}    ".format(
        tablero[1],tablero[2],tablero[3],tablero[4],tablero[5],tablero[6]))
    print("   {}    {}   {}    {}     {}     {}    ".format(
        tablero[7],tablero[8],tablero[9],tablero[10],tablero[11],tablero[12]))
    print("   {}    {}   {}    {}     {}     {}    ".format(
        tablero[13],tablero[14],tablero[15],tablero[16],tablero[17],tablero[18]))
    print("   {}    {}   {}    {}     {}     {}    ".format(
        tablero[19],tablero[20],tablero[21],tablero[22],tablero[23],tablero[24]))
    print("   {}    {}   {}    {}     {}     {}    ".format(
        tablero[25],tablero[26],tablero[27],tablero[28],tablero[29],tablero[30]))
    print("   {}    {}   {}    {}     {}     {}    ".format(
        tablero[31],tablero[32],tablero[33],tablero[34],tablero[35],tablero[36]))
    print("   {}    {}   {}    {}     {}     {}    ".format(
        tablero[37],tablero[38],tablero[39],tablero[40],tablero[41],tablero[42]))
    print("   {}    {}   {}    {}     {}     {}    ".format(
        tablero[43],tablero[44],tablero[45],tablero[46],tablero[47],tablero[48]))
    print("   {}    {}   {}    {}     {}     {}    ".format(
        tablero[49],tablero[50],tablero[51],tablero[52],tablero[53],tablero[54]))
    print("    +-+      +-+     +-+      +-+       +-+       +-+")
    print(str("  100.000   10.000  1.000     100       10         1"))
    
    return tablero


def principal(lista):
    
    monto = (input('ingrese Monto:'))
    if monto.isdigit():
        usuario_intentos.append(monto)
        montos = [100000,10000,1000,100,10,1]
        for i in montos:
                sobrante =  int(monto) // i
                monto = int(monto) % i
                lista.append(sobrante)
        return lista
    else:
        return monto

def ordena_abaco(lista, tablero):
    if lista[0] > 0:
        clav = 49
        for i in range(0, lista[0]):
            tablero.update({clav:"xxxxx"})
            clav -= 6
    if lista[1] > 0:
        clav = 50
        for i in range(0, lista[1]):
            tablero.update({clav:"xxxxx"})
            clav -= 6
    if lista[2] > 0:
        clav = 51
        for i in range(0, lista[2]):
            tablero.update({clav:"xxxxx"})
            clav -= 6
    if lista[3] > 0:
        clav = 52
        for i in range(0, lista[3]):
            tablero.update({clav:"xxxxx"})
            clav -= 6
    if lista[4] > 0:
        clav = 53
        for i in range(0, lista[4]):
            tablero.update({clav:"xxxxx"})
            clav -= 6
    if lista[5] > 0:
        clav = 54
        for i in range(0, lista[5]):
            tablero.update({clav:"xxxxx"})
            clav -= 6
    return lista 

def limpiar_tablero(tablero):
    for i in range(1, 54):
        for clave, valor in tablero.items():
            if valor != " | | ":
                tablero.update({clave:" | | "})


if os.name == "posix":
   limpiar = "clear"       
elif os.name == "ce" or os.name == "nt" or os.name == "dos":
   limpiar = "cls"

salir  = True
while True:
    lista = []
    limpiar_tablero(tablero)
    inicio = principal(lista)
    if inicio == 'salir':
        break
    os.system(limpiar)
    ordena_abaco(lista, tablero)
    muestra_tablero(tablero)
    print(usuario_intentos)
    