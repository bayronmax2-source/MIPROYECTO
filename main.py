print("==============================")
print(" SISTEMA DE VALIDACION")
print("==============================")
# ==========================================
# VALIDACION DEL DNI
# ==========================================
def validar_vacio_dni(dni):

    if dni == "":
        print("ERROR: No ingresaste ningún DNI.")
        return False

    return True

def validar_espacios_dni(dni):

    if dni != dni.strip():
        print("ERROR: El DNI no debe tener espacios.")
        return False

    return True


def validar_numeros_dni(dni):

    if not dni.isdigit():
        print("ERROR: El DNI solo debe contener números.")
        return False

    return True


def validar_cantidad_dni(dni):

    if len(dni) != 8:
        print("ERROR: El DNI debe tener exactamente 8 dígitos.")
        return False

    return True


def validar_dni(dni):

    if not validar_vacio_dni(dni):
        return False

    if not validar_espacios_dni(dni):
        return False

    if not validar_numeros_dni(dni):
        return False

    if not validar_cantidad_dni(dni):
        return False

    return True


# ==========================================
# VALIDACION DEL RUC
# ==========================================

def validacion_digitos_ruc(ruc):

    if len(ruc) != 11:
        print("ERROR: El RUC debe tener 11 dígitos.")
        return False

    return True


def validacion_espacios_ruc(ruc):

    if " " in ruc:
        print("ERROR: El RUC no debe tener espacios.")
        return False

    return True


def validacion_numeros_ruc(ruc):

    if not ruc.isdigit():
        print("ERROR: El RUC solo debe tener números.")
        return False

    return True


def validacion_prefijo_ruc(ruc):

    if ruc.startswith(("10", "15", "16", "17", "20")):
        return True
    else:
        print("ERROR: El RUC no tiene un prefijo válido.")
        return False


def validacion_modulo_11(ruc):

    suma = 0

    pesos = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2]

    for i in range(10):

        suma = suma + int(ruc[i]) * pesos[i]

    residuo = suma % 11
    resultado = 11 - residuo

    if resultado == 10:
        digito_verificador = 0

    elif resultado == 11:
        digito_verificador = 1

    else:
        digito_verificador = resultado

    if int(ruc[10]) == digito_verificador:
        return True

    else:
        print("ERROR: El RUC no es válido según el módulo 11.")
        return False


def validar_ruc(ruc):

    if not validacion_digitos_ruc(ruc):
        return False

    if not validacion_espacios_ruc(ruc):
        return False

    if not validacion_numeros_ruc(ruc):
        return False

    if not validacion_prefijo_ruc(ruc):
        return False

    if not validacion_modulo_11(ruc):
        return False

    return True


# ==========================================
# VALIDACION DE LA ESTRUCTURA DEL XML
# ==========================================

def validar_inicio_xml(xml):

    if not xml.startswith("<persona>"):
        print("ERROR XML: Debe comenzar con <persona>.")
        return False

    return True


def validar_nombre_xml(xml):

    if "<nombre>" not in xml:
        print("ERROR XML: Falta el campo <nombre>.")
        return False

    if "</nombre>" not in xml:
        print("ERROR XML: Falta </nombre>.")
        return False

    return True


def validar_dni_xml(xml):

    if "<dni>" not in xml:
        print("ERROR XML: Falta el campo <dni>.")
        return False

    if "</dni>" not in xml:
        print("ERROR XML: Falta </dni>.")
        return False

    return True


def validar_ruc_xml(xml):

    if "<ruc>" not in xml:
        print("ERROR XML: Falta el campo <ruc>.")
        return False

    if "</ruc>" not in xml:
        print("ERROR XML: Falta </ruc>.")
        return False

    return True


def validar_fin_xml(xml):

    if not xml.endswith("</persona>"):
        print("ERROR XML: Debe terminar con </persona>.")
        return False

    return True


# ==========================================
# VERIFICAR QUE EL XML TENGA LOS DATOS
# CORRECTOS DEL DNI Y RUC
# ==========================================

