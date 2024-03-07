from src import archivo
from src import hash
from src import arbol_b
import random


if __name__ == "__main__":
    nombre_archivo = "./input/animales.txt"
    lista = archivo.leer_archivo_txt(nombre_archivo)
    random.shuffle(lista)
    tamano_tabla = len(lista)
    tabla_hash_verbose = hash.crear_tabla_hash_verbose(lista, tamano_tabla)

    print("Tabla hash:")
    hash.print_hash(tabla_hash_verbose)
    print('\n')

    elemento_buscar = "Perro"
    resultado_busqueda = hash.buscar_elemento(
        tabla_hash_verbose, elemento_buscar)
    if resultado_busqueda is not None:
        print(
            f"Elemento {elemento_buscar} encontrado en la celda {resultado_busqueda[0]+1}")
    else:
        print(f"Elemento {elemento_buscar} no encontrado en la tabla hash")

    elemento_buscar = "unicornio"
    resultado_busqueda = hash.buscar_elemento(
        tabla_hash_verbose, elemento_buscar)
    if resultado_busqueda is not None:
        print(
            f"Elemento {elemento_buscar} encontrado en la celda {resultado_busqueda[0]+1}")
    else:
        print(f"Elemento {elemento_buscar} no encontrado en la tabla hash")
    print('\n')

    # Crear árbol B y leer palabras del archivo de animales
    arbol_animales = arbol_b.leer_archivo_y_construir_arbol(
        './input/animales.txt')

    # Mostrar el árbol en consola
    print("Árbol B de animales:")
    arbol_animales.imprimir()

    # Realizar consultas sobre palabras que existen y no existen en el árbol
    palabra_existente = "Pez Rana"
    palabra_no_existente = "unicornio"
    print('\n')
    encontrada, profundidad = arbol_b.buscar_palabra(
        arbol_animales, palabra_existente)
    if encontrada:
        print(
            f"La palabra '{palabra_existente}' existe en el árbol. Profundidad: {profundidad}")
    else:
        print(f"La palabra '{palabra_existente}' no existe en el árbol.")

    encontrada, profundidad = arbol_b.buscar_palabra(
        arbol_animales, palabra_no_existente)
    if encontrada:
        print(
            f"La palabra '{palabra_no_existente}' existe en el árbol. Profundidad: {profundidad}")
    else:
        print(f"La palabra '{palabra_no_existente}' no existe en el árbol.")
    print('\n')
