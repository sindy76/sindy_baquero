import pandas as pd
import kagglehub
import os
import zipfile
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import tkinter
# tkinter._test()
import numpy as np

class ejercicios:
    def __init__(self):
        datos = [(i, None) for i in range(1, 13)] 
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
        self.df.loc[0, "valor"] = ruta_ej1
        print(frutas)

    def ejercicio2(self):
        # Crea un DataFrame ventas_frutas que coincida con el diagrama:
        ventas_frutas = pd.DataFrame(
    {"Granadilla": [20, 49], "Tomates": [50, 100]},
    index=["ventas 2021", "ventas 2022"])
        ruta_ej2 = os.path.join(self.ruta_Actividad_3, "Ejercicio_2.csv")
        ventas_frutas.to_csv(ruta_ej2, index=True)
        self.df.loc[1, "valor"] = ruta_ej2
        print(ventas_frutas)


    def ejercicio3(self):
        #Crea una variable utensilios con una Serie que tenga el siguiente aspecto:
        utensilios = pd.Series(
    data=["3 unidades", "2 unidades", "4 unidades", "5 unidades"],
    index=["Cuchara", "Tenedor", "Cuchillo", "Plato"],
    name="cocina")
        ruta_ej3 = os.path.join(self.ruta_Actividad_3, "Ejercicio_3.csv")
        utensilios.to_csv(ruta_ej3, index=True)
        self.df.loc[2, "valor"] = ruta_ej3
        print(utensilios)

    def ejercicio4(self):
        #Descarga el dataset 'wine review' desde Kaggle y cárgalo en un DataFrame llamado review, tal y como se muestra en la figura.
        print("Descargando dataset desde Kaggle...")
        dataset_path = kagglehub.dataset_download("zynicide/wine-reviews")
        print(f"Dataset descargado en: {dataset_path}")

        # Extraer el contenido del archivo ZIP
        extracted_dir = self.extract_zip_files(dataset_path)

        # Procesar el archivo CSV
        review = self.create_review_csv(extracted_dir)

        # Mostrar el DataFrame para verificar que se cargó correctamente
        print("DataFrame 'review' cargado exitosamente:")
        print(review.head())

    def extract_zip_files(self, dataset_path):
        zip_files = [f for f in os.listdir(dataset_path) if f.endswith('.zip')]
        if zip_files:
            zip_file = os.path.join(dataset_path, zip_files[0])
            extract_dir = os.path.join(dataset_path, "extracted")
            os.makedirs(extract_dir, exist_ok=True)
            print(f"Extrayendo {zip_file} en {extract_dir}...")
            with zipfile.ZipFile(zip_file, "r") as z:
                z.extractall(extract_dir)
            return extract_dir
        else:
            # Verificar si hay archivos CSV
            csv_files = [f for f in os.listdir(dataset_path) if f.endswith('.csv')]
            if csv_files:
                print("No se encontró archivo ZIP pero se detectaron archivos CSV; se asume que el dataset ya está extraído.")
                return dataset_path
            else:
                raise FileNotFoundError("No se encontró ningún archivo .zip ni archivos .csv en la ruta del dataset.")

    def create_review_csv(self, csv_dir):
        csv_files = [f for f in os.listdir(csv_dir) if f.endswith('.csv')]
        if not csv_files:
            raise FileNotFoundError("No se encontraron archivos CSV en el directorio extraído.")

        for file in csv_files:
            file_path = os.path.join(csv_dir, file)
            print(f"Leyendo {file_path}...")
            try:
                review = pd.read_csv(file_path, encoding="latin1")
                output_file = os.path.join(self.ruta_Actividad_3, "review.csv")
                review.to_csv(output_file, index=False)
                self.df.loc[3, "valor"] = output_file
                print(f"Archivo 'wine review' guardado correctamente en: {output_file}")
                return review  # Retorna el DataFrame para futuros usos
            except Exception as e:
                print(f"Error al leer {file}: {e}")
                continue
    def ejercicio5(self):
        ruta_review = os.path.join(self.ruta_Actividad_3, "review.csv")
        ruta_nuevo_csv = os.path.join(self.ruta_Actividad_3, "Ejercicio_5.csv")

        if os.path.exists(ruta_review):
            review = pd.read_csv(ruta_review)
            primeras_filas = review.head(2)
            primeras_filas.to_csv(ruta_nuevo_csv, index=False)
            self.df.loc[4, "valor"] = ruta_nuevo_csv
            print(f"Se ha creado el archivo: {ruta_nuevo_csv}")
            print(primeras_filas)

    def ejercicio6(self):
    #Utiliza el método .info() para averiguar cuántas entradas hay. ¿Cuántas encontraste?

      ruta_review = os.path.join(self.ruta_Actividad_3, "review.csv")
      ruta_salida = os.path.join(self.ruta_Actividad_3, "Ejercicio_6.txt")
      if os.path.exists(ruta_review):
        review = pd.read_csv(ruta_review)
        with open(ruta_salida, "w", encoding="utf-8") as f:
            review.info(buf=f)  # Guarda el resultado de .info() en el archivo
        self.df.loc[5, "valor"] = ruta_salida
        print(f"Información del DataFrame guardada en: {ruta_salida}")
        print("Resumen de .info():")
        review.info()  # Muestra la información en consola también

    def ejercicio7(self):  
        #¿Cuál es el precio promedio?
        ruta_review = os.path.join(self.ruta_Actividad_3, "review.csv")
        ruta_salida = os.path.join(self.ruta_Actividad_3, "Ejercicio_7.txt")
        if os.path.exists(ruta_review):
            review = pd.read_csv(ruta_review)
            precio_promedio = review["price"].mean()
            with open(ruta_salida, "w", encoding="utf-8") as f:
                f.write(f"Precio promedio: {precio_promedio:.2f}")
            self.df.loc[6, "valor"] = ruta_salida
            print(f"Precio promedio: {precio_promedio:.2f}")
            print(f"Resultado guardado en: {ruta_salida}")

    def ejercicio8(self):
        #¿Cuál es el precio más alto pagado?
        ruta_review = os.path.join(self.ruta_Actividad_3, "review.csv")
        ruta_salida = os.path.join(self.ruta_Actividad_3, "Ejercicio_8.txt")
        if os.path.exists(ruta_review):
            review = pd.read_csv(ruta_review)
            precio_maximo = review["price"].max()
            with open(ruta_salida, "w", encoding="utf-8") as f:
                f.write(f"Precio máximo: {precio_maximo:.2f}")
            self.df.loc[7, "valor"] = ruta_salida
            print(f"Precio máximo: {precio_maximo:.2f}")
            print(f"Resultado guardado en: {ruta_salida}")

    def ejercicio9(self):
        #Crea un DataFrame con todos los vinos de california.
        ruta_review = os.path.join(self.ruta_Actividad_3, "review.csv")
        ruta_salida = os.path.join(self.ruta_Actividad_3, "Ejercicio_9.csv")
        if os.path.exists(ruta_review):
            review = pd.read_csv(ruta_review)
            vinos_california = review[review["province"] == "California"]
            vinos_california.to_csv(ruta_salida, index=False)
            self.df.loc[8, "valor"] = ruta_salida
            print("Vinos de California:")
            print(vinos_california)

    def ejercicio10(self):
        #Utiliza idxmax() para encontrar el índice del vino con el precio más alto y luego utiliza loc para obtener toda la información de ese vino específico.
        ruta_review = os.path.join(self.ruta_Actividad_3, "review.csv")
        ruta_salida = os.path.join(self.ruta_Actividad_3, "Ejercicio_10.txt")
        if os.path.exists(ruta_review):
            review = pd.read_csv(ruta_review)
            idx_precio_max = review["price"].idxmax()
            vino_precio_max = review.loc[idx_precio_max]
            with open(ruta_salida, "w", encoding="utf-8") as f:
                f.write(f"Vino con precio más alto:\n{vino_precio_max}")
            self.df.loc[9, "valor"] = ruta_salida
            print("Vino con precio más alto:")
            print(vino_precio_max)

    def ejercicio11(self):
        #¿Cuáles son los tipos de uva más comunes en California?
        ruta_review = os.path.join(self.ruta_Actividad_3, "review.csv")
        ruta_salida = os.path.join(self.ruta_Actividad_3, "Ejercicio_11.txt")
        if os.path.exists(ruta_review):
            review = pd.read_csv(ruta_review)
            uvas_california = review[review["province"] == "California"]["variety"].value_counts()
            with open(ruta_salida, "w", encoding="utf-8") as f:
                f.write(f"Tipos de uva más comunes en California:\n{uvas_california}")
            self.df.loc[10, "valor"] = ruta_salida
            print("Tipos de uva más comunes en California:")
            print(uvas_california)

    def ejercicio12(self):
        # ¿Cuáles son los 10 tipos de uva más comunes en California?
        ruta_review = os.path.join(self.ruta_Actividad_3, "review.csv")
        ruta_salida = os.path.join(self.ruta_Actividad_3, "Ejercicio_12.csv")
        if os.path.exists(ruta_review):
            review = pd.read_csv(ruta_review)
            uvas_california = review[review["province"] == "California"]["variety"].value_counts().head(10)
            uvas_california = uvas_california.rename_axis("variety").reset_index(name="count")  # Convertir a DataFrame
            uvas_california.to_csv(ruta_salida, index=False, encoding="utf-8")
            self.df.loc[11, "valor"] = ruta_salida
            print("Los 10 tipos de uva más comunes en California son:")
            print(uvas_california)


    def ejecutar(self):
        self.ejercicio1()
        self.ejercicio2()
        self.ejercicio3()
        self.ejercicio4()
        self.ejercicio5()
        self.ejercicio6()
        self.ejercicio7()
        self.ejercicio8()
        self.ejercicio9()
        self.ejercicio10()
        self.ejercicio11()
        self.ejercicio12()


      

        
        self.df.to_csv(f"{self.ruta_Actividad_3}/Actividad_3.csv", index=False)
ene= ejercicios()
ene.ejecutar()

        