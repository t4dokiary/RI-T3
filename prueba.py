from bisect import bisect_left


class NodoB:
    def __init__(self, hoja=True):
        self.hoja = hoja
        self.claves = []
        self.hijos = []

    def insertar(self, clave):
        if self.hoja:
            self.claves.append(clave)
            self.claves.sort()
            if len(self.claves) > 2:
                return self.dividir()
        else:
            hijo = self.hijo_para(clave)
            division = hijo.insertar(clave)
            if division:
                self.claves.append(division[0])
                self.claves.sort()
                self.hijos.remove(hijo)
                self.hijos.extend(division[1:])
                if len(self.claves) > 3:
                    return self.dividir()
        return None

    def dividir(self):
        medio = len(self.claves) // 2
        padre = self
        nueva_clave = self.claves[medio]
        nueva_hoja_izq = NodoB(hoja=self.hoja)
        nueva_hoja_izq.claves = self.claves[:medio]
        nueva_hoja_der = NodoB(hoja=self.hoja)
        nueva_hoja_der.claves = self.claves[medio + 1:]
        if not self.hoja:
            nueva_hoja_izq.hijos = self.hijos[:medio + 1]
            nueva_hoja_der.hijos = self.hijos[medio + 1:]
        return nueva_clave, nueva_hoja_izq, nueva_hoja_der

    def hijo_para(self, clave):
        for i, c in enumerate(self.claves):
            if clave < c:
                return self.hijos[i]
        return self.hijos[-1]

    def imprimir(self, profundidad=0):
        print('  ' * profundidad, self.claves)
        for hijo in self.hijos:
            hijo.imprimir(profundidad + 1)


class ArbolB:
    def __init__(self):
        self.raiz = NodoB()

    def insertar(self, clave):
        division = self.raiz.insertar(clave)
        if division:
            nueva_raiz = NodoB(hoja=False)
            nueva_raiz.claves = [division[0]]
            nueva_raiz.hijos = [division[1], division[2]]
            self.raiz = nueva_raiz

    def imprimir(self):
        self.raiz.imprimir()


# Función para leer el archivo y agregar palabras al árbol B
def leer_archivo_y_construir_arbol(nombre_archivo):
    arbol = ArbolB()
    with open(nombre_archivo, 'r', encoding='utf8') as archivo:
        for linea in archivo:
            arbol.insertar(linea.strip())
    return arbol

# Función para buscar una palabra en el árbol


def buscar_palabra(arbol, palabra, nodo=None, profundidad=0):
    if nodo is None:
        nodo = arbol.raiz

    while nodo:
        posicion = bisect_left(nodo.claves, palabra)

        if posicion < len(nodo.claves) and nodo.claves[posicion] >= palabra:
            return True, profundidad

        elif posicion < len(nodo.claves) and palabra < nodo.claves[posicion]:
            if not nodo.hijos:
                return False, profundidad + 1
            nodo = nodo.hijos[posicion]
            profundidad += 1

        else:
            if posicion == len(nodo.claves):
                if not nodo.hijos:
                    return False, profundidad + 1
                nodo = nodo.hijos[posicion]
                profundidad += 1
            else:
                if not nodo.claves:
                    return False, profundidad + 1
                nodo = nodo.hijos[posicion + 1]
                profundidad += 1

    return False, profundidad


# Crear árbol B y leer palabras del archivo de animales
arbol_animales = leer_archivo_y_construir_arbol('./input/animales.txt')

# Mostrar el árbol en consola
print("Árbol B de animales:")
arbol_animales.imprimir()

# Realizar consultas sobre palabras que existen y no existen en el árbol
palabra_existente = "Pez Rana"
palabra_no_existente = "unicornio"
print('\n')
encontrada, profundidad = buscar_palabra(arbol_animales, palabra_existente)
if encontrada:
    print(
        f"La palabra '{palabra_existente}' existe en el árbol. Profundidad: {profundidad}")
else:
    print(f"La palabra '{palabra_existente}' no existe en el árbol.")

encontrada, profundidad = buscar_palabra(arbol_animales, palabra_no_existente)
if encontrada:
    print(
        f"La palabra '{palabra_no_existente}' existe en el árbol. Profundidad: {profundidad}")
else:
    print(f"La palabra '{palabra_no_existente}' no existe en el árbol.")
print('\n')
