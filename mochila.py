from itertools import permutations
import random
mochila = {}



# un escript que lea el exel y lo deje en este formato



poblacion = []
arreglo_de_claves = []
def generar_n_individuos_permutacion():
    global arreglo_de_claves
    for clave in mochila:
        arreglo_de_claves.append(clave)
    arreglo_permutaciones = permutations(arreglo_de_claves)
    arreglo_permutaciones = list(arreglo_permutaciones)
    return random.sample(arreglo_permutaciones, 7)

def seleccion_parejas(arreglo_permutaciones):
    numero_de_parejas = 1
    parejas_aleatorias = [random.sample(arreglo_permutaciones, 2) for _ in range(numero_de_parejas)]
    return parejas_aleatorias

def cruza(parejas_aleatorias):
    punto_de_cruce = 2
    hijos = []
    for pareja in parejas_aleatorias:
        tupla1 = pareja[0]
        tupla2 = pareja[1]
        # Realizar el cruce por punto fijo
        hijo1 = tupla1[:punto_de_cruce] + tupla2[punto_de_cruce:]
        hijo2 = tupla2[:punto_de_cruce] + tupla1[punto_de_cruce:]
        # Agregar las tuplas cruzadas a la lista de parejas cruzadas
        hijos.append(hijo1)
        hijos.append(hijo2)
    return hijos

def reparar_hijos(hijos_sin_reparar):
    global arreglo_de_claves
    hijos_reparados = []
    for hijo in hijos_sin_reparar:
        auxiliar_elementos_usados = []
        for elemanto in hijo:
            if elemanto in auxiliar_elementos_usados:
                 for claves in arreglo_de_claves: 
                     if claves not in auxiliar_elementos_usados:
                         auxiliar_elementos_usados.append(claves)
                         break
            else:       
                auxiliar_elementos_usados.append(elemanto)
        hijos_reparados.append(auxiliar_elementos_usados)
    return hijos_reparados
        

def mutacion(hijos_reparados):
    posibilidad_mut_individuo = 50
    posibilidad_mut_gen = 25
    for hijo in hijos_reparados:
        arreglo_posiciones_que_mutan=[]
        if random.randint(0,100) <= posibilidad_mut_individuo :
            for posicion in range(len(hijo)):
                if random.randint(0,100) <= posibilidad_mut_gen :
                    arreglo_posiciones_que_mutan.append(posicion)
        Intercambio_de_valor(arreglo_posiciones_que_mutan, hijo)

#metodo de modificar gen por intercambio de valor
def Intercambio_de_valor(arreglo_posiciones_que_mutan,hijo):
    global poblacion
    print(arreglo_posiciones_que_mutan)

    for elemento in arreglo_posiciones_que_mutan:
        posicion_random = random.randint(0,len(hijo)-1)
        print(posicion_random)
        #hace referencia al valor que va cambiar
        print(elemento)
        elemento_1 = hijo[elemento]
        #hace referencia al valor por el que se cambiara
        elemento_2 = hijo[posicion_random]

        hijo[elemento] = elemento_2
        hijo[posicion_random] = elemento_1
    poblacion.append(hijo)
    print(poblacion)





        
def main():
    global poblacion
    arreglo_permutaciones = generar_n_individuos_permutacion()
    print("permutaciones: ", arreglo_permutaciones,"\n")
    
    parejas_aleatorias = seleccion_parejas(arreglo_permutaciones)
    print("parejas aleatorias: ", parejas_aleatorias,"\n")

    hijos_sin_reparar = cruza(parejas_aleatorias)
    print("hijos sin reparar: ", hijos_sin_reparar,"\n")

    hijos_reparados = reparar_hijos(hijos_sin_reparar)
    print("hijos reparados: ", hijos_reparados,"\n")

    mutacion(hijos_reparados)

    poblacion.extend(parejas_aleatorias)
    ## despues de la mutacion
    poblacion.extend(hijos_reparados) 
    print("poblacion final: ", poblacion,"\n")

main()