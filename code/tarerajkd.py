# Definir una clase para representar vehículos
class Vehiculo:
    # Constructor para inicializar atributos
    def __init__(self, marca, velocidad_maxima, color, pais):
        self.__marca = marca  # Marca del vehículo (privado)
        self.__velocidad = 0  # Velocidad actual del vehículo (privado)
        self.__velocidad_maxima = velocidad_maxima  # Velocidad máxima del vehículo (privado)
        self.color = color  # Color del vehículo (público)
        self._pais = pais  # País del vehículo (protegido)

    # Método para acelerar el vehículo
    def acelerar(self, cantidad):
        self.__velocidad += cantidad
        if self.__velocidad > self.__velocidad_maxima:
            self.__velocidad = self.__velocidad_maxima

    # Método para mostrar la velocidad actual del vehículo
    def mostrar_velocidad(self):
        return self.__velocidad

    # Método para desacelerar el vehículo
    def desacelerar(self, cantidad):
        self.__velocidad -= cantidad
        if self.__velocidad < 0:
            self.__velocidad = 0

# Crear una lista para almacenar vehículos
vehiculos = []

# Bucle principal para el menú
while True:
    print("Menú:")
    print("1. Agregar vehículo")
    print("2. Acelerar vehículo")
    print("3. Mostrar velocidad")
    print("4. Desacelerar vehículo")
    print("5. Salir")
    
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        marca = input("Marca del vehículo: ")
        velocidad_maxima = int(input("Velocidad máxima del vehículo: "))
        color = input("Color del vehículo: ")
        pais = input("País del vehículo: ")

        nuevo_vehiculo = Vehiculo(marca, velocidad_maxima, color, pais)
        vehiculos.append(nuevo_vehiculo)
        print("Vehículo agregado con éxito.")

    elif opcion == "2":
        if not vehiculos:
            print("No hay vehículos registrados.")
        else:
            for i, vehiculo in enumerate(vehiculos):
                print(f"{i + 1}. Marca: {vehiculo._Vehiculo__marca}, Color: {vehiculo.color}")
            seleccion = int(input("Seleccione un vehículo para acelerar: ")) - 1
            cantidad = int(input("Cantidad de aceleración: "))
            vehiculos[seleccion].acelerar(cantidad)
            print("Velocidad actual:", vehiculos[seleccion].mostrar_velocidad())

    elif opcion == "3":
        if not vehiculos:
            print("No hay vehículos registrados.")
        else:
            for i, vehiculo in enumerate(vehiculos):
                print(f"{i + 1}. Marca: {vehiculo._Vehiculo__marca}, Color: {vehiculo.color}")
            seleccion = int(input("Seleccione un vehículo para mostrar la velocidad: ")) - 1
            print("Velocidad actual:", vehiculos[seleccion].mostrar_velocidad())

    elif opcion == "4":
        if not vehiculos:
            print("No hay vehículos registrados.")
        else:
            for i, vehiculo in enumerate(vehiculos):
                print(f"{i + 1}. Marca: {vehiculo._Vehiculo__marca}, Color: {vehiculo.color}")
            seleccion = int(input("Seleccione un vehículo para desacelerar: ")) - 1
            cantidad = int(input("Cantidad de desaceleración: "))
            vehiculos[seleccion].desacelerar(cantidad)
            print("Velocidad actual:", vehiculos[seleccion].mostrar_velocidad())

    elif opcion == "5":
        print("Saliendo del programa.")
        break

    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
