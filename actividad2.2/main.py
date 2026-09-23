# ============================================
# ACTIVIDAD 4: AGENTE RECOLECTOR
# Agentes Inteligentes
# ============================================

# --------------------------------------------
# VARIABLES DEL ENTORNO
# --------------------------------------------

entorno = []

posicion_agente = [0, 0]

puntuacion = 0

paquetes_iniciales = 0
paquetes_recogidos = 0

movimientos = 0
penalizaciones = 0
acciones_realizadas = 0

# Máximo de acciones permitido por la actividad
MAXIMO_ACCIONES = 50


# --------------------------------------------
# FUNCIÓN PARA MOSTRAR EL ENTORNO
# --------------------------------------------

def mostrar_entorno():
    print("\nEstado actual del almacén:")

    for fila in range(len(entorno)):
        fila_mostrar = ""

        for columna in range(len(entorno[fila])):

            if [fila, columna] == posicion_agente:
                fila_mostrar += "A "
            else:
                fila_mostrar += entorno[fila][columna] + " "

        print(fila_mostrar)

    print("Puntuación:", puntuacion)
    print("Paquetes recogidos:", paquetes_recogidos)
    print("Movimientos:", movimientos)
    print("Acciones:", acciones_realizadas)


# --------------------------------------------
# FUNCIÓN PERCIBIR
# --------------------------------------------

def percibir():

    fila = posicion_agente[0]
    columna = posicion_agente[1]

    percepcion = {
        "posicion": (fila, columna),
        "actual": None,
        "arriba": None,
        "abajo": None,
        "izquierda": None,
        "derecha": None
    }

    # Celda actual
    percepcion["actual"] = entorno[fila][columna]

    # Sensor arriba
    if fila - 1 < 0:
        percepcion["arriba"] = "FUERA_DEL_TABLERO"
    else:
        percepcion["arriba"] = entorno[fila - 1][columna]

    # Sensor abajo
    if fila + 1 >= len(entorno):
        percepcion["abajo"] = "FUERA_DEL_TABLERO"
    else:
        percepcion["abajo"] = entorno[fila + 1][columna]

    # Sensor izquierda
    if columna - 1 < 0:
        percepcion["izquierda"] = "FUERA_DEL_TABLERO"
    else:
        percepcion["izquierda"] = entorno[fila][columna - 1]

    # Sensor derecha
    if columna + 1 >= len(entorno[fila]):
        percepcion["derecha"] = "FUERA_DEL_TABLERO"
    else:
        percepcion["derecha"] = entorno[fila][columna + 1]

    return percepcion


# --------------------------------------------
# FUNCIÓN DECIDIR
# --------------------------------------------

def decidir(percepcion):

    # REGLA 1:
    # Si la celda actual contiene un paquete,
    # recogerlo.
    if percepcion["actual"] == "P":
        return "RECOGER"

    # REGLA 2:
    # Buscar primero paquetes en las celdas
    # adyacentes.

    if percepcion["arriba"] == "P":
        return "ARRIBA"

    if percepcion["derecha"] == "P":
        return "DERECHA"

    if percepcion["abajo"] == "P":
        return "ABAJO"

    if percepcion["izquierda"] == "P":
        return "IZQUIERDA"

    # REGLA 3, 4 y 5:
    # Si no hay paquetes cercanos,
    # buscar una celda libre.

    if percepcion["derecha"] == ".":
        return "DERECHA"

    if percepcion["abajo"] == ".":
        return "ABAJO"

    if percepcion["izquierda"] == ".":
        return "IZQUIERDA"

    if percepcion["arriba"] == ".":
        return "ARRIBA"

    # REGLA 7:
    # No existe una acción de movimiento válida.
    return "ESPERAR"


# --------------------------------------------
# FUNCIÓN ACTUAR
# --------------------------------------------

def actuar(accion):

    global puntuacion
    global paquetes_recogidos
    global movimientos
    global penalizaciones
    global acciones_realizadas

    acciones_realizadas += 1

    # ----------------------------------------
    # ACCIÓN RECOGER
    # ----------------------------------------

    if accion == "RECOGER":

        if entorno[posicion_agente[0]][posicion_agente[1]] == "P":

            entorno[posicion_agente[0]][posicion_agente[1]] = "."

            paquetes_recogidos += 1

            puntuacion += 10

            print("\nACCIÓN: RECOGER")
            print("Paquete recogido. +10 puntos")

        return

    # ----------------------------------------
    # ACCIÓN ESPERAR
    # ----------------------------------------

    if accion == "ESPERAR":

        print("\nACCIÓN: ESPERAR")
        print("No existe un movimiento disponible.")

        return

    # ----------------------------------------
    # MOVIMIENTO
    # ----------------------------------------

    fila_actual = posicion_agente[0]
    columna_actual = posicion_agente[1]

    nueva_fila = fila_actual
    nueva_columna = columna_actual

    if accion == "ARRIBA":
        nueva_fila -= 1

    elif accion == "ABAJO":
        nueva_fila += 1

    elif accion == "IZQUIERDA":
        nueva_columna -= 1

    elif accion == "DERECHA":
        nueva_columna += 1

    # ----------------------------------------
    # COMPROBAR LÍMITES
    # ----------------------------------------

    if (
        nueva_fila < 0
        or nueva_fila >= len(entorno)
        or nueva_columna < 0
        or nueva_columna >= len(entorno[0])
    ):

        puntuacion -= 5
        penalizaciones += 5

        print("\nACCIÓN:", accion)
        print("Movimiento fuera del tablero. -5 puntos")

        return

    # ----------------------------------------
    # COMPROBAR OBSTÁCULO
    # ----------------------------------------

    if entorno[nueva_fila][nueva_columna] == "X":

        puntuacion -= 5
        penalizaciones += 5

        print("\nACCIÓN:", accion)
        print("Obstáculo encontrado. -5 puntos")

        return

    # ----------------------------------------
    # REALIZAR MOVIMIENTO
    # ----------------------------------------

    posicion_agente[0] = nueva_fila
    posicion_agente[1] = nueva_columna

    movimientos += 1

    puntuacion -= 1

    print("\nACCIÓN:", accion)
    print("Movimiento realizado. -1 punto")


