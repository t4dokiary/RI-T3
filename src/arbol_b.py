class BTreeNode:
    def __init__(self, keys=None, children=None):
        if keys is None:
            keys = []
        if children is None:
            children = []
        self.keys = keys
        self.children = children


def insert(raiz, value, max_hijos):
    if not raiz:
        return BTreeNode([value])

    # Encontrar la posición adecuada para insertar el valor
    i = len(raiz.keys) - 1
    while i >= 0 and value < raiz.keys[i]:
        i -= 1

    # Si el valor ya está presente, no hacemos nada
    if raiz.keys[i] == value:
        return raiz

    # Insertar en el hijo correspondiente
    if raiz.children:
        if len(raiz.children) > i + 1:
            raiz.children[i + 1] = insert(raiz.children[i + 1], value, max_hijos)
        else:
            raiz.children.append(insert(None, value, max_hijos))
    else:
        raiz.children = [insert(None, value, max_hijos)]

    # Dividir el nodo si es necesario
    if len(raiz.keys) > max_hijos - 1:  # Cambiar este valor según la cantidad máxima de hijos
        return split(raiz)

    return raiz


def split(node):
    mid = len(node.keys) // 2
    left_keys = node.keys[:mid]
    right_keys = node.keys[mid + 1:]
    left_children = node.children[:mid + 1]
    right_children = node.children[mid + 1:]

    left_child = BTreeNode(left_keys, left_children)
    right_child = BTreeNode(right_keys, right_children)

    mid_key = node.keys[mid]
    return BTreeNode([mid_key], [left_child, right_child])


def search(raiz, value):
    if not raiz:
        return False

    for i in range(len(raiz.keys)):
        if raiz.keys[i] == value:
            return True
        elif raiz.keys[i] > value:
            if raiz.children:
                return search(raiz.children[i], value)
            else:
                return False
    if raiz.children:
        return search(raiz.children[-1], value)
    else:
        return False


def print_tree(raiz, level=0, max_hijos=2):
    if raiz:
        # Imprimir claves y sus hijos de forma recursiva
        if raiz.children:
            for child, key in zip(raiz.children, raiz.keys):
                if isinstance(key, list) and not key:
                    continue
                print("    " * level + "└──", key)
                print_tree(child, level + 1, max_hijos)
            if len(raiz.children) > len(raiz.keys) and len(raiz.keys) < max_hijos:
                print_tree(raiz.children[-1], level + 1, max_hijos)
        else:
            if isinstance(raiz.keys, list) and not raiz.keys:
                return
            print("    " * level + "└──", raiz.keys)
