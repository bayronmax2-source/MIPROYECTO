from paciente import Paciente
from medico import Medico
from cita import Cita
from datetime import datetime

pacientes = []
medicos = []
citas = []
atenciones = []

def mostrar_resumen(objeto):
    print(objeto.resumen())

def seleccionar_especialidad():
    print("\n========== ESPECIALIDADES ==========")
    print("1. Medicina General")
    print("2. Pediatría")
    print("3. Obstetricia")
    print("4. Cirugía General")
    print("5. Nutrición")

    opcion = input("Seleccione una opción (1-5): ")

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
            print("ERROR: Debe seleccionar una opción del 1 al 5.")
            return None

def ingresar_fecha():
    while True:
        fecha = input(
            "\nIngrese fecha y hora "
            "(ejemplo: 25/10/2026 14:30): "
        ).strip()

        if fecha == "":
            print("ERROR: La fecha no puede estar vacía.")
            continue

        partes = fecha.split(" ")

        if len(partes) != 2:
            print(
                "ERROR: El formato debe ser DD/MM/AAAA HH:MM."
            )
            continue

        fecha_parte = partes[0]
        hora_parte = partes[1]

        datos_fecha = fecha_parte.split("/")

        if len(datos_fecha) != 3:
            print(
                "ERROR: La fecha debe tener el formato DD/MM/AAAA."
            )
            continue

        dia = datos_fecha[0]
        mes = datos_fecha[1]
        anio = datos_fecha[2]

        if not dia.isdigit():
            print("ERROR: El día debe contener solo números.")
            continue

        if not mes.isdigit():
            print("ERROR: El mes debe contener solo números.")
            continue

        if not anio.isdigit():
            print("ERROR: El año debe contener solo números.")
            continue

        if len(dia) != 2:
            print("ERROR: El día debe tener 2 dígitos.")
            continue

        if len(mes) != 2:
            print("ERROR: El mes debe tener 2 dígitos.")
            continue

        if len(anio) != 4:
            print("ERROR: El año debe tener 4 dígitos.")
            continue

        datos_hora = hora_parte.split(":")

        if len(datos_hora) != 2:
            print(
                "ERROR: La hora debe tener el formato HH:MM."
            )
            continue

        hora = datos_hora[0]
        minutos = datos_hora[1]

        if not hora.isdigit():
            print("ERROR: La hora debe contener solo números.")
            continue

        if not minutos.isdigit():
            print("ERROR: Los minutos deben contener solo números.")
            continue

        if len(hora) != 2:
            print("ERROR: La hora debe tener 2 dígitos.")
            continue

        if len(minutos) != 2:
            print("ERROR: Los minutos deben tener 2 dígitos.")
            continue

        try:
            datetime.strptime(
                fecha,
                "%d/%m/%Y %H:%M"
            )
        except ValueError:
            print(
                "ERROR: La fecha u hora no es válida. "
                "Revise los valores ingresados."
            )
            continue

        return fecha

def registrar_paciente():
    print("\n========== REGISTRAR PACIENTE ==========")

    codigo = input(
        "Ingrese código del paciente (ejemplo: P001): "
    ).strip()

    if codigo == "":
        print("ERROR: El código no puede estar vacío.")
        return

    for paciente in pacientes:
        if paciente.codigo == codigo:
            print("ERROR: El código del paciente ya está registrado.")
            return

    nombre = input(
        "Ingrese nombre del paciente (ejemplo: Juan Pérez): "
    ).strip()

    if nombre == "":
        print("ERROR: El nombre no puede estar vacío.")
        return

    while True:
        edad_texto = input(
            "Ingrese edad del paciente (ejemplo: 25): "
        ).strip()

        if edad_texto == "":
            print("ERROR: La edad no puede estar vacía.")
            continue

        if not edad_texto.isdigit():
            print("ERROR: La edad debe contener solo números.")
            continue

        edad = int(edad_texto)

        if edad < 0 or edad > 120:
            print("ERROR: La edad debe estar entre 0 y 120.")
            continue

        break

    pacientes.append(
        Paciente(codigo, nombre, edad)
    )

    print("Paciente registrado correctamente.")

def registrar_medico():
    print("\n========== REGISTRAR MÉDICO ==========")

    codigo = input(
        "Ingrese código del médico (ejemplo: M001): "
    ).strip()

    if codigo == "":
        print("ERROR: El código no puede estar vacío.")
        return

    for medico in medicos:
        if medico.codigo == codigo:
            print("ERROR: El código del médico ya está registrado.")
            return

    nombre = input(
        "Ingrese nombre del médico (ejemplo: Ana Torres): "
    ).strip()

    if nombre == "":
        print("ERROR: El nombre no puede estar vacío.")
        return

    especialidad = seleccionar_especialidad()

    if especialidad is None:
        return

    medicos.append(
        Medico(codigo, nombre, especialidad)
    )

    print("Médico registrado correctamente.")

def buscar_paciente():
    print("\n========== BUSCAR PACIENTE ==========")

    codigo = input(
        "Ingrese código del paciente (ejemplo: P001): "
    ).strip()

    for paciente in pacientes:
        if paciente.codigo == codigo:
            print("\nPaciente encontrado:")
            mostrar_resumen(paciente)
            return

    print("ERROR: Paciente no encontrado.")

