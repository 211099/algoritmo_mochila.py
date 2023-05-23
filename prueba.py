import random
poblacion = [[1,5,4,3,2]]

def reparar_hijos():
    arreglo_de_claves = [1,2,3,4,5]
    hijos_sin_reparar = [(4, 3, 3, 2, 3), (1, 4, 2, 1, 5)]
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

    print(hijos_reparados)

        
def acceder_diccionario():
    mochila = {
    1 : ["manzana",30,50,60],
    2 : ["pera",28,30,60],
    3 : ["chocolate",120,20,150],
    4 : ["mango",40,60,110],
    5 : ["paleta",70,8,80],
    }
    
    for clave in mochila:
        print(mochila[clave])
        for nombre in mochila[clave]:
            print(nombre)


def mutacion():
    hijos_reparados = [ [4, 2, 3, 1, 5], [1, 2 , 3 , 4 , 5 ]]
    posibilidad_mut_individuo = 50
    posibilidad_mut_gen = 25
    for hijo in hijos_reparados:
        arreglo_posiciones_que_mutan=[]
        if random.randint(0,100) <= posibilidad_mut_individuo :
            for posicion in range(len(hijo)):
                if random.randint(0,100) <= posibilidad_mut_gen :
                    arreglo_posiciones_que_mutan.append(posicion)
        cambio_de_posicion(arreglo_posiciones_que_mutan, hijo)
    
        
        

def cambio_de_posicion(arreglo_posiciones_que_mutan,hijo):
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



mutacion()