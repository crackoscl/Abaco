
import os


class Abaco:

    def __init__(self):
        self.board = []
        self.excess_list = []
        self.user_attempts = []

    def enter_amount(self, amount):
        self.user_attempts.append(amount)
        amounts = [100000, 10000, 1000, 100, 10, 1]
        for i in amounts:
            excess = int(amount) // i
            amount = int(amount) % i
            self.excess_list.append(excess)
        return amount

    def show_board(self):
        show_top_down = "    +-+  " * 6
        print("Bienvenido al Abaco, por favor ingrese numero del 1 al 999.999")
        print("Escriba salir para cerrar el abaco")
        print(show_top_down)
        for i in range(0, 9):
            for j in range(0, 6):
                print(self.board[i][j], end='')
            print()
        print(show_top_down)
        print(str("  100.000   10.000  1.000     100       10         1"))

    def show_bars(self):
        for i in range(0, 9):
            for j in range(0, 6):
                if self.excess_list[j] > 0:
                    for k in range(1, self.excess_list[j]+1):
                        self.board[-k][j] = '   xxxxx '

    def set_values(self):
        self.excess_list = []
        self.board = [["    | |  "] * 6 for x in range(0, 9)]


if os.name == "posix":
    limpiar = "clear"
elif os.name == "ce" or os.name == "nt" or os.name == "dos":
    limpiar = "cls"

if __name__ == "__main__":
    abaco = Abaco()

    while True:
        abaco.set_values()
        amount = (input('ingrese monto:'))
        if amount.isdigit():
            if int(amount) <= 0 or int(amount) > 999999:
                print('numero debe ser mayor a 0 y menor a 999999')
            else:
                ingresar = abaco.enter_amount(amount)
                os.system(limpiar)
                abaco.show_bars()
                abaco.show_board()
                print('intentos', abaco.user_attempts)
        else:
            if amount.lower() == 'salir':
                break
            else:
                print('valor ingresado no es valido')
