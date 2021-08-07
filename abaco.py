
import os


class Abaco:

    def __init__(self):
        self.tablero = [["    | |  "] * 6 for x in range(0, 9)]
        self.lista = list()
        self.usuario_intentos = list()

    def ingresar_monto(self):
        monto = (input('ingrese Monto:'))
        if monto.isdigit():
            self.usuario_intentos.append(monto)
            montos = [100000, 10000, 1000, 100, 10, 1]
            for i in montos:
                sobrante = int(monto) // i
                monto = int(monto) % i
                self.lista.append(sobrante)
            return monto
        else:
            return monto

    def mostrar_tablero(self):
        print("Bienvenido al Abaco, por favor ingrese numero del 1 al 999.999")
        print("    +-+  " * 6)
        for i in range(0, 9):
            for j in range(0, 6):
                print(self.tablero[i][j], end='')
            print()
        print("    +-+  " * 6)
        print(str("  100.000   10.000  1.000     100       10         1"))

    def ordenar_abaco(self):
        for i in range(0, 9):
            for j in range(0, 6):
                if self.lista[j] > 0:
                    for k in range(1, self.lista[j]+1):
                        self.tablero[-k][j] = '   xxxxx '

    def limpiar_datos(self):
        self.lista = []
        self.tablero = [["    | |  "] * 6 for x in range(0, 9)]


if os.name == "posix":
    limpiar = "clear"
elif os.name == "ce" or os.name == "nt" or os.name == "dos":
    limpiar = "cls"

if __name__ == "__main__":
    abaco = Abaco()

    while True:
        abaco.limpiar_datos()
        ingresar = abaco.ingresar_monto()
        if ingresar == 'salir':
            break

        elif int(ingresar) < 0:
            print('numero debe ser mayor a 0')

        else:
            os.system(limpiar)
            abaco.ordenar_abaco()
            abaco.mostrar_tablero()
            print('intentos', abaco.usuario_intentos)
