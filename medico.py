class Medico:

    def __init__(self, codigo, nombre, especialidad):
        self.codigo = codigo
        self.nombre = nombre
        self.especialidad = especialidad

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, valor):
        if valor.isdigit():
            self._codigo = valor
        else:
            raise ValueError("El código debe contener solo números.")

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if valor.replace(" ", "").isalpha():
            self._nombre = valor
        else:
            raise ValueError("El nombre debe contener solo letras.")

    @property
    def especialidad(self):
        return self._especialidad

    @especialidad.setter
    def especialidad(self, valor):
        self._especialidad = valor

    def resumen(self):
        return (
            f"Médico: {self.codigo} - "
            f"{self.nombre} - "
            f"Especialidad: {self.especialidad}"
        )


def seleccionar_especialidad():
    while True:
        print("\n=== ESPECIALIDADES ===")
        print("1. Medicina General")
        print("2. Pediatría")
        print("3. Obstetricia")
        print("4. Cirugía General")
        print("5. Nutrición")

        opcion = input("Seleccione una especialidad: ")

        match opcion:
            case "1":
                return "Medicina General"
            case "2":
                return "Pediatría"
            case "3":
                return "Obstetricia"
            case "4":
                return "Cirugía General"
            case "5":
                return "Nutrición"
            case _:
                print("ERROR: Especialidad no válida.")
