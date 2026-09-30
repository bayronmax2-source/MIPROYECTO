class Paciente:

    def __init__(self, codigo, nombre, edad):
        self.codigo = codigo
        self.nombre = nombre
        self.edad = edad

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
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, valor):
        if 0 <= valor <= 120:
            self._edad = valor
        else:
            raise ValueError("La edad debe estar entre 0 y 120.")

    def resumen(self):
        return (
            f"Paciente: {self.codigo} - "
            f"{self.nombre} - "
            f"{self.edad} años"
        )
