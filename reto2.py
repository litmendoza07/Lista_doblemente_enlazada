# Reto 2: Insertar después de un valor en una lista doblemente enlazada.

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


def insertar_despues(referencia, dato):
    global cabeza, cola
    actual = cabeza

    while actual is not None:
        if actual["dato"] == referencia:
            nuevo = crear_nodo(dato)
            nuevo["anterior"] = actual
            nuevo["siguiente"] = actual["siguiente"]

            if actual["siguiente"] is not None:
                actual["siguiente"]["anterior"] = nuevo
            else:
                cola = nuevo

            actual["siguiente"] = nuevo
            return True

        actual = actual["siguiente"]

    return False


if __name__ == "__main__":
    cabeza = None
    cola = None

    for valor in ["A", "B", "C"]:
        agregar_final(valor)

    print("Lista original:")
    mostrar_adelante()

    print("Insertar X después de B:", insertar_despues("B", "X"))
    mostrar_adelante()

    print("Insertar Y después de Z:", insertar_despues("Z", "Y"))