def buscar_medico():
    print("\n========== BUSCAR MÉDICO ==========")

    codigo = input(
        "Ingrese código del médico (ejemplo: M001): "
    ).strip()

    for medico in medicos:
        if medico.codigo == codigo:
            print("\nMédico encontrado:")
            mostrar_resumen(medico)
            return

    print("ERROR: Médico no encontrado.")

def buscar_por_especialidad():
    print("\n========== BUSCAR POR ESPECIALIDAD ==========")

    especialidad = seleccionar_especialidad()

    if especialidad is None:
        return

    encontrados = list(
        filter(
            lambda medico:
            medico.especialidad.lower() == especialidad.lower(),
            medicos
        )
    )

    if len(encontrados) == 0:
        print(
            f"No existen médicos registrados con "
            f"la especialidad {especialidad}."
        )
    else:
        print(
            f"\nMédicos encontrados: {especialidad}"
        )
        for medico in encontrados:
            mostrar_resumen(medico)

def programar_cita():
    print("\n========== PROGRAMAR CITA ==========")

    codigo_cita = input(
        "Ingrese código de la cita (ejemplo: C001): "
    ).strip()

    if codigo_cita == "":
        print("ERROR: El código de la cita no puede estar vacío.")
        return

    for cita in citas:
        if cita.codigo == codigo_cita:
            print("ERROR: El código de la cita ya está registrado.")
            return

    codigo_paciente = input(
        "Ingrese código del paciente (ejemplo: P001): "
    ).strip()

    paciente_encontrado = None

    for paciente in pacientes:
        if paciente.codigo == codigo_paciente:
            paciente_encontrado = paciente
            break

    if paciente_encontrado is None:
        print("ERROR: El paciente no existe.")
        return

    codigo_medico = input(
        "Ingrese código del médico (ejemplo: M001): "
    ).strip()

    medico_encontrado = None

    for medico in medicos:
        if medico.codigo == codigo_medico:
            medico_encontrado = medico
            break

    if medico_encontrado is None:
        print("ERROR: El médico no existe.")
        return

    fecha = ingresar_fecha()

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

    citas.append(
        Cita(
            codigo_cita,
            paciente_encontrado,
            medico_encontrado,
            fecha
        )
    )

    print("Cita registrada correctamente.")

def buscar_cita():
    print("\n========== BUSCAR CITA ==========")

    codigo = input(
        "Ingrese código de la cita (ejemplo: C001): "
    ).strip()

    for cita in citas:
        if cita.codigo == codigo:
            print("\nCita encontrada:")
            mostrar_resumen(cita)
            return

    print("ERROR: Cita no encontrada.")

def cancelar_cita():
    print("\n========== CANCELAR CITA ==========")

    codigo = input(
        "Ingrese código de la cita (ejemplo: C001): "
    ).strip()

    for cita in citas:
        if cita.codigo == codigo:
            citas.remove(cita)
            print("Cita cancelada correctamente.")
            return

    print("ERROR: Cita no encontrada.")

def registrar_atencion():
    print("\n========== REGISTRAR ATENCIÓN ==========")

    codigo_cita = input(
        "Ingrese código de la cita (ejemplo: C001): "
    ).strip()

    cita_encontrada = None

    for cita in citas:
        if cita.codigo == codigo_cita:
            cita_encontrada = cita
            break

    if cita_encontrada is None:
        print("ERROR: La cita no existe.")
        return

    descripcion = input(
        "Ingrese descripción de la atención "
        "(ejemplo: Control general): "
    ).strip()

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

def mostrar_historial():
    print("\n========== HISTORIAL DE ATENCIONES ==========")

    codigo_paciente = input(
        "Ingrese código del paciente (ejemplo: P001): "
    ).strip()

    paciente_encontrado = None

    for paciente in pacientes:
        if paciente.codigo == codigo_paciente:
            paciente_encontrado = paciente
            break

    if paciente_encontrado is None:
        print("ERROR: El paciente no existe.")
        return

    encontrados = []

    for atencion in atenciones:
        if atencion["paciente"] == paciente_encontrado.nombre:
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

def mostrar_pacientes():
    print("\n========== LISTA DE PACIENTES ==========")

    if len(pacientes) == 0:
        print("No existen pacientes registrados.")
    else:
        print("Total de pacientes:", len(pacientes))
        for paciente in pacientes:
            mostrar_resumen(paciente)

def mostrar_medicos():
    print("\n========== LISTA DE MÉDICOS ==========")

    if len(medicos) == 0:
        print("No existen médicos registrados.")
    else:
        print("Total de médicos:", len(medicos))
        for medico in medicos:
            mostrar_resumen(medico)

def mostrar_citas():
    print("\n========== LISTA DE CITAS ==========")

    if len(citas) == 0:
        print("No existen citas registradas.")
    else:
        print("Total de citas:", len(citas))
        for cita in citas:
            mostrar_resumen(cita)

while True:
    print("\n========================================")
    print("           SISTEMA KAWSAY")
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

    opcion = input(
        "Seleccione una opción (1-14): "
    ).strip()

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
            print(
                "ERROR: Opción no válida. "
                "Debe seleccionar un número del 1 al 14."
            )