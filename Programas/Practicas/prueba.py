from statistics import multimode
from MetricasSimilitud import EuclidianaPro, Canberra, Manhattan

###CARGAR INSTANCIA DE ENTRENAMIENTO

archivo = open("iris_entrenamiento.csv", "r")
contenido = archivo.readlines()

#VISUALIZA EL CONTENIDO DEL ARCHIVO
print('\nArchivo Completo: ') #Impreso línea a línea
for l in contenido:
    print(l, end="") #por el formato en que se lee el archivo se quita el terminador (salto de linea) para evidar un doble salto
print("\n\n")


lista = [linea.split(",") for linea in contenido]

#VISUALIZA LISTA PROCESADA
print("Lista de listas separadas por comas: ")
#Impreso línea a línea
for l in lista:
    print(l)
print("\n\n")


instancia = [ [ list(map(float,x[:4])), x[4] ] for x in lista ] #iris

print("Total de datos de la Instancia",len(instancia))

print("Instancia de entrenamiento:")
#VISUALIZA EL CONTENIDO DEL ARCHIVO
#Impreso línea a línea
for l in instancia:
    print(l)
print("\n\n")


##############################################################################
###CARGAR INSTANCIA DE PRUEBA

archivo = open("iris_prueba.csv", "r")
contenido = archivo.readlines()

#VISUALIZA EL CONTENIDO DEL ARCHIVO
print('\nArchivo Completo: ') #Impreso línea a línea
for l in contenido:
    print(l, end="") #por el formato en que se lee el archivo se quita el terminador (salto de linea) para evidar un doble salto
print("\n\n")


lista = [linea.split(",") for linea in contenido]

#VISUALIZA LISTA PROCESADA
print("Lista de listas separadas por comas: ")
#Impreso línea a línea
for l in lista:
    print(l)
print("\n\n")

prueba = [ [ list(map(float,x[:4])), x[4] ] for x in lista ] #iris

print("Total de datos de la Instancia",len(prueba))

print("Instancia de prueba:")
#VISUALIZA EL CONTENIDO DEL ARCHIVO
#Impreso línea a línea
for l in prueba:
    print(l)
print("\n\n")

medSimilitud = 0
while medSimilitud < 1 or medSimilitud > 3:
    medSimilitud = int(input("Qué medida de similitud desea utilizar: \n"
                         "\t 1 Manhattan\n"
                         "\t 2 Euclidiana Pro\n"
                         "\t 3 Canberra\n"
                             " >> "))



aciertosK = []
##############################################################################



for K in range(1,len(instancia)):
    print(f"CUANDO K = {K}\n\n\n")
    contAciertos = 0 #contador de aciertos obtenidos en la clasificación

    for registroNC in prueba:
        print("Clasificación del registro: ")
        print(registroNC)

        NC = registroNC[0]
        estructuraDatos = {}

        for NoCaso, i in enumerate(instancia):
            if medSimilitud == 1:
                distancia_NC_i = Manhattan(NC, i[0])
            elif medSimilitud == 2:
                distancia_NC_i = EuclidianaPro(NC, i[0])
            else:
                distancia_NC_i = Canberra(NC, i[0])
            #print(distancia_NC_i)
            estructuraDatos[NoCaso] = distancia_NC_i



        ordenado = sorted(estructuraDatos.items(), key=lambda x: x[1])
        print(ordenado)

        temporalK = []
        for i in range(K):
            NoCaso = ordenado[i][0]
            #print(etiqueta)
            registro = instancia[NoCaso]


            #print(registro)
            temporalK.append(registro[1]) #obtencion de la etiqueta


        print("Clases de los vectores más cercanos al registro NC:")
        print(temporalK)  #los primeros K vectores
        print("\n\n")


        from statistics import multimode
        moda = multimode(temporalK)
        respKnn = moda[0]

        print(f"ESTA ES LA MODA PARA CUANDO K = {K}")
        print(moda)

        print("Clase asignada por el KNN: "  + str(respKnn))
        print("Clase Real: " + str(registroNC[1]))

        if str(respKnn) == registroNC[1]:
            contAciertos += 1
            print("Acerto")
        else:
            print("Fallo")

    print("Total de aciertos: " + str(contAciertos))
    print("Total de pruebas: " + str(len(prueba)))
    print("Rendimiento: " + str(contAciertos/len(prueba)*100))

    aciertosK.append((K,contAciertos))



for ka, cont in aciertosK:
    print(f" k = {ka} tiene como resultado {cont}")
