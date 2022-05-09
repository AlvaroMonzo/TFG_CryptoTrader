

class MiClase():

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


    def mostrar_datos(self, frase):

        print(f"{frase} -> {self.nombre} - {self.apellido}")

        self.nombre = "Nuevo nombre"

        print(f"{frase} -> {self.nombre} - {self.apellido}")


if __name__ == "__main__":

    mi_clase = MiClase("Alvaro", "Monzon")
    mi_clase.mostrar_datos("Este es mi nombre")
