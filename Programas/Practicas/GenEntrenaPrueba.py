import serial as connector #para conectar con Arduino
import sys
import PyQt5
from PyQt5 import uic, QtWidgets
import  random

qtCreatorFile = "Test_Entrena_Vali.ui"  # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = PyQt5.uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.btn_exe.clicked.connect(self.createFiles)




    def createFiles(self):

        indice = int(self.txt_test.text())

        archivo = open("Instancia_wine.csv", "r")  # ABRE EL ARCHIVO
        contenido = archivo.readlines()  # LEE TODO EL CONTENIDO DEL ARCHIVO

        # VISUALIZA EL CONTENIDO DEL ARCHIVO
        print('\nArchivo Completo: ')  # Impreso línea a línea
        for l in contenido:
            print(l,
                  end="")  # por el formato en que se lee el archivo se quita el terminador (salto de linea) para evidar un doble salto
        print("\n\n")

        # CREA UNA LISTA EN LA QUE CADA ELEMENTO SEA UNA LINEA DEL ARCHIVO CONVERTIDA EN LISTA SEPARADA POR TABULADOR
        lista = [linea.split(",") for linea in contenido]

        instanica = []
        for data in lista:
            aux = list(map(float, data[:13]))
            aux.append(int(data[13].replace("\n","")))
            instanica.append(aux)


        random.shuffle(instanica)

        entrenamiento = instanica[:indice]
        #random.shuffle(entrenamiento)
        prueba = instanica[indice:]
        #random.shuffle(prueba)

        fileEntrena = open("wine_entrenamiento8713.csv","w")
        filePrueba = open("wine_prueba8713.csv","w")


        for data in entrenamiento:
            aux = str(data)
            aux = aux[1:len(aux)-1]
            fileEntrena.write(aux + "\n")


        for data in prueba:
            aux = str(data)
            aux = aux[1:len(aux)-1]
            filePrueba.write(aux+ "\n")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
