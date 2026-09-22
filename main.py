class Cita:

    def __init__(self, codigo, paciente, medico, fecha):
        self.codigo = codigo
        self.paciente = paciente
        self.medico = medico
        self.fecha = fecha

    # ==========================================
    # PROPIEDAD CODIGO
    # ==========================================

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, valor):
        if valor != "":
            self._codigo = valor
        else:
            print("ERROR: El código de la cita no puede estar vacío.")

    # ==========================================
    # PROPIEDAD PACIENTE
    # ==========================================

    @property
    def paciente(self):
        return self._paciente

    @paciente.setter
    def paciente(self, valor):
        if valor is not None:
            self._paciente = valor
        else:
            print("ERROR: El paciente no puede estar vacío.")

    # ==========================================
    # PROPIEDAD MEDICO
    # ==========================================

    @property
    def medico(self):
        return self._medico

    @medico.setter
    def medico(self, valor):
        if valor is not None:
            self._medico = valor
        else:
            print("ERROR: El médico no puede estar vacío.")

    # ==========================================
    # PROPIEDAD FECHA
    # ==========================================

    @property
    def fecha(self):
        return self._fecha

    @fecha.setter
    def fecha(self, valor):
        if valor != "":
            self._fecha = valor
        else:
            print("ERROR: La fecha no puede estar vacía.")

    # ==========================================
    # RESUMEN
    # ==========================================

    def resumen(self):
        return (
            f"Cita: {self._codigo} | "
            f"Paciente: {self._paciente.nombre} | "
            f"Médico: {self._medico.nombre} | "
            f"Especialidad: {self._medico.especialidad} | "
            f"Fecha: {self._fecha}"
        )
