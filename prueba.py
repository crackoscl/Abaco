
import os

fichas = [
    ["  | |  ","  | |  ","  | |  ","  | |  ","  | |  ","  | |  "],
    ["  | |  ","  | |  ","  | |  ","  | |  ","  | |  ","  | |  "],
    ["  | |  ","  | |  ","  | |  ","  | |  ","  | |  ","  | |  "],
    ["  | |  ","  | |  ","  | |  ","  | |  ","  | |  ","  | |  "],
    ["  | |  ","  | |  ","  | |  ","  | |  ","  | |  ","  | |  "],
    ["  | |  ","  | |  ","  | |  ","  | |  ","  | |  ","  | |  "],
    ["  | |  ","  | |  ","  | |  ","  | |  ","  | |  ","  | |  "],
    ["  | |  ","  | |  ","  | |  ","  | |  ","  | |  ","  | |  "],
    ["  | |  ","  | |  ","  | |  ","  | |  ","  | |  ","  | |  "]
    ]

lista = []
usuario_intentos = []

def mostrar_abaco():
    print("abaco con listas :D")
    print("  +-+     +-+     +-+     +-+     +-+     +-+")
    for i in range(0,9):
        for j in range(0,6):
            print(fichas[i][j] ,end=" ")
        print()
    print("  +-+     +-+     +-+     +-+     +-+     +-+")
    print("100.000   10.000  1.000   100      10      1")
    print("-----------------------------------------------")
    print("intentos",usuario_intentos)

def crear_lista(lista):
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
    

def pintar_abaco(lista,fichas):
    for i in range(0,9):
        for j in range(0,6):
            if lista[0] > 0:
                for x in range(1,lista[0]+1):
                    fichas[-x][0] = " xxxxx "
            if lista[1] > 0:
                for x in range(1,lista[1]+1):
                    fichas[-x][1] = " xxxxx "
            if lista[2] > 0:
                for x in range(1,lista[2]+1):
                    fichas[-x][2] = " xxxxx "
            if lista[3] > 0:
                for x in range(1,lista[3]+1):
                    fichas[-x][3] = " xxxxx "
            if lista[4] > 0:
                for x in range(1,lista[4]+1):
                    fichas[-x][4] = " xxxxx "
            if lista[5] > 0:
                for x in range(1,lista[5]+1):
                    fichas[-x][5] = " xxxxx "       
    
if os.name == "posix":
   limpiar = "clear"       
elif os.name == "ce" or os.name == "nt" or os.name == "dos":
   limpiar = "cls"


mostrar_abaco()
crear_lista(lista)
pintar_abaco(lista,fichas)
mostrar_abaco()
    