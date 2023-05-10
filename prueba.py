

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

        
reparar_hijos()