#matriz
entorno1 = [
 [".", ".", ".", "P", "."],
 [".", "X", ".", ".", "."],
 ["A", ".", ".", "X", "P"],
 [".", ".", "P", ".", "."],
 [".", "X", ".", ".", "."]
]
entorno2 = [
 ["P", ".", "X", ".", "."],
 [".", ".", "X", ".", "P"],
 [".", ".", "A", ".", "."],
 ["X", ".", ".", ".", "."],
 ["P", ".", "X", ".", "."]
]
entorno3 = [
 [".", "X", ".", ".", "P"],
 [".", "X", ".", "X", "."],
 [".", ".", "A", ".", "."],
 ["P", "X", ".", "X", "."],
 [".", ".", ".", "P", "."]
]
#   ENCONTRAR AGENTE
def buscar_agente(entorno):
    """Encuentra la fila y columna donde está 'A'."""
    for i, fila in enumerate(entorno):
        for j, celda in enumerate(fila):
            if celda == "A":
                return i, j
    return None  # Si no se encuentra a 'A'
# PERCIBIR
def percibir(entorno):
    posicion = buscar_agente(entorno)

    fila, columna = posicion
    num_filas = len(entorno)
    num_columnas = len(entorno[0])

    # Se evalúa cada dirección verificando los bordes de la matriz
    percepcion = {
        "agente_en": (fila, columna),
        "arriba": entorno[fila - 1][columna] if fila > 0 else None,
        "abajo": entorno[fila + 1][columna] if fila < num_filas - 1 else None,
        "izquierda": entorno[fila][columna - 1] if columna > 0 else None,
        "derecha": entorno[fila][columna + 1] if columna < num_columnas - 1 else None,
    }

    print(f"--- Percepción para el agente en posición ({fila}, {columna}) ---")
    print("Arriba:   ", percepcion["arriba"])
    print("Abajo:    ", percepcion["abajo"])
    print("Izquierda:", percepcion["izquierda"])
    print("Derecha:  ", percepcion["derecha"])

    return percepcion


#DECIDIR
def decidir(posicion_actual):
    pass
#ACTUAR
def actuar(posicion_actual):
    pass
#ACTUALIZAR MEDIDAS DE RENDIMIENTO
def actualizar(evento):
    pass



percibir(entorno1)