# --------------------------------------------
# ACTUALIZAR RENDIMIENTO
# --------------------------------------------

def actualizar_rendimiento():

    global puntuacion

    if paquetes_recogidos == paquetes_iniciales:

        puntuacion += 20

        print("\n¡TODOS LOS PAQUETES FUERON RECOGIDOS!")
        print("+20 puntos adicionales")


# --------------------------------------------
# CONTAR PAQUETES
# --------------------------------------------

def contar_paquetes():

    cantidad = 0

    for fila in entorno:

        for celda in fila:

            if celda == "P":
                cantidad += 1

    return cantidad


# --------------------------------------------
# EJECUTAR ESCENARIO
# --------------------------------------------

def ejecutar_escenario(mapa, posicion_inicial):

    global entorno
    global posicion_agente
    global puntuacion
    global paquetes_iniciales
    global paquetes_recogidos
    global movimientos
    global penalizaciones
    global acciones_realizadas

    # Reiniciar datos
    entorno = [fila[:] for fila in mapa]

    posicion_agente = posicion_inicial[:]

    puntuacion = 0
    paquetes_recogidos = 0
    movimientos = 0
    penalizaciones = 0
    acciones_realizadas = 0

    paquetes_iniciales = contar_paquetes()

    print("\n============================================")
    print("INICIO DEL ESCENARIO")
    print("============================================")

    mostrar_entorno()

    # ----------------------------------------
    # CICLO PRINCIPAL DEL AGENTE
    # ----------------------------------------

    while (
        paquetes_recogidos < paquetes_iniciales
        and acciones_realizadas < MAXIMO_ACCIONES
    ):

        # PERCEPCIÓN
        percepcion = percibir()

        print("\nPERCEPCIÓN:")
        print(percepcion)

        # DECISIÓN
        accion = decidir(percepcion)

        print("DECISIÓN:", accion)

        # ACCIÓN
        actuar(accion)

        # Mostrar entorno después de cada acción
        mostrar_entorno()

    # ----------------------------------------
    # BONIFICACIÓN
    # ----------------------------------------

    if paquetes_recogidos == paquetes_iniciales:

        actualizar_rendimiento()

    # ----------------------------------------
    # RESULTADOS
    # ----------------------------------------

    print("\n============================================")
    print("RESULTADOS DEL ESCENARIO")
    print("============================================")

    print("Paquetes iniciales:", paquetes_iniciales)
    print("Paquetes recogidos:", paquetes_recogidos)
    print("Movimientos:", movimientos)
    print("Penalizaciones:", penalizaciones)
    print("Acciones realizadas:", acciones_realizadas)
    print("Puntuación final:", puntuacion)

    return {
        "paquetes": paquetes_recogidos,
        "movimientos": movimientos,
        "penalizaciones": penalizaciones,
        "puntuacion": puntuacion
    }


# ============================================
# ESCENARIO 1
# ============================================

escenario_1 = [
    [".", ".", ".", "P", "."],
    [".", "X", ".", ".", "."],
    [".", ".", ".", "X", "P"],
    [".", ".", "P", ".", "."],
    [".", "X", ".", ".", "."]
]

resultado_1 = ejecutar_escenario(
    escenario_1,
    [2, 0]
)


# ============================================
# ESCENARIO 2
# ============================================

escenario_2 = [
    ["P", ".", "X", ".", "."],
    [".", ".", "X", ".", "P"],
    [".", ".", "A", ".", "."],
    ["X", ".", ".", ".", "."],
    ["P", ".", "X", ".", "."]
]

resultado_2 = ejecutar_escenario(
    escenario_2,
    [2, 2]
)


# ============================================
# ESCENARIO 3
# ============================================

escenario_3 = [
    [".", "X", ".", ".", "P"],
    [".", "X", ".", "X", "."],
    [".", ".", "A", ".", "."],
    ["P", "X", ".", "X", "."],
    [".", ".", ".", ".", "P"]
]

resultado_3 = ejecutar_escenario(
    escenario_3,
    [2, 2]
)


# ============================================
# RESUMEN FINAL
# ============================================

print("\n\n============================================")
print("RESUMEN DE LOS TRES ESCENARIOS")
print("============================================")

print("\nEscenario | Paquetes | Movimientos | Penalizaciones | Puntuación")

print(
    "1         |",
    resultado_1["paquetes"],
    "       |",
    resultado_1["movimientos"],
    "          |",
    resultado_1["penalizaciones"],
    "             |",
    resultado_1["puntuacion"]
)

print(
    "2         |",
    resultado_2["paquetes"],
    "       |",
    resultado_2["movimientos"],
    "          |",
    resultado_2["penalizaciones"],
    "             |",
    resultado_2["puntuacion"]
)

print(
    "3         |",
    resultado_3["paquetes"],
    "       |",
    resultado_3["movimientos"],
    "          |",
    resultado_3["penalizaciones"],
    "             |",
    resultado_3["puntuacion"]
)