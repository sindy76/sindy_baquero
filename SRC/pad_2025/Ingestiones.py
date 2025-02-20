import json



class Ingestiones():
    def __init__(self):
        self.ruta_static = "G:/P_Paola/IUD/Analitica de dato/Reposotorio/sindy_baquero/SRC/pad_2025/Static/"
    def leer_json(self):
        # r read w write
        ruta_json="{}Json/Datos_personas.json".format(self.ruta_static)
        datos=""
        with open(ruta_json, "r", encoding="utf-8") as f:
            datos = json.load(f)
        return datos
             
    def leer_txt(self):
        # r read w write
        ruta_json="{}Txt/Info.txt".format(self.ruta_static)
        datos=""
        with open(ruta_json, "r", encoding="utf-8") as f:
            datos = f.read()
        return datos        

inges= Ingestiones()
datos_json = inges.leer_json()
print(datos_json)
print("**********************************************************************")
print("**********************************************************************")
datos_txt = inges.leer_txt()
print(datos_txt)
