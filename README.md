# TP — Visualización de algoritmos de ordenamiento 

## Introducción a la Programación - Comisión virtual - UNGS2C2025

## Integrantes 👥
 - Pereyra Rios, Marco Leon
 - Jaimes, Valentina
   
---

## Objetivos 🔍

- Implementar **Bubble**, **Selection** e **Insertion** cumpliendo el **contrato** `init(vals)` + `step()` que usa la UI.
- Ver el algoritmo **animado** y **paso a paso** (una operación por llamada a `step`).
- (Opcional) Agregar algoritmos extra y/o **métricas** (comparaciones, swaps, tiempo), y documentar un análisis breve.

---

# Algoritmos implementados ✅

Hemos implementado los siguientes algoritmos dentro de la carpeta `/algorithms/`:

1.  **Bubble Sort** (`sort_bubble.py`)
2.  **Selection Sort** (`sort_selection.py`)
3.  **Insertion Sort** (`sort_insertion.py`)
4.  **Gnome Sort** (`sort_gnome.py`)
5.  **Shell Sort** (`sort_shell.py`)

---

## Ver nuestro visualizador ▶️

Para cargar el entorno web y ejecutar los algoritmos localmente:

1.  Abrir la terminal (sea PowerShell, CMD o Terminal de VSC) dentro de la carpeta `/visualizador`.
2.  Ejecutar el siguiente comando para iniciar el servidor HTTP local:

    ```
    python -m http.server 8000
    ```
3.  Abrir el navegador web e ir a la siguiente dirección:

    ```
    http://localhost:8000
    ```
4. Si se desea ver las métricas adicionales integradas, las pueden observar a través de la consola del navegador (F12).