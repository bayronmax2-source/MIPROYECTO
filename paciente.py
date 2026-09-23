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
        if valor != "":
            self._codigo = valor
        else:
            print("ERROR: El código no puede estar vacío.")

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if valor != "":
            self._nombre = valor
        else:
            print("ERROR: El nombre no puede estar vacío.")

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, valor):
        if 0 <= valor <= 120:
            self._edad = valor
        else:
            print("ERROR: La edad debe estar entre 0 y 120.")

    def resumen(self):
        return f"Paciente: {self._codigo} - {self._nombre} - {self._edad} años"
