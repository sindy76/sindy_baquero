import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

class ejercicios:
    def __init__(self):
        datos = [(i, None) for i in range(1, 22)] 
        self.df= pd.DataFrame(data=datos,columns=["#ejercicio", "valor"])
        self.ruta_raiz=os.path.abspath(os.getcwd())
        self.ruta_Actividad_3 = "{}/SRC/pad_2025/Actividad_3/".format(self.ruta_raiz)

    def ejercicio1(self):

        # Crea un DataFrame frutas
        frutas = pd.DataFrame({
            "Granadilla": [20],
            "Tomates": [50]})
        ruta_ej1 = os.path.join(self.ruta_Actividad_3, "Ejercicio_1.csv")
        frutas.to_csv(ruta_ej1, index=False)
        print(frutas)

    def ejercicio2(self):
        # Crea un DataFrame ventas_frutas que coincida con el diagrama:
        ventas_frutas = pd.DataFrame(
    {"Granadilla": [20, 49], "Tomates": [50, 100]},
    index=["ventas 2021", "ventas 2022"])
        ruta_ej2 = os.path.join(self.ruta_Actividad_3, "Ejercicio_2.csv")
        ventas_frutas.to_csv(ruta_ej2, index=True)
        print(ventas_frutas)


    def ejercicio3(self):
        #Crea una variable utensilios con una Serie que tenga el siguiente aspecto:
        utensilios = pd.Series(
    data=["3 unidades", "2 unidades", "4 unidades", "5 unidades"],
    index=["Cuchara", "Tenedor", "Cuchillo", "Plato"],
    name="cocina")
        ruta_ej3 = os.path.join(self.ruta_Actividad_3, "Ejercicio_3.csv")
        utensilios.to_csv(ruta_ej3, index=True)
        print(utensilios)
       

                          


    def ejecutar(self):
        self.ejercicio1()
        self.ejercicio2()
        self.ejercicio3()
      

        
        self.df.to_csv(f"{self.ruta_Actividad_3}/Actividad_3.csv", index=False)
ene= ejercicios()
ene.ejecutar()

        