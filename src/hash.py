def custom_hash_with_position_verbose(word):
    """
    Calcula el hash de la palabra dada con la posición de cada carácter en la palabra.
    Retorna el valor del hash y una expresión que muestra los pasos del cálculo.
    """
    hash_val = 0
    hash_steps = []
    for i, char in enumerate(word):
        step = f"{ord(char)}^{i + 1}"
        hash_steps.append(step)
        hash_val += ord(char) ** (i + 1)
    hash_expression = '+'.join(hash_steps)
    return hash_val, hash_expression


def crear_tabla_hash_verbose(lista_palabras, tamano_tabla):
    tabla_hash = {}
    for palabra in lista_palabras:
        hash_val, hash_expression = custom_hash_with_position_verbose(palabra)
        indice = hash_val % tamano_tabla
        if indice not in tabla_hash:
            tabla_hash[indice] = []
        tabla_hash[indice].append(palabra)

    # Crear una lista de celdas que contenga las listas de palabras o valores nulos si la celda está vacía
    celdas_ordenadas = [None] * tamano_tabla
    for clave, valor in tabla_hash.items():
        celdas_ordenadas[clave] = valor

    return celdas_ordenadas


def buscar_elemento(tabla_hash, elemento):
    """
    Busca un elemento en la tabla hash utilizando la fórmula hash.
    Retorna el índice de la celda si se encuentra el elemento, o None si no se encuentra.
    """
    hash_val, _ = custom_hash_with_position_verbose(elemento)
    indice = hash_val % len(tabla_hash)
    celda = tabla_hash[indice]
    if celda is None:
        return None
    else:
        try:
            return indice, celda.index(elemento)
        except ValueError:
            return None


def eliminar_elemento(tabla_hash, elemento):
    """
    Elimina un elemento de la tabla hash utilizando la fórmula hash.
    Retorna True si se eliminó el elemento correctamente, o False si el elemento no estaba en la tabla.
    """
    indice = buscar_elemento(tabla_hash, elemento)
    if indice is not None:
        tabla_hash[indice[0]].remove(elemento)
        return True
    else:
        return False
