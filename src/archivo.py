def leer_archivo_txt(nombre_archivo):
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            lista_elementos = archivo.read().splitlines()
        return lista_elementos
    except FileNotFoundError:
        print("El archivo no se encontró.")
        return []


def escribir_archivo_txt(tabla_hash_verbose, nombre_archivo):
    # Escribir la tabla hash en un archivo de texto
    with open("./output/"+nombre_archivo, "w", encoding="utf-8") as f:
        for i, celda in enumerate(tabla_hash_verbose, start=1):
            if celda is None:
                print(f"Celda {i}: []", file=f)
            else:
                print(f"Celda {i}: {celda}", file=f)


def print_tree_to_file(root, filename):
    tree_representation = []

    # Función auxiliar para construir la representación del árbol
    def build_tree_representation(node, level=0):
        if node:
            for key in node.keys:
                tree_representation.append("    " * level + "└── " + str(key))
            for child in node.children:
                build_tree_representation(child, level + 1)

    # Construir la representación del árbol
    build_tree_representation(root)

    # Escribir la representación del árbol en el archivo de texto
    with open(filename, 'w', encoding='utf-8') as file:
        for line in tree_representation:
            file.write(line + '\n')
