import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class ejercicios:
    def __init__(self):
        datos=[(1,0),(2,0), (3,0), (4,0)]
        self.df= pd.DataFrame(data=datos,columns=["#ejercicio", "valor"])

    def ejercicio1(self):

        # Generar un array con valores desde 10 hasta 29
        array_10_29 = np.arange(10,30)
        #self.df["#ejercicio"]=1
        #self.df["valor"]=str(array_10_29)
        self.df.iloc[0,1]=str(array_10_29)
        #self.df.to_excel("Actividad_2.xlsx")

    def ejercicio2(self):

        # 2. Suma de una matriz 10x10 de unos.
        array2 = np.ones((10, 10))
        suma = np.sum(array2)
        self.df.iloc[1,1]=str(suma)
        print("ejercicio2", suma)
        
    def ejercicio3(self):

        # Generar dos arrays de tamaño 5 con números aleatorios entre 1 y 10
        array1 = np.random.randint(1, 11, 5)
        array2 = np.random.randint(1, 11, 5)
        # Realizar el producto elemento a elemento
        producto = array1 * array2
        self.df.iloc[2,1]=str(producto)
        print("Array 1:", array1)
        print("Array 2:", array2)
        print("ejercicio3", producto)

    def ejercicio4(self):
        


  


        #print("array del 10 al 29")
        #print(array_10_29)
     def ejecutar(self):
        self.ejercicio1()
        self.ejercicio2()
        self.ejercicio3()
        self.ejercicio4()


        self.df.to_excel("Actividad_2.xlsx")
ene= ejercicios()
ene.ejecutar()

        

        


