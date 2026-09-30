from paciente import Paciente
from medico import Medico, seleccionar_especialidad
from cita import Cita
from datetime import datetime

pacientes = []
medicos = []
citas = []
atenciones = []

# ==========================================
# PEDIR CODIGO
# ==========================================
def pedir_codigo(mensaje):
    while True:
        codigo = input(mensaje)
        if codigo.isdigit():
            return codigo
        print("ERROR: El código debe contener solo números.")

# ==========================================
# PEDIR NOMBRE
# ==========================================
def pedir_nombre(mensaje):
    while True:
        nombre = input(mensaje)
        if nombre.replace(" ", "").isalpha():
            return nombre
        print("ERROR: El nombre debe contener solo letras.")

# ==========================================
# PEDIR EDAD
# ==========================================
def pedir_edad():
    while True:
        try:
            edad = int(input("Edad: "))
            if edad < 0 or edad > 120:
                print("ERROR: La edad debe estar entre 0 y 120.")
                continue
            return edad
        except ValueError:
            print("ERROR: La edad debe contener solo números.")

# ==========================================
# INGRESAR FECHA
# ==========================================
def ingresar_fecha():
    while True:
        fecha = input("Ingrese fecha y hora: ")
        try:
            datetime.strptime(fecha, "%d/%m/%Y %H:%M")
            return fecha
        except ValueError:
            print("ERROR: Fecha no válida.")
            print("Ejemplo: 25/10/2026 14:30")

# ==========================================
# REGISTRAR PACIENTE
# ==========================================
def registrar_paciente():
    print("\n=== REGISTRAR PACIENTE ===")
    while True:
        codigo = pedir_codigo("Código: ")
        repetido = False
        for paciente in pacientes:
            if paciente.codigo == codigo:
                repetido = True
        if repetido:
            print("ERROR: El código ya existe.")
        else:
            break

    nombre = pedir_nombre("Nombre: ")
    edad = pedir_edad()

    try:
        paciente = Paciente(codigo, nombre, edad)
        pacientes.append(paciente)
        print("Paciente registrado correctamente.")
    except ValueError as error:
        print("ERROR:", error)

# ==========================================
# REGISTRAR MEDICO
# ==========================================
def registrar_medico():
    print("\n=== REGISTRAR MEDICO ===")
    while True:
        codigo = pedir_codigo("Código: ")
        repetido = False
        for medico in medicos:
            if medico.codigo == codigo:
                repetido = True
        if repetido:
            print("ERROR: El código ya existe.")
        else:
            break

    nombre = pedir_nombre("Nombre: ")
    especialidad = seleccionar_especialidad()

    try:
        medico = Medico(codigo, nombre, especialidad)
        medicos.append(medico)
        print("Médico registrado correctamente.")
    except ValueError as error:
        print("ERROR:", error)

# ==========================================
# PROGRAMAR CITA
# ==========================================
def programar_cita():
    print("\n=== PROGRAMAR CITA ===")

    # CODIGO DE LA CITA
    while True:
        codigo = pedir_codigo("Código de la cita (0 para cancelar): ")
        if codigo == "0":
            print("Programación de cita cancelada.")
            return

        repetido = False
        for cita in citas:
            if cita.codigo == codigo:
                repetido = True

        if repetido:
            print("ERROR: El código de la cita ya existe.")
        else:
            break

    # BUSCAR PACIENTE
    while True:
        codigo_paciente = pedir_codigo("Código del paciente (0 para cancelar): ")
        if codigo_paciente == "0":
            print("Programación de cita cancelada.")
            return

        paciente_encontrado = None
        for paciente in pacientes:
            if paciente.codigo == codigo_paciente:
                paciente_encontrado = paciente

        if paciente_encontrado is None:
            print("ERROR: El paciente no existe.")
        else:
            break

    # BUSCAR MEDICO
    while True:
        codigo_medico = pedir_codigo("Código del médico (0 para cancelar): ")
        if codigo_medico == "0":
            print("Programación de cita cancelada.")
            return

        medico_encontrado = None
        for medico in medicos:
            if medico.codigo == codigo_medico:
                medico_encontrado = medico

        if medico_encontrado is None:
            print("ERROR: El médico no existe.")
        else:
            break

    # INGRESAR FECHA
    fecha = ingresar_fecha()

    # VERIFICAR HORARIO DEL MEDICO
    for cita in citas:
        if cita.medico.codigo == codigo_medico and cita.fecha == fecha:
            print("ERROR: El médico ya tiene una cita en ese horario.")
            return

    # CREAR CITA
    try:
        cita = Cita(codigo, paciente_encontrado, medico_encontrado, fecha)
        citas.append(cita)
        print("Cita registrada correctamente.")
    except ValueError as error:
        print("ERROR:", error)

