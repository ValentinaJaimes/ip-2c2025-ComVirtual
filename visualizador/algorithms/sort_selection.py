# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
i = 0          # cabeza de la parte no ordenada
j = 0          # cursor que recorre y busca el mínimo
min_idx = 0    # índice del mínimo de la pasada actual
fase = "buscar"  # "buscar" | "swap"

def init(vals):
    global items, n, i, j, min_idx, fase
    items = list(vals)
    n = len(items)
    i = 0
    j = i + 1
    min_idx = i
    fase = "buscar"

def step():
    global i, j, min_idx, fase

    if i >= n - 1:
        return {"done": True}

    if fase == "buscar":
        if j >= n:

            fase = "swap"
            return step()


        if items[j] < items[min_idx]:
            min_idx = j

        current_j = j
        j += 1
        return {"a": min_idx, "b": current_j, "swap": False, "done": False}

    if fase == "swap":

        if min_idx != i:
            items[i], items[min_idx] = items[min_idx], items[i]
            result = {"a": i, "b": min_idx, "swap": True, "done": False}
        else:
            result = {"a": i, "b": min_idx, "swap": False, "done": False}


        i += 1
        if i >= n:
            return {"a": 0, "b": 0, "swap": False, "done": True}


        j = i + 1
        min_idx = i
        fase = "buscar"
        return result
