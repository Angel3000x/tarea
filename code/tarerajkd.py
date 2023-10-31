import random
class Tragamonedas:
    def __init__(self):
        self.creditos_disponibles = 0
        self.creditos_ganados = 0
        self.opciones = ['Bar/Bar', 'Bar', '77', 'Estrellas', 'Sandia', 'Melón', 'Campana', 'Naranja', 'Manzana', 'Cereza']

    def insertar_monedas(self, cantidad):
        if self.creditos_disponibles + cantidad > 999:
            print("Has alcanzado el límite máximo de créditos.")
        else:
            self.creditos_disponibles += cantidad

    def apostar(self, opcion, creditos_apostados):
        if creditos_apostados <= 0 or creditos_apostados > 9 or creditos_apostados > self.creditos_disponibles:
            print("Apuesta inválida. Inténtalo de nuevo.")
        else:
            self.creditos_disponibles -= creditos_apostados
            self.girar(opcion, creditos_apostados)

    def girar(self, opcion, creditos_apostados):
        resultado = random.choice(self.opciones)
        print(f"Resultado: {resultado}")
        if resultado == opcion:
            premio = creditos_apostados * (self.opciones.index(opcion) + 1)
            self.creditos_disponibles += premio
            self.creditos_ganados += premio
            print(f"¡Felicidades! Has ganado {premio} créditos.")
        else:
            print("Lo siento, no has ganado esta vez.")           

    def cobrar_creditos(self):
        print(f"Tienes {self.creditos_disponibles} créditos disponibles y {self.creditos_ganados} créditos ganados.")
        self.creditos_ganados = 0

    def jugar_de_nuevo(self):
        self.girar('Bar/Bar', self.creditos_disponibles)


tragamonedas = Tragamonedas()
while True:
    print("\n===== MÁQUINA TRAGAMONEDAS =====")
    print(f"Créditos disponibles: {tragamonedas.creditos_disponibles}")
    print(f"Créditos ganados: {tragamonedas.creditos_ganados}")
    print("\n1. Insertar monedas")
    print("2. Apostar")
    print("3. Cobrar créditos")
    print("4. Jugar de nuevo")
    print("5. Salir")
   
    opcion = input("\nElige una opción: ")
    if opcion == '1':
        monedas = int(input("Ingresa la cantidad de monedas a insertar (máximo 999): "))
        tragamonedas.insertar_monedas(monedas)
    elif opcion == '2':
        apuesta = input(f"Elige una opción para apostar {tragamonedas.opciones}: ")
        creditos_apostados = int(input("Ingresa la cantidad de créditos a apostar (máximo 9): "))
        tragamonedas.apostar(apuesta, creditos_apostados)
    elif opcion == '3':
        tragamonedas.cobrar_creditos()
    elif opcion == '4':
        tragamonedas.jugar_de_nuevo()
    elif opcion == '5':
        print("¡Gracias por jugar!")
        break
    else:
        print("Opción inválida. Inténtalo de nuevo.")


