# Reto 1: Buscador bidireccional
# Búsqueda en una lista doblemente enlazada desde la cabeza y desde la cola.

cabeza = None
cola = None


def crear_nodo(dato):
    return {"dato": dato, "anterior": None, "siguiente": None}


def agregar_final(dato):
    global cabeza, cola
    nuevo = crear_nodo(dato)

    if cabeza is None:
        cabeza = nuevo
        cola = nuevo
        return

    nuevo["anterior"] = cola
    cola["siguiente"] = nuevo
    cola = nuevo


def mostrar_adelante():
    actual = cabeza
    while actual is not None:
        print(actual["dato"], end=" ")
        actual = actual["siguiente"]
    print()


def mostrar_atras():
    actual = cola
    while actual is not None:
        print(actual["dato"], end=" ")
        actual = actual["anterior"]
    print()


def buscar(dato):
    global cabeza, cola

    actual = cabeza
    while actual is not None:
        if actual["dato"] == dato:
            return True
        actual = actual["siguiente"]

    actual = cola
    while actual is not None:
        if actual["dato"] == dato:
            return True
        actual = actual["anterior"]

    return False


if __name__ == "__main__":
    cabeza = None
    cola = None

    for valor in [10, 20, 30, 40]:
        agregar_final(valor)

    print("Lista adelante:")
    mostrar_adelante()
    print("Lista atrás:")
    mostrar_atras()

    print("¿Existe 30?", buscar(30))
    print("¿Existe 99?", buscar(99))
