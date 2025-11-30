# Template genérico — SKELETON
# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
gap = 0
i = 0
j = None

#METRICAS
steps = 0
comparaciones = 0

def init(vals):
    global items, n, gap, i, j
    global steps, comparaciones
    items = list(vals)
    n = len(items)
    gap = n // 2        # primer gap
    i = gap            # primer indice valido para comparacion
    j = None           
    
    steps = 0
    comparaciones = 0

def step():
    global items, n, gap, i, j
    global steps, comparaciones

    steps += 1
    print(f"DEBUG {steps}: Comparaciones={comparaciones}, Steps={steps}") #Muestra en DevTools (f12) 

    # Si gap llega a 0, fin
    if gap == 0:
        print(f"*** ALGORITMO FINALIZADO. Comparaciones totales: {comparaciones}, Steps totales: {steps} ***")
        return {"done": True}

    # si j es None, comenzamos nueva insercion con gap
    if j is None:
        if i >= n:
            # reducir gap
            gap //= 2
            if gap == 0:
                print(f"*** ALGORITMO FINALIZADO. Comparaciones totales: {comparaciones}, Steps totales: {steps} ***")
                return {"done": True}
            i = gap
            j = None
            return {"a": 0, "b": 0, "swap": False, "done": False}
        j = i
        return {"a": j - gap, "b": j, "swap": False, "done": False}

    comparaciones += 1
    # comparar con separacion gap
    if j - gap >= 0 and items[j] < items[j - gap]:
        a = j
        b = j - gap
        items[a], items[b] = items[b], items[a]
        j -= gap
        return {"a": a, "b": b, "swap": True, "done": False}

    # - Si ya no hay que desplazar: avanzar i y setear j=None.
    i += 1
    j = None
    return {"a": 0, "b": 0, "swap": False, "done": False}
    
