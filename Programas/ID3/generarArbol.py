import math as m
file = open("wine_training60.0.csv")
file2 = open("wine_test60.0.csv")


entropias = open("EntropiasWine60.txt", "a")
resEntropias = open("EntropiasWine60.txt", "a")

contenido = file.readlines()
contenido2 = file2.readlines()

contenidoP = [i.split(",") for i in contenido]
contenidoP2 = [i.split(",") for i in contenido2]

contenidoP = contenidoP + contenidoP2

print(len(contenidoP))


A = [ list(map(float, i) )for i in contenidoP ]

f = len(A)
c = len(A[0])

SI, NO = 0, 0

for i in range(f):
    if A[i][c-1] == 1:
        SI += 1
    else:
        NO += 1

GT = - (SI/f) * m.log2(SI/f) - (NO/f) * m.log2(NO/f)

for q in range(1, c-1):
    SI_et1, SI_et2, SI_et3, SI_et4 = 0, 0, 0, 0
    NO_et1, NO_et2, NO_et3, NO_et4 = 0, 0, 0, 0

    for i in range(f):
        if A[i][q] == 1:
            if A[i][ c-1] == 1:
                SI_et1 += 1
            else:
                NO_et1 += 1
        elif A[i][q] == 2:
            if A[i][c-1] == 1:
                SI_et2 += 1
            else:
                NO_et2 += 1
        elif A[i][q] == 3:
            if A[i][c-1] == 1:
                SI_et3 += 1
            else:
                NO_et3 += 1
        elif A[i][q] == 4:
            if A[i][c-1] == 1:
                SI_et4 += 1
            else:
                NO_et4 += 1


    Tet1, Tet2, Tet3, Tet4 = 0, 0, 0, 0
    Tet1 = SI_et1 + NO_et1
    Tet2 = SI_et2 + NO_et2
    Tet3 = SI_et3 + NO_et3
    Tet4 = SI_et4 + NO_et4

    Ee1, Ee2, Ee3, Ee4 = 0, 0, 0, 0
    if Tet1 == 0 or SI_et1 == 0 or NO_et1 == 0:
        Ee1 = 0
    else:
        Ee1 = -(SI_et1 / Tet1) * m.log2(SI_et1 / Tet1) - (NO_et1 / Tet1) * m.log2(NO_et1 / Tet1)

    if Tet2 == 0 or SI_et2 == 0 or NO_et2 == 0:
        Ee2 = 0
    else:
        Ee2 = -(SI_et2 / Tet2) * m.log2(SI_et2 / Tet2) - (NO_et2 / Tet2) * m.log2(NO_et2 / Tet2)

    if Tet3 == 0 or SI_et3 == 0 or NO_et3 == 0:
        Ee3 = 0
    else:
        Ee3 = -(SI_et3 / Tet3) * m.log2(SI_et3 / Tet3) - (NO_et3 / Tet3) * m.log2(NO_et3 / Tet3)

    if Tet4 == 0 or SI_et4 == 0 or NO_et4 == 0:
        Ee4 = 0
    else:
        Ee4 = -(SI_et4 / Tet4) * m.log2(SI_et4 / Tet4) - (NO_et4 / Tet4) * m.log2(NO_et4 / Tet4)


    EVar = ((Tet1 / f) * Ee1) + ((Tet2 / f) * Ee2) + ((Tet3 / f) * Ee3) + ((Tet4 / f) * Ee4)

    Gvar = abs(GT - EVar)

    entropias.write(f" {Ee1} {Ee2} {Ee3} {Ee4} {EVar} {Gvar}\n")
    resEntropias.write(f"{SI_et1} {NO_et1} {SI_et2} {NO_et2} {SI_et3} {NO_et3} {SI_et4} {NO_et4}\n")

entropias.close()
resEntropias.close()
