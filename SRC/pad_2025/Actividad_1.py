
import json
import requests
import sys
sys.stdout.reconfigure(encoding='utf-8') 

class Ingestiones():
    def __init__(self):
        self.ruta_static="SRC/pad_2025/Static/"
        
    def  leer_api(self,url="https://api.disneyapi.dev/character"):
         response = requests.get(url)
         return response.json()

    def escribir_json(self,nombre,datos):
        # r read w write

        ruta_json = "{}/Json/{}".format(self.ruta_static,nombre)
        with open(ruta_json,"w",encoding="utf-8") as f:
            json.dump(datos,f,indent=4,ensure_ascii=False)
        
        
inges = Ingestiones() 
datos_api = inges.leer_api()
print(datos_api)

inges.escribir_json("Actividad_1.json", datos_api)