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
    def especialidad(self):
        return self._especialidad
    @especialidad.setter
    def especialidad(self, valor):
        if valor != "":
            self._especialidad = valor
        else:
            print("ERROR: La especialidad no puede estar vacía.")
    def resumen(self):
        return (
            f"Médico: {self._codigo} - "
            f"{self._nombre} - "
            f"{self._especialidad}"
        )
