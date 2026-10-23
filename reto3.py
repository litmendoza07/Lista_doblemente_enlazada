# Reto 3: Historial del navegador.
# Implementación con listas y una variable para la página actual.

pagina_actual = None
historial_atras = []
historial_adelante = []


def visitar_pagina(pagina):
    global pagina_actual, historial_atras, historial_adelante

    if pagina_actual is not None:
        historial_atras.append(pagina_actual)

    historial_adelante.clear()
    pagina_actual = pagina


def retroceder():
    global pagina_actual, historial_atras, historial_adelante

    if not historial_atras:
        return False

    historial_adelante.append(pagina_actual)
    pagina_actual = historial_atras.pop()
    return True


def avanzar():
    global pagina_actual, historial_atras, historial_adelante

    if not historial_adelante:
        return False

    historial_atras.append(pagina_actual)
    pagina_actual = historial_adelante.pop()
    return True


def mostrar_actual():
    print("Página actual:", pagina_actual)


if __name__ == "__main__":
    visitar_pagina("Google")
    visitar_pagina("Facebook")
    visitar_pagina("YouTube")

    mostrar_actual()
    print("Retroceder:", retroceder())
    mostrar_actual()

    visitar_pagina("GitHub")
    mostrar_actual()
    print("Historial adelante:", historial_adelante)
    print("Historial atrás:", historial_atras)
