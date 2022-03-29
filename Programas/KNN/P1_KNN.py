from statistics import multimode
from MetricasSimilitud import EuclidianaPro, Canberra, Manhattan, Euclidiana




###CARGAR INSTANCIA DE ENTRENAMIENTO

#archivo = open("wine_training60.0.csv","r")
#archivo = open("wine_training70.0.csv","r")
#archivo = open("wine_training80.0.csv","r")
archivo = open("wine_training90.0.csv","r")

contenido = archivo.readlines()

#VISUALIZA EL CONTENIDO DEL ARCHIVO
print('\nArchivo Completo: ') #Impreso línea a línea
inde = 0
for l in contenido:
    print(inde)
    inde += 1
    print(l, end="") #por el formato en que se lee el archivo se quita el terminador (salto de linea) para evidar un doble salto
print("\n\n")


lista = [linea.split(",") for linea in contenido]

#VISUALIZA LISTA PROCESADA
print("Lista de listas separadas por comas: ")
#Impreso línea a línea
"""
for l in lista:
    print(l)
print("\n\n")
"""

instancia = [ [ list(map(float,x[:13])), float(x[13].replace("\n","")) ] for x in lista ] #iris

print("Total de datos de la Instancia",len(instancia))

print("Instancia de entrenamiento:")
#VISUALIZA EL CONTENIDO DEL ARCHIVO
#Impreso línea a línea
"""
for l in instancia:
    print(l)
print("\n\n")
"""

##############################################################################
###CARGAR INSTANCIA DE PRUEBA

#archivo = open("wine_test60.0.csv","r")
#archivo = open("wine_test70.0.csv","r")
#archivo = open("wine_test80.0.csv","r")
archivo = open("wine_test90.0.csv","r")
contenido = archivo.readlines()

#VISUALIZA EL CONTENIDO DEL ARCHIVO
"""
print('\nArchivo Completo: ') #Impreso línea a línea
for l in contenido:
    print(l, end="") #por el formato en que se lee el archivo se quita el terminador (salto de linea) para evidar un doble salto
print("\n\n")
"""

lista = [linea.split(",") for linea in contenido]

#VISUALIZA LISTA PROCESADA
print("Lista de listas separadas por comas: ")
#Impreso línea a línea
"""
for l in lista:
    print(l)
print("\n\n")
"""
prueba = [ [ list(map(float,x[:13])), float(x[13].replace("\n","")) ] for x in lista ] #iris

print("Total de datos de la Instancia",len(prueba))

print("Instancia de prueba:")
#VISUALIZA EL CONTENIDO DEL ARCHIVO
#Impreso línea a línea
"""
for l in prueba:
    print(l)
print("\n\n")
"""

###############################################################################
###DEFINIR QUE MEDIDA DE SIMILITUD SE UTILIZARÁ
medSimilitud = 0
while medSimilitud < 1 or medSimilitud > 4:
    medSimilitud = int(input("Qué medida de similitud desea utilizar: \n"
                         "\t 1 Manhattan\n"
                         "\t 2 Euclidiana Pro\n"
                         "\t 3 Canberra\n"
                         "\t 4 Euclidiana\n"
                             " >> "))

##############################################################################
###DEFINIR EL VALOR DE "K"  - Un número entre 1 y el total de registros de la instancia (entrenamiento)
##############################################################################
### Se declara el arreglo de aciertosenK para conocer cuantos aciertos tiene dicha K
aciertosK = []
##############################################################################
confusionMatrixforAllK  = []

for K in range(1,len(instancia)):

    print(f"CUANDO K = {K}\n\n\n")
    contAciertos = 0 #contador de aciertos obtenidos en la clasificación

    confusionMatrix = [[0, 0, 0],
                       [0, 0, 0],
                       [0, 0, 0]]

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
            elif medSimilitud == 3:
                distancia_NC_i = Canberra(NC, i[0])
            else:
                distancia_NC_i = Euclidiana(NC, i[0])
            #print(distancia_NC_i)
            estructuraDatos[NoCaso] = distancia_NC_i


        ordenado = sorted(estructuraDatos.items(), key=lambda x: x[1], reverse = False)


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

        moda = multimode(temporalK)
        print("Moda de los vectores más cercanos")
        print(moda)

        respKnn = moda[0]


        print("Clase asignada por el KNN: "  + str(respKnn))
        print("Clase Real: " + str(registroNC[1]))

        if respKnn == registroNC[1]:
            contAciertos += 1

        confusionMatrix[int(registroNC[1])-1][int(respKnn)-1] += 1

    confusionMatrixforAllK.append(confusionMatrix)

    aciertosK.append(contAciertos)
    print("Total de aciertos: " + str(contAciertos))
    print("Total de pruebas: " + str(len(prueba)))
    print("Rendimiento: " + str(contAciertos/len(prueba)*100))


print(aciertosK)
may = 0
indexMay = 0

for i in range(len(aciertosK)):
    if aciertosK[i] > may:
        #Se debe sumar 1 para ajustar K
        may = aciertosK[i]
        indexMay = i

print("\n\n\n")
print(f"La K = {indexMay + 1} tiene el mayor rendimiento")
print("Total de aciertos: " + str(aciertosK[indexMay]))
print("Total de pruebas: " + str(len(prueba)))
print("Rendimiento: " + str(aciertosK[indexMay] / len(prueba) * 100))

confusionMatrix = confusionMatrixforAllK[indexMay]
print(f"Matriz de confusición para K = {indexMay + 1}")
print("    1  2  3")
for i in range(len(confusionMatrix)):
    print(f"{i+1} ",end="")
    print(confusionMatrix[i])



print("CLASE 1 tiene: ")

p = round(confusionMatrix[0][0] / ( confusionMatrix[0][0] + (confusionMatrix[1][0] + confusionMatrix[2][0])),2)
print(f"\tP = {p}")

r = round(confusionMatrix[0][0] / ( confusionMatrix[0][0] + (confusionMatrix[0][1] + confusionMatrix[0][1]) ),2)
print(f"\tr = {r}")

f1 = round((2 * (r * p))/(r + p),2)
print(f"\tf1 = {f1}")

print("CLASE 2 tiene: ")

p = round(confusionMatrix[1][1] / ( confusionMatrix[1][1] + (confusionMatrix[0][1] + confusionMatrix[2][1]) ),2)
print(f"\tP = {p}")

r = round(confusionMatrix[1][1] / ( confusionMatrix[1][1] + (confusionMatrix[1][0] + confusionMatrix[1][2]) ),2)
print(f"\tr = {r}")

f1 = round((2 * (r * p))/(r + p),2)
print(f"\tf1 = {f1}")

print("CLASE 3 tiene: ")

p = round(confusionMatrix[2][2] / ( confusionMatrix[2][2] + (confusionMatrix[0][2] + confusionMatrix[1][2]) ),2)
print(f"\tP = {p}")

r = round(confusionMatrix[2][2] / ( confusionMatrix[2][2] + (confusionMatrix[2][0] + confusionMatrix[2][1]) ),2)
print(f"\tr = {r}")

f1 =round( (2 * (r * p))/(r + p),2)
print(f"\tf1 = {f1}")
