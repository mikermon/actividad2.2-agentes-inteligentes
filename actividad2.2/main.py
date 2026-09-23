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

# Memoria del agente
posiciones_visitadas = set()

# Camino utilizado por el agente.
# Se utiliza para regresar cuando llega
# a un callejón sin salida.
camino_agente = []

# --------------------------------------------
# FUNCIÓN PARA MOSTRAR EL ENTORNO
# --------------------------------------------
def mostrar_entorno():

    print("\nEstado actual del almacén:")

    for fila in range(len(entorno)):

        fila_mostrar = ""

        for columna in range(len(entorno[fila])):

            # La posición del agente se muestra
            # automáticamente.
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
# FUNCIÓN PARA OBTENER POSICIÓN SEGÚN ACCIÓN
# --------------------------------------------
def obtener_nueva_posicion(accion):

    fila = posicion_agente[0]
    columna = posicion_agente[1]

    if accion == "ARRIBA":
        return fila - 1, columna

    elif accion == "ABAJO":
        return fila + 1, columna

    elif accion == "IZQUIERDA":
        return fila, columna - 1

    elif accion == "DERECHA":
        return fila, columna + 1

    return fila, columna
# --------------------------------------------
# FUNCIÓN DECIDIR
# --------------------------------------------
def decidir(percepcion):

    # ----------------------------------------
    # REGLA 1:
    # ----------------------------------------
    if percepcion["actual"] == "P":
        return "RECOGER"
    # ----------------------------------------
    # REGLA 2:
    # ----------------------------------------
    if percepcion["arriba"] == "P":
        return "ARRIBA"

    if percepcion["derecha"] == "P":
        return "DERECHA"

    if percepcion["abajo"] == "P":
        return "ABAJO"

    if percepcion["izquierda"] == "P":
        return "IZQUIERDA"
    # ----------------------------------------
    # REGLA 3:
    # ----------------------------------------
    direcciones = [
        ("ARRIBA", percepcion["arriba"]),
        ("DERECHA", percepcion["derecha"]),
        ("ABAJO", percepcion["abajo"]),
        ("IZQUIERDA", percepcion["izquierda"])
    ]

    for direccion, contenido in direcciones:

        if contenido != ".":
            continue

        nueva_fila, nueva_columna = obtener_nueva_posicion(direccion)

        nueva_posicion = (
            nueva_fila,
            nueva_columna
        )

        # Si todavía no visitamos esta posición,
        # podemos explorarla.
        if nueva_posicion not in posiciones_visitadas:
            return direccion
    # ----------------------------------------
    # REGLA 5:
    # ----------------------------------------
    if camino_agente:

        posicion_anterior = camino_agente[-1]

        fila_actual = posicion_agente[0]
        columna_actual = posicion_agente[1]

        fila_anterior = posicion_anterior[0]
        columna_anterior = posicion_anterior[1]

        diferencia_fila = fila_anterior - fila_actual
        diferencia_columna = columna_anterior - columna_actual

        if diferencia_fila == -1:
            return "ARRIBA"

        elif diferencia_fila == 1:
            return "ABAJO"

        elif diferencia_columna == -1:
            return "IZQUIERDA"

        elif diferencia_columna == 1:
            return "DERECHA"

# --------------------------------------------
# FUNCIÓN ACTUAR
# --------------------------------------------

