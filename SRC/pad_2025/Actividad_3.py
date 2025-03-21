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
            "":[0],
            "Granadilla": [20],
            "Tomates": [50]})
        ruta_ej1 = os.path.join(self.ruta_Actividad_3, "Ejercicio_1.csv")
        frutas.to_csv(ruta_ej1, index=False)

    def ejecutar(self):
        self.ejercicio1()
        #self.ejercicio2()
        #self.ejercicio3()
      

        
        self.df.to_csv(f"{self.ruta_Actividad_3}/Actividad_3.csv", index=False)
ene= ejercicios()
ene.ejecutar()

        