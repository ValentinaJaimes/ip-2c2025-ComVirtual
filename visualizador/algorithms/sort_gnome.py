# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}
#Con sort_gnome vamos a buscar compararlo con sort_insertion (tiempo de ordenamiento,comparaciones realizadas, steps)
#FALTA AGREGAR METRICAS!!

items = []
n = 0
i = 0

def init(vals):
    global items, n, i
    items = list(vals)
    n = len(items)
    i = 1   # arranco en el segundo elemento

def step():
    global items, n, i

    # Si i >= n: devolver {"done": True}. // Fin del programa
    if i >= n:
        return {"done": True}

    # En caso de que estemos en el inicio, el programa debe avanzar al siguiente
    if i == 0:
        i = 1
        return {"a": 0, "b": 0, "swap": False, "done": False}

    # Hago la comparación entre los items
    if items[i] >= items[i - 1]:       # si la comparacion es correcta entonces avanzo
        i += 1
        return {"a": i - 1, "b": i - 2, "swap": False, "done": False}
    else:
        # En caso de que sea incorrecta, retrocedo e intercambio para seguir avanzando
        items[i], items[i - 1] = items[i - 1], items[i] 
        i -= 1
        return {"a": i, "b": i + 1, "swap": True, "done": False}
