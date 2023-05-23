from itertools import permutations
import pandas as pd
import random
mochila = {}

posicion_valor_diferencia = {}

poblacion = []

arreglo_de_claves = []

# 
numero_de_poblacion_iniical = 2


# un escript que lea el exel y lo deje en este formato
def leer_exel():
    df = pd.read_excel('datos.xlsx')
    df = df.iloc[:, 1:]
    inicio = 0
    for index, row in df.iterrows():
        if inicio <= 3:
            inicio = inicio + 1
        else: 
            mochila[index+1-4] = [row[col] for col  in range(13)]


def generar_n_individuos_aleatorios():
    global arreglo_de_claves
    poblacion_inicial = []
    auxiliar_claves = []
    for clave in mochila:
        arreglo_de_claves.append(clave)
    auxiliar_claves = arreglo_de_claves
    
    for i in range(numero_de_poblacion_iniical):
        auxiliar_claves_copia = auxiliar_claves[:] # crea una copia de la lista
        random.shuffle(auxiliar_claves_copia) # baraja la copia
        poblacion_inicial.append(auxiliar_claves_copia) # agrega la copia barajada a la población inicial
    return poblacion_inicial
   
def seleccion_parejas():
    numero_de_parejas = 5
    parejas_aleatorias = [random.sample(poblacion, 2) for _ in range(numero_de_parejas)]
    return parejas_aleatorias

def cruza(parejas_aleatorias):
    punto_de_cruce = 8
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
        
# 2,1,3,5,4,6

def mutacion(hijos_reparados):
    posibilidad_mut_individuo = 60
    posibilidad_mut_gen = 10
    for hijo in hijos_reparados:
        arreglo_posiciones_que_mutan=[]

        if random.randint(0,100) <= posibilidad_mut_individuo :

            for posicion in range(len(hijo)):

                if random.randint(0,100) <= posibilidad_mut_gen :
                    arreglo_posiciones_que_mutan.append(posicion)

            Intercambio_de_valor(arreglo_posiciones_que_mutan, hijo)

        else:
            poblacion.append(hijo)
# 0 1 2 3 4 5
# 2,1,3,5,4,6
# . * * * . *

#metodo de modificar gen por intercambio de valor
def Intercambio_de_valor(arreglo_posiciones_que_mutan,hijo):
    global poblacion
    for elemento in arreglo_posiciones_que_mutan:
        posicion_random = random.randint(0,len(hijo)-1)
     
        #hace referencia al valor que va cambiar

        elemento_1 = hijo[elemento]#2
        #hace referencia al valor por el que se cambiara
        elemento_2 = hijo[posicion_random]#3

        hijo[elemento] = elemento_2

        hijo[posicion_random] = elemento_1

    poblacion.append(hijo)
  
  #3,1,3,5,4,6
  #3,1,2,5,4,6

                    #mochila    #poblacion
def sumar_valores(diccionario, lista_claves):
    # Inicializar variables para sumar los valores
    contador = 0

    for individuo in lista_claves:

        resultado = []
        nombre_elementos = []
        categorias = []
        valores = [0] * 11
        num_elemtos = 30   
        aux = individuo[:num_elemtos]

        # Iterar a través de las claves en la lista
        #aux son los primeros 30 elementos de l individuo
        for clave in aux:
            # Obtener el elemento correspondiente y agregar su nombre
            elemento = diccionario[clave]
            nombre_elementos.append(elemento[0])
            categorias.append(elemento[1])

            # Sumar los valores del elemento
            for i in range(2, len(elemento)):
                if i in [5, 6, 9, 10, 12] :
                    valores[i-2] += elemento[i]/1000
                elif i in  [7 , 11]:
                    valores[i-2] += elemento[i]/1000
                else:
                    valores[i-2] += elemento[i]

        # Retornar el resultado como una lista
        resultado.append(nombre_elementos)
        resultado.append(categorias)
        resultado.append(valores)
        posicion_valor_diferencia[contador] = resultado
        contador += 1

# [[alimnetos],[categorias],[atributos]]


def obtener_diferencia():
    
    valores_atributos = [3200,260,150,20,1,10,10,1,1,1,1]
    # for i in range(11):
    #     valores_atributos.append(int(input(str(i) + ": ")))
  
    for elemento in range(len(posicion_valor_diferencia)):
        aux_valores = []
        aux = 0
        for atributos in posicion_valor_diferencia[elemento][2]:
            valor = atributos - valores_atributos[aux]
            aux_valores.append(valor)
            aux = aux + 1
        posicion_valor_diferencia[elemento].append(aux_valores)


def calcular_suma_distancias():
    arreglo_suma_distancias_aux = []
    for elemento in posicion_valor_diferencia.values():
        suma_distancias = sum(abs(elemento) for elemento in elemento[3])
        arreglo_suma_distancias_aux.append(suma_distancias)

    for i in posicion_valor_diferencia:
        posicion_valor_diferencia[i].append(arreglo_suma_distancias_aux[i])

    return suma_distancias

def ordenar_elitsta():
    global poblacion
    combinado = list(zip(posicion_valor_diferencia.values(), poblacion))
    ordenado = sorted(combinado, key=lambda x: x[0][4])
    arreglos_ordenados = [tupla[1] for tupla in ordenado]
    poblacion = arreglos_ordenados[:7]

def main():

    global poblacion
    leer_exel()

    numero_iteraciones = 30
    
    poblacion = generar_n_individuos_aleatorios()
  
      ##inicia el bucle
    for i in range(numero_iteraciones):
        parejas_aleatorias = seleccion_parejas()
            

        hijos_sin_reparar = cruza(parejas_aleatorias)
            

        hijos_reparados = reparar_hijos(hijos_sin_reparar)
        

        mutacion(hijos_reparados)

        sumar_valores(mochila, poblacion)

        obtener_diferencia()

        calcular_suma_distancias()

        ordenar_elitsta()
        
    print(poblacion)
        
    ##termina el bucle
    ## despues de la mutacion




main()



