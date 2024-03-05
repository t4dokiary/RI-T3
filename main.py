from src import archivo
from src import hash
from src import arbol_b

# Ejemplo de uso
nombre_archivo = "./input/animales.txt"  # Cambia esto por el nombre de tu archivo
lista = archivo.leer_archivo_txt(nombre_archivo)
print(lista)

# Crear la tabla hash
tamano_tabla = 200
tabla_hash_verbose = hash.crear_tabla_hash_verbose(lista, tamano_tabla)

# Imprimir la tabla hash con celdas nulas
for i, celda in enumerate(tabla_hash_verbose, start=0):
    if celda is None:
        print(f"Celda {i}: []")
    else:
        print(f"Celda {i}: {celda}")

# Escribir la tabla hash en un archivo de texto
nombre_archivo = "tabla_hash_verbose.txt"
archivo.escribir_archivo_txt(tabla_hash_verbose, nombre_archivo)

# Buscar un elemento
elemento_buscar = "Perro"
resultado_busqueda = hash.buscar_elemento(tabla_hash_verbose, elemento_buscar)
if resultado_busqueda is not None:
    print(f"Elemento {elemento_buscar} encontrado en la celda {resultado_busqueda[0]}")
else:
    print(f"Elemento {elemento_buscar} no encontrado en la tabla hash")

# Imprimir la tabla hash con celdas nulas
for i, celda in enumerate(tabla_hash_verbose, start=0):
    if celda is None:
        print(f"Celda {i}: []")
    else:
        print(f"Celda {i}: {celda}")

# Eliminar un elemento
elemento_eliminar = "Perro"
resultado_eliminacion = hash.eliminar_elemento(tabla_hash_verbose, elemento_eliminar)
if resultado_eliminacion:
    print(f"Elemento {elemento_eliminar} eliminado de la tabla hash")
else:
    print(f"Elemento {elemento_eliminar} no encontrado en la tabla hash, no se pudo eliminar")

# Imprimir la tabla hash con celdas nulas
for i, celda in enumerate(tabla_hash_verbose, start=0):
    if celda is None:
        print(f"Celda {i}: []")
    else:
        print(f"Celda {i}: {celda}")

# Ejemplo de uso:
root = None
animals = lista
max_hijos = 2   # Cambiar este valor según tu preferencia

for animal in animals:
    root = arbol_b.insert(root, animal.lower(), max_hijos)  # Convertir a minúsculas antes de insertar

primera_busqueda = arbol_b.search(root, 'Unicornio'.lower())  # Convertir a minúsculas antes de buscar
print(str(primera_busqueda))  # True
segunda_busqueda = arbol_b.search(root, 'Perdiz'.lower())  # Convertir a minúsculas antes de buscar
print(str(segunda_busqueda))  # False

arbol_b.print_tree(root, max_hijos)

archivo.print_tree_to_file(root, "./output/arbol_b.txt")
print('hola')
