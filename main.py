from src import archivo
from src import hash
from src import arbol_b


if __name__ == "__main__":
    # Ejemplo de uso
    # Cambia esto por el nombre de tu archivo
    nombre_archivo = "./input/animales.txt"
    lista = archivo.leer_archivo_txt(nombre_archivo)
    animals = lista
    root = None
    max_hijos = 4   # Cambiar este valor según tu preferencia

    # Crear la tabla hash
    # Al tamaño de la tabla hash se le da el tamaño de la lista de animales
    tamano_tabla = len(lista)
    tabla_hash_verbose = hash.crear_tabla_hash_verbose(lista, tamano_tabla)

    # Escribir la tabla hash en un archivo de texto
    nombre_archivo = "tabla_hash_verbose.txt"
    archivo.escribir_archivo_txt(tabla_hash_verbose, nombre_archivo)

    # Ejemplo de uso:
    for animal in animals:
        # Convertir a minúsculas antes de insertar
        root = arbol_b.insert(root, animal.lower(), max_hijos)
    archivo.print_tree_to_file(root, "./output/arbol_b.txt")

    # Buscar un elemento
    # elemento_buscar = "Perro"
    # resultado_busqueda = hash.buscar_elemento(
    #     tabla_hash_verbose, elemento_buscar)
    # if resultado_busqueda is not None:
    #     print(
    #         f"Elemento {elemento_buscar} encontrado en la celda {resultado_busqueda[0]}")
    # else:
    #     print(f"Elemento {elemento_buscar} no encontrado en la tabla hash")

    # Eliminar un elemento
    # elemento_eliminar = "Perro"
    # resultado_eliminacion = hash.eliminar_elemento(
    #     tabla_hash_verbose, elemento_eliminar)
    # if resultado_eliminacion:
    #     print(f"Elemento {elemento_eliminar} eliminado de la tabla hash")
    # else:
    #     print(
    #         f"Elemento {elemento_eliminar} no encontrado en la tabla hash, no se pudo eliminar")
