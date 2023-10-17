class Juego:
    def __init__(self, nombre, monedas, vidas, tamaño, mundo, nivel, disparos):
        self.nombre = nombre
        self.monedas = monedas
        self.vidas = vidas
        self.tamaño = tamaño
        self.mundo = mundo
        self.nivel = nivel
        self.disparos = disparos

    def cambiar_mundo(self):
        self.nivel += 1
        if self.nivel >= 5:
            self.nivel = 1
            self.mundo += 1
            if self.mundo >= 9:
                self.mundo = 1
                self.nivel = 1

    def hongoscre(self):
        self.tamaño = "grande"

    def recoger_flor(self):
        if self.tamaño == "grande":
            self.disparos += 1

    def recoger_monedas(self):
        self.monedas += 20
        if self.monedas == 100:
            self.vidas += 1
        elif self.monedas > 100:
            self.monedas = 20

    def incidentes(self):
        if self.tamaño == "pequeño":
            self.vidas -= 1
        elif self.tamaño == "grande":
            self.tamaño = "pequeño"

    def incidenteg(self):
        self.vidas -= 1
        self.tamaño = "pequeño"

    def recoger_hongos_vida(self):
        self.vidas += 1

    def reiniciar(self):
        self.monedas = 0
        self.vidas = 3
        self.tamaño = "pequeño"
        self.mundo = 1
        self.nivel = 1


def mostrar(listaa):
    for per in listaa:
        print(
            "personaje:", per.nombre, "//",
            "monedas:", per.monedas, "//",
            "vidas:", per.vidas, "//",
            "tamaño:", per.tamaño, "//",
            "mundo:", per.mundo, "//",
            "nivel:", per.nivel, "disparos:", per.disparos
        )


def elegir_P(listaa):
    print("1. mario")
    print("2. luigi")
    personaje = int(input("Ingrese el personaje: "))
    if personaje == 1:
        nombre = "mario"
    elif personaje == 2:
        nombre = "luigi"
    monedas = 0
    vidas = 3
    tamaño = "pequeño"
    mundo = 1
    nivel = 1
    disparos = 0
    juego = Juego(nombre, monedas, vidas, tamaño, mundo, nivel, disparos)
    listaa.append(juego)
    return juego


listaa = []
opc = 0
while True:

    print("1. Elegir personaje")
    print("2. Avanzar")
    print("3. Recoger hongo de crecimiento")
    print("4. Recoger flor")
    print("5. Recoger monedas")
    print("6. Incidente sencillo")
    print("7. Incidente grave")
    print("8. Recoger hongo de vida")
    print("9. Reiniciar")
    print("10. Salir")

    opc = int(input("Selecciona una opción: "))

    if opc == 1:
        per = elegir_P(listaa)
        mostrar(listaa)
    elif opc == 2:
        per.cambiar_mundo()
        mostrar(listaa)
    elif opc == 3:
        per.hongoscre()
        mostrar(listaa)
    elif opc == 4:
        per.recoger_flor()
        mostrar(listaa)
    elif opc == 5:
        per.recoger_monedas()
        mostrar(listaa)
    elif opc == 6:
        per.incidentes()
        mostrar(listaa)
    elif opc == 7:
        per.incidenteg()
        mostrar(listaa)
    elif opc == 8:
        per.recoger_hongos_vida()
        mostrar(listaa)
    elif opc == 9:
        per.reiniciar()
        mostrar(listaa)
    elif opc >= 10:
        break

  
 
