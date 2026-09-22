from paciente import Paciente
from medico import Medico
from cita import Cita


# ==========================================
# LISTAS DEL SISTEMA
# ==========================================

pacientes = []
medicos = []
citas = []
atenciones = []


# ==========================================
# FUNCIÓN POLIMÓRFICA
# ==========================================

def mostrar_resumen(objeto):
    print(objeto.resumen())


# ==========================================
# REGISTRAR PACIENTE
# ==========================================

def registrar_paciente():

    print("\n========== REGISTRAR PACIENTE ==========")

    codigo = input("Ingrese código del paciente: ")

    if codigo == "":
        print("ERROR: El código no puede estar vacío.")
        return

    # Verificar código duplicado

    for paciente in pacientes:

        if paciente.codigo == codigo:
            print("ERROR: El código del paciente ya está registrado.")
            return

    nombre = input("Ingrese nombre del paciente: ")

    if nombre == "":
        print("ERROR: El nombre no puede estar vacío.")
        return

    # Validar edad

    while True:

        try:

            edad = int(input("Ingrese edad del paciente: "))

            if 0 <= edad <= 120:
                break
            else:
                print("ERROR: La edad debe estar entre 0 y 120.")

        except ValueError:

            print("ERROR: La edad debe ser un número.")

    paciente = Paciente(codigo, nombre, edad)

    pacientes.append(paciente)

    print("Paciente registrado correctamente.")


# ==========================================
# REGISTRAR MEDICO
# ==========================================

def registrar_medico():

    print("\n========== REGISTRAR MEDICO ==========")

    codigo = input("Ingrese código del médico: ")

    if codigo == "":
        print("ERROR: El código no puede estar vacío.")
        return

    # Verificar código duplicado

    for medico in medicos:

        if medico.codigo == codigo:
            print("ERROR: El código del médico ya está registrado.")
            return

    nombre = input("Ingrese nombre del médico: ")

    if nombre == "":
        print("ERROR: El nombre no puede estar vacío.")
        return

    # ==========================================
    # SELECCIONAR ESPECIALIDAD
    # ==========================================

    print("\n========== ESPECIALIDADES ==========")
    print("1. Medicina General")
    print("2. Pediatría")
    print("3. Obstetricia")
    print("4. Cirugía General")
    print("5. Nutrición")

    opcion_especialidad = input("Seleccione una especialidad: ")

    match opcion_especialidad:

        case "1":
            especialidad = "Medicina General"

        case "2":
            especialidad = "Pediatría"

        case "3":
            especialidad = "Obstetricia"

        case "4":
            especialidad = "Cirugía General"

        case "5":
            especialidad = "Nutrición"

        case _:
            print("ERROR: Opción de especialidad no válida.")
            return

    medico = Medico(codigo, nombre, especialidad)

    medicos.append(medico)

    print("Médico registrado correctamente.")


# ==========================================
# BUSCAR PACIENTE
# ==========================================

def buscar_paciente():

    print("\n========== BUSCAR PACIENTE ==========")

    codigo = input("Ingrese código del paciente: ")

    for paciente in pacientes:

        if paciente.codigo == codigo:

            print("\nPaciente encontrado:")

            mostrar_resumen(paciente)

            return

    print("ERROR: Paciente no encontrado.")


# ==========================================
# BUSCAR MEDICO
# ==========================================

def buscar_medico():

    print("\n========== BUSCAR MEDICO ==========")

    codigo = input("Ingrese código del médico: ")

    for medico in medicos:

        if medico.codigo == codigo:

            print("\nMédico encontrado:")

            mostrar_resumen(medico)

            return

    print("ERROR: Médico no encontrado.")


# ==========================================
# BUSCAR MEDICOS POR ESPECIALIDAD
# PARADIGMA FUNCIONAL
# ==========================================

# ==========================================
# BUSCAR MEDICOS POR ESPECIALIDAD
# ==========================================