def actuar(accion):

    global puntuacion
    global paquetes_recogidos
    global movimientos
    global penalizaciones
    global acciones_realizadas
    global camino_agente

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
    # COMPROBAR LÍMITES regla 4
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
    # COMPROBAR OBSTÁCULO regla4
    # ----------------------------------------
    if entorno[nueva_fila][nueva_columna] == "X":

        puntuacion -= 5
        penalizaciones += 5

        print("\nACCIÓN:", accion)
        print("Obstáculo encontrado. -5 puntos")

        return
    # ----------------------------------------
    # COMPROBAR SI ES RETROCESO
    # ----------------------------------------

    posicion_nueva = (
        nueva_fila,
        nueva_columna
    )

    es_retroceso = False

    if camino_agente:

        posicion_anterior = camino_agente[-1]

        if posicion_nueva == posicion_anterior:
            es_retroceso = True

    # ----------------------------------------
    # GUARDAR CAMINO
    # ----------------------------------------

    posicion_actual = (
        posicion_agente[0],
        posicion_agente[1]
    )

    if es_retroceso:

        # Estamos regresando al punto anterior,
        # por lo tanto quitamos la posición actual
        # de la pila del camino.
        camino_agente.pop()

    else:

        # Estamos explorando una posición nueva,
        # así que guardamos de dónde venimos.
        camino_agente.append(posicion_actual)

    # ----------------------------------------
    # REALIZAR MOVIMIENTO
    # ----------------------------------------

    posicion_agente[0] = nueva_fila
    posicion_agente[1] = nueva_columna

    movimientos += 1

    puntuacion -= 1

    # Registrar posición visitada
    posiciones_visitadas.add(posicion_nueva)

    print("\nACCIÓN:", accion)

    if es_retroceso:
        print("Retroceso realizado. -1 punto")
    else:
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
    global posiciones_visitadas
    global camino_agente
    # ----------------------------------------
    # REINICIAR DATOS
    # ----------------------------------------
    entorno = [fila[:] for fila in mapa]

    posicion_agente = posicion_inicial[:]

    puntuacion = 0
    paquetes_recogidos = 0
    movimientos = 0
    penalizaciones = 0
    acciones_realizadas = 0

    # Reiniciar memoria
    posiciones_visitadas = set()

    # Reiniciar camino
    camino_agente = []

    # Registrar posición inicial
    posiciones_visitadas.add(
        tuple(posicion_agente)
    )

    paquetes_iniciales = contar_paquetes()

    # ----------------------------------------
    # MOSTRAR ESCENARIO
    # ----------------------------------------

    print("\n============================================")
    print("INICIO DEL ESCENARIO")
    print("============================================")

    mostrar_entorno()
    # ----------------------------------------
    # CICLO PRINCIPAL
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

        # MOSTRAR ENTORNO
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

# ============================================
# ESCENARIOS
# ============================================
escenario_1 = [
    [".", ".", ".", "P", "."],
    [".", "X", ".", ".", "."],
    [".", ".", ".", "X", "P"],
    [".", ".", "P", ".", "."],
    [".", "X", ".", ".", "."]
]
escenario_2 = [
    ["P", ".", "X", ".", "."],
    [".", ".", "X", ".", "P"],
    [".", ".", ".", ".", "."],
    ["X", ".", ".", ".", "."],
    ["P", ".", "X", ".", "."]
]
escenario_3 = [
    [".", "X", ".", ".", "P"],
    [".", "X", ".", "X", "."],
    [".", ".", ".", ".", "."],
    ["P", "X", ".", "X", "."],
    [".", ".", ".", ".", "P"]
]

# ============================================
# SELECCIÓN DEL ESCENARIO
# ============================================
print("\n============================================")
print("       AGENTE RECOLECTOR")
print("============================================")
print("\nSelecciona el escenario que deseas ejecutar:")
print("1. Escenario 1")
print("2. Escenario 2")
print("3. Escenario 3")

while True:
    opcion = input("\nIngresa el número del escenario: ")
    if opcion == "1":
        print("\nHas seleccionado el ESCENARIO 1")

        ejecutar_escenario(
            escenario_1,
            [2, 0]
        )
        break
    elif opcion == "2":

        print("\nHas seleccionado el ESCENARIO 2")

        ejecutar_escenario(
            escenario_2,
            [2, 2]
        )
        break
    elif opcion == "3":
        print("\nHas seleccionado el ESCENARIO 3")
        ejecutar_escenario(
            escenario_3,
            [2, 2]
        )
        break
    else:
        print("Opción no válida.")
        print("Selecciona 1, 2 o 3.")