class Cita:

    def __init__(self, codigo, paciente, medico, fecha):
        self.codigo = codigo
        self.paciente = paciente
        self.medico = medico
        self.fecha = fecha

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
    def paciente(self):
        return self._paciente

    @paciente.setter
    def paciente(self, valor):
        self._paciente = valor

    @property
    def medico(self):
        return self._medico

    @medico.setter
    def medico(self, valor):
        self._medico = valor

    @property
    def fecha(self):
        return self._fecha

    @fecha.setter
    def fecha(self, valor):
        self._fecha = valor

    def resumen(self):
        return (
            f"Cita: {self.codigo} | "
            f"Paciente: {self.paciente.nombre} | "
            f"Médico: {self.medico.nombre} | "
            f"Especialidad: {self.medico.especialidad} | "
            f"Fecha: {self.fecha}"
        )