def verificar_datos_xml(xml, nombre, dni, ruc):

    xml_correcto = (
        "<persona>"
        "<nombre>" + nombre + "</nombre>"
        "<dni>" + dni + "</dni>"
        "<ruc>" + ruc + "</ruc>"
        "</persona>"
    )

    if xml != xml_correcto:

        print("\n==============================")
        print("ERRORES EN LOS DATOS DEL XML")
        print("==============================")

        xml_dni_correcto = "<dni>" + dni + "</dni>"
        xml_ruc_correcto = "<ruc>" + ruc + "</ruc>"
        xml_nombre_correcto = "<nombre>" + nombre + "</nombre>"

        if xml_nombre_correcto not in xml:
            print("ERROR: El nombre del XML no coincide con el ingresado.")

        if xml_dni_correcto not in xml:
            print("ERROR: El DNI del XML no coincide con el DNI ingresado.")

        if xml_ruc_correcto not in xml:
            print("ERROR: El RUC del XML no coincide con el RUC ingresado.")

        return False

    return True


# ==========================================
# PROGRAMA PRINCIPAL
# ==========================================

print("\n==============================")
print("INGRESO DE DATOS")
print("==============================")

nombre = input("Ingrese su nombre: ")
dni = input("Ingrese su DNI: ")
ruc = input("Ingrese su RUC: ")


# ------------------------------------------
# VALIDAR DNI
# ------------------------------------------

print("\n==============================")
print("VALIDANDO DNI")
print("==============================")

dni_correcto = validar_dni(dni)

if dni_correcto:
    print("DNI válido.")


# ------------------------------------------
# VALIDAR RUC
# ------------------------------------------

print("\n==============================")
print("VALIDANDO RUC")
print("==============================")

ruc_correcto = validar_ruc(ruc)

if ruc_correcto:
    print("RUC válido.")


# ------------------------------------------
# SOLICITAR XML
# ------------------------------------------

print("\n==============================")
print("VALIDACION DEL XML")
print("==============================")

print("Ejemplo de XML:")
print("<persona><nombre>Bayron</nombre><dni>12345678</dni><ruc>10123456789</ruc></persona>")

xml = input("\nIngrese el XML: ")


# ------------------------------------------
# VALIDAR ESTRUCTURA DEL XML
# ------------------------------------------

xml_correcto = True

if not validar_inicio_xml(xml):
    xml_correcto = False

if not validar_nombre_xml(xml):
    xml_correcto = False

if not validar_dni_xml(xml):
    xml_correcto = False

if not validar_ruc_xml(xml):
    xml_correcto = False

if not validar_fin_xml(xml):
    xml_correcto = False


# ------------------------------------------
# VERIFICAR DATOS DEL XML
# ------------------------------------------

datos_xml_correctos = False

if xml_correcto:

    datos_xml_correctos = verificar_datos_xml(
        xml,
        nombre,
        dni,
        ruc
    )


# ==========================================
# RESULTADO FINAL
# ==========================================

print("\n==============================")
print("       RESULTADO FINAL")
print("==============================")

print("Nombre ingresado :", nombre)
print("DNI ingresado    :", dni)
print("RUC ingresado    :", ruc)
print("XML ingresado    :", xml)

print("\n------------------------------")

if dni_correcto:
    print("DNI: CORRECTO")
else:
    print("DNI: INCORRECTO")

if ruc_correcto:
    print("RUC: CORRECTO")
else:
    print("RUC: INCORRECTO")

if xml_correcto and datos_xml_correctos:
    print("XML: CORRECTO")
else:
    print("XML: INCORRECTO")


if dni_correcto and ruc_correcto and xml_correcto and datos_xml_correctos:

    print("\n==============================")
    print("VALIDACION COMPLETADA")
    print("TODOS LOS DATOS SON CORRECTOS")
    print("==============================")

else:

    print("\n==============================")
    print("VALIDACION RECHAZADA")
    print("EXISTEN DATOS INCORRECTOS")
    print("==============================")