def buscar_por_especialidad():

    print("\n========== ESPECIALIDADES ==========")
    print("1. Medicina General")
    print("2. Pediatría")
    print("3. Obstetricia")
    print("4. Cirugía General")
    print("5. Nutrición")

    opcion_especialidad = input("Seleccione el número de especialidad a buscar: ")

    match opcion_especialidad:

        case "1":
            especialidad = "Medicina General"

        case "2":
            especialidad = "Pediatría"

        case "3":
            especialidad = "Obstetricia"

        case "4":
            especialidad = "Cirugía General"

        case "5":
            especialidad = "Nutrición"

        case _:
            print("ERROR: Opción de especialidad no válida.")
            return

    encontrados = list(
        filter(
            lambda medico: medico.especialidad.lower() == especialidad.lower(),
            medicos
        )
    )

    if len(encontrados) == 0:

        print(f"No existen médicos registrados con la especialidad {especialidad}.")

    else:

        print(f"\nMédicos encontrados ({especialidad}):")

        for medico in encontrados:

            mostrar_resumen(medico)


# ==========================================
# PROGRAMAR CITA
# ==========================================

def programar_cita():

    print("\n========== PROGRAMAR CITA ==========")

    codigo_cita = input("Ingrese código de la cita: ")

    if codigo_cita == "":
        print("ERROR: El código de la cita no puede estar vacío.")
        return

    # ==========================================
    # VERIFICAR CITA DUPLICADA
    # ==========================================

    for cita in citas:

        if cita.codigo == codigo_cita:

            print("ERROR: El código de la cita ya está registrado.")
            return

    # ==========================================
    # BUSCAR PACIENTE
    # ==========================================

    codigo_paciente = input("Ingrese código del paciente: ")

    paciente_encontrado = None

    for paciente in pacientes:

        if paciente.codigo == codigo_paciente:

            paciente_encontrado = paciente
            break

    if paciente_encontrado is None:

        print("ERROR: El paciente no existe.")
        return

    # ==========================================
    # BUSCAR MEDICO
    # ==========================================

    codigo_medico = input("Ingrese código del médico: ")

    medico_encontrado = None

    for medico in medicos:

        if medico.codigo == codigo_medico:

            medico_encontrado = medico
            break

    if medico_encontrado is None:

        print("ERROR: El médico no existe.")
        return

    # ==========================================
    # INGRESAR FECHA
    # ==========================================

    fecha = input(
        "Ingrese fecha y hora de la cita "
        "(DD/MM/AAAA HH:MM): "
    )

    if fecha == "":
        print("ERROR: La fecha no puede estar vacía.")
        return

    # ==========================================
    # EVITAR DOS CITAS DEL MISMO MEDICO
    # ==========================================

    for cita in citas:

        if (
            cita.medico.codigo == codigo_medico
            and cita.fecha == fecha
        ):

            print(
                "ERROR: El médico ya tiene una cita "
                "en esa fecha y hora."
            )

            return

    # ==========================================
    # CREAR CITA
    # ==========================================

    cita = Cita(
        codigo_cita,
        paciente_encontrado,
        medico_encontrado,
        fecha
    )

    citas.append(cita)

    print("Cita registrada correctamente.")


# ==========================================
# BUSCAR CITA
# ==========================================

def buscar_cita():

    print("\n========== BUSCAR CITA ==========")

    codigo = input("Ingrese código de la cita: ")

    for cita in citas:

        if cita.codigo == codigo:

            print("\nCita encontrada:")

            mostrar_resumen(cita)

            return

    print("ERROR: Cita no encontrada.")


# ==========================================
# CANCELAR CITA
# ==========================================

def cancelar_cita():

    print("\n========== CANCELAR CITA ==========")

    codigo = input("Ingrese código de la cita: ")

    for cita in citas:

        if cita.codigo == codigo:

            citas.remove(cita)

            print("Cita cancelada correctamente.")

            return

    print("ERROR: Cita no encontrada.")


# ==========================================
# REGISTRAR ATENCION
# ==========================================

