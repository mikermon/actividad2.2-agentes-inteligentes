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
def percibir(entorno,fila,columna):
    arriba=fila-1
    abajo=fila+1
    derecha=columna+1
    izquierda=fila-1
    percibir_arriba=entorno[arriba][columna]
    percibir_abajo=entorno[abajo][columna]
    percibir_derecha=entorno[derecha][columna]
    percibir_izquierda=entorno[izquierda][columna]
    print("Percepcion")
    print("arriba:",percibir_arriba)
    print("abajo:",percibir_abajo)
    print("derecha:",percibir_derecha)
    print("izquierda:",percibir_izquierda)


#DECIDIR
def decidir(posicion_actual):
    pass
#ACTUAR
def actuar(posicion_actual):
    pass
#ACTUALIZAR MEDIDAS DE RENDIMIENTO
def actualizar(evento):
    pass



percibir(entorno2,3,3)