# ==========================================
# MOSTRAR PACIENTES
# ==========================================
def mostrar_pacientes():
    print("\n=== PACIENTES ===")
    if len(pacientes) == 0:
        print("No hay pacientes.")
        return
    for paciente in pacientes:
        print(paciente.resumen())

# ==========================================
# MOSTRAR MEDICOS
# ==========================================
def mostrar_medicos():
    print("\n=== MEDICOS ===")
    if len(medicos) == 0:
        print("No hay médicos.")
        return
    for medico in medicos:
        print(medico.resumen())

# ==========================================
# MOSTRAR CITAS
# ==========================================
def mostrar_citas():
    print("\n=== CITAS ===")
    if len(citas) == 0:
        print("No hay citas.")
        return
    for cita in citas:
        print(cita.resumen())

# ==========================================
# CONSULTAS
# ==========================================
def consultas():
    while True:
        print("\n=== CONSULTAS ===")
        print("1. Mostrar pacientes")
        print("2. Mostrar médicos")
        print("3. Mostrar citas")
        print("4. Volver")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_pacientes()
        elif opcion == "2":
            mostrar_medicos()
        elif opcion == "3":
            mostrar_citas()
        elif opcion == "4":
            break
        else:
            print("ERROR: Opción no válida.")

# ==========================================
# REGISTRAR ATENCION
# ==========================================
def registrar_atencion():
    print("\n=== REGISTRAR ATENCION ===")

    while True:
        codigo = pedir_codigo("Código de la cita (0 para cancelar): ")
        if codigo == "0":
            print("Registro de atención cancelado.")
            return

        cita_encontrada = None
        for cita in citas:
            if cita.codigo == codigo:
                cita_encontrada = cita

        if cita_encontrada is None:
            print("ERROR: La cita no existe.")
        else:
            break

    # DESCRIPCION
    while True:
        descripcion = input("Descripción: ")
        if descripcion != "":
            break
        print("ERROR: La descripción no puede estar vacía.")

    # GUARDAR ATENCION
    atencion = {
        "cita": cita_encontrada.codigo,
        "codigo_paciente": cita_encontrada.paciente.codigo,
        "paciente": cita_encontrada.paciente.nombre,
        "medico": cita_encontrada.medico.nombre,
        "especialidad": cita_encontrada.medico.especialidad,
        "descripcion": descripcion
    }

    atenciones.append(atencion)
    print("Atención registrada correctamente.")

# ==========================================
# MOSTRAR HISTORIAL
# ==========================================
def mostrar_historial():
    print("\n=== HISTORIAL ===")

    while True:
        codigo_paciente = pedir_codigo("Código del paciente (0 para cancelar): ")
        if codigo_paciente == "0":
            print("Consulta cancelada.")
            return

        paciente_encontrado = None
        for paciente in pacientes:
            if paciente.codigo == codigo_paciente:
                paciente_encontrado = paciente

        if paciente_encontrado is None:
            print("ERROR: El paciente no existe.")
        else:
            break

    encontrado = False
    for atencion in atenciones:
        if atencion["codigo_paciente"] == codigo_paciente:
            print("\n----------------------")
            print("Cita:", atencion["cita"])
            print("Paciente:", atencion["paciente"])
            print("Médico:", atencion["medico"])
            print("Especialidad:", atencion["especialidad"])
            print("Atención:", atencion["descripcion"])
            encontrado = True

    if not encontrado:
        print("No hay atenciones para este paciente.")

# ==========================================
# MENU PRINCIPAL
# ==========================================
while True:
    print("\n==========================")
    print("      SISTEMA KAWSAY")
    print("==========================")
    print("1. Registrar paciente")
    print("2. Registrar médico")
    print("3. Programar cita")
    print("4. Consultas")
    print("5. Registrar atención")
    print("6. Mostrar historial")
    print("7. Salir")

    opcion = input("Seleccione una opción: ")

    match opcion:
        case "1":
            registrar_paciente()
        case "2":
            registrar_medico()
        case "3":
            programar_cita()
        case "4":
            consultas()
        case "5":
            registrar_atencion()
        case "6":
            mostrar_historial()
        case "7":
            print("Saliendo del sistema...")
            break
        case _:
            print("ERROR: Opción no válida.")