def registrar_atencion():

    print("\n========== REGISTRAR ATENCION ==========")

    codigo_cita = input("Ingrese código de la cita: ")

    cita_encontrada = None

    for cita in citas:

        if cita.codigo == codigo_cita:

            cita_encontrada = cita
            break

    if cita_encontrada is None:

        print("ERROR: La cita no existe.")
        return

    descripcion = input(
        "Ingrese descripción de la atención: "
    )

    if descripcion == "":

        print("ERROR: La descripción no puede estar vacía.")

        return

    atencion = {
        "codigo_cita": cita_encontrada.codigo,
        "paciente": cita_encontrada.paciente.nombre,
        "medico": cita_encontrada.medico.nombre,
        "especialidad": cita_encontrada.medico.especialidad,
        "fecha": cita_encontrada.fecha,
        "descripcion": descripcion
    }

    atenciones.append(atencion)

    print("Atención registrada correctamente.")


# ==========================================
# MOSTRAR HISTORIAL
# ==========================================

def mostrar_historial():

    print("\n========== HISTORIAL DE ATENCIONES ==========")

    codigo_paciente = input(
        "Ingrese código del paciente: "
    )

    encontrados = []

    for atencion in atenciones:

        for paciente in pacientes:

            if (
                paciente.codigo == codigo_paciente
                and paciente.nombre == atencion["paciente"]
            ):

                encontrados.append(atencion)

    if len(encontrados) == 0:

        print("No existen atenciones para este paciente.")

    else:

        for atencion in encontrados:

            print("\n--------------------------------")

            print("Cita:", atencion["codigo_cita"])
            print("Paciente:", atencion["paciente"])
            print("Médico:", atencion["medico"])
            print("Especialidad:", atencion["especialidad"])
            print("Fecha:", atencion["fecha"])
            print("Atención:", atencion["descripcion"])


# ==========================================
# MOSTRAR PACIENTES
# ==========================================

def mostrar_pacientes():

    print("\n========== LISTA DE PACIENTES ==========")

    if len(pacientes) == 0:

        print("No existen pacientes registrados.")

    else:

        print("Total de pacientes:", len(pacientes))

        for paciente in pacientes:

            mostrar_resumen(paciente)


# ==========================================
# MOSTRAR MEDICOS
# ==========================================

def mostrar_medicos():

    print("\n========== LISTA DE MEDICOS ==========")

    if len(medicos) == 0:

        print("No existen médicos registrados.")

    else:

        print("Total de médicos:", len(medicos))

        for medico in medicos:

            mostrar_resumen(medico)


# ==========================================
# MOSTRAR CITAS
# ==========================================

def mostrar_citas():

    print("\n========== LISTA DE CITAS ==========")

    if len(citas) == 0:

        print("No existen citas registradas.")

    else:

        print("Total de citas:", len(citas))

        for cita in citas:

            mostrar_resumen(cita)


# ==========================================
# MENU PRINCIPAL
# ==========================================

while True:

    print("\n========================================")
    print("             SISTEMA KAWSAY")
    print("========================================")

    print("1. Registrar paciente")
    print("2. Registrar médico")
    print("3. Buscar paciente")
    print("4. Buscar médico")
    print("5. Programar cita")
    print("6. Mostrar pacientes")
    print("7. Mostrar médicos")
    print("8. Mostrar citas")
    print("9. Buscar cita")
    print("10. Cancelar cita")
    print("11. Buscar por especialidad")
    print("12. Registrar atención")
    print("13. Mostrar historial")
    print("14. Salir")

    print("========================================")

    opcion = input("Seleccione una opción: ")

    match opcion:

        case "1":
            registrar_paciente()

        case "2":
            registrar_medico()

        case "3":
            buscar_paciente()

        case "4":
            buscar_medico()

        case "5":
            programar_cita()

        case "6":
            mostrar_pacientes()

        case "7":
            mostrar_medicos()

        case "8":
            mostrar_citas()

        case "9":
            buscar_cita()

        case "10":
            cancelar_cita()

        case "11":
            buscar_por_especialidad()

        case "12":
            registrar_atencion()

        case "13":
            mostrar_historial()

        case "14":
            print("Saliendo del sistema...")
            break

        case _:
            print("ERROR: Opción no válida.")
            buscar_por_especialidad