
def Manhattan( A, B):
    d = 0;
    for i in range(len(A)):
        d += abs(A[i] - B[i])
    return d


def Euclidiana(A, B):
    d = 0
    for i in range(len(A)):
        d += (A[i] - B[i])**2
    d = d ** 0.5
    return d


def EuclidianaPro(A, B):
    d = 0
    for i in range(len(A)):
        d += (A[i] - B[i]) ** 2
    d = (d/len(A))**0.5
    return d

def DiferenciaCaracterPro(A, B):
    d = Manhattan(A, B) / len(A)
    print(d)
    return d

def  Canberra(A, B):
    d = 0
    for i in range (len(A)):
        d += abs(A[i]-B[i])/(abs(A[i])+abs(B[i]))
    return d

def SorenceDice(A, B):
    up, down = 0, 0

    for i in range(len(A)):
        up += A[i] + B[i]
        down += A[i] + B[i]

    d = 2 * up / down
    return d

def Coseno(A, B):
    up, x2, y2 = 0, 0, 0
    for i in range(len(A)):
        up += A[i] * B[i]
        x2 += A[i] ** 2
        y2 += B[i] ** 2

    d = up / ( x2 * y2 ) ** 0.5
    return d

def Jaccard(A, B):
    up, x2, y2 = 0, 0, 0
    for i in range(len(A)):
        up += A[i] * B[i]
        x2 += A[i] ** 2
        y2 += B[i] ** 2

    d = up / ( x2 + y2 - up )
    return d

def EucliadanaNorm(A, B):
    cont = 0

    for i in range(len(A)):
        cont += A[i] ** 2 - 2 * (A[i] + B[i])  + B[i] ** 2

    d = cont
    return d
