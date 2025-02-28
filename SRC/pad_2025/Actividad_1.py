
import json
import requests

class Ingestiones():
    def __init__(self):
        self.ruta_static="SRC/pad_2025/Static/"
        
    def leer_json(self):
        # r read w write

        ruta_json = "{}Json/Datos_personas.json".format(self.ruta_static)
        datos=""
        with open(ruta_json,"r",encoding="utf-8") as f:
            datos = json.load(f)
        return datos    
    
    def leer_txt(self):
        # r read w write

        ruta_json = "{}txt/info.txt".format(self.ruta_static)
        datos=""
        with open(ruta_json,"r",encoding="utf-8") as f:
            datos = f.read()
        return datos 

    def leer_varios_txt(self,nombre=""):
        # r read w write

        ruta_txt = "{}txt/{}".format(self.ruta_static,nombre)
        datos=""
        with open(ruta_txt,"r",encoding="utf-8") as f:
            datos = f.read()
        return datos 
      
    def  leer_api(self,url="https://dog.ceo/api/breeds/list/all"):
         response = requests.get(url)
         return response.json()

    
    def  leer_cualquier_excel(self,nombre=""):
        pass
    
    def  leer_cualquier_csv(self,nombre=""):
        pass
    
    def  leer_html(self,url=""):
        pass
    
    def  leer_bd(self,nombre_bd="",servidor="",puerto=0000):
        pass
    
    
    def escribir_txt(self,nombre,datos):
        # r read w write

        ruta_txt = "{}.txt".format(nombre)
        datos=""
        with open(ruta_txt,"w",encoding="utf-8") as f:
            #f.write(datos)
            f.writelines(datos)

    def escribir_json(self,nombre,datos):
        # r read w write

        ruta_json = "{}/json/{}".format(self.ruta_static,nombre)
        with open(ruta_json,"w",encoding="utf-8") as f:
            json.dump(datos,f,indent=4,ensure_ascii=False)
        
        

inges = Ingestiones() 
datos_json = inges.leer_json()
print(datos_json)
print("************************************************************")
print("************************************************************")
datos_txt = inges.leer_txt()
print(datos_txt)
print("************************************************************")
print("************************************************************")
nombre_archivo = "Info copia.txt"
datos_txt_dos = inges.leer_varios_txt(nombre_archivo)
print(datos_txt_dos)
print("************************************************************")
print("************************************************************")
datos_api = inges.leer_api()
print(datos_api)
print("************************************************************")
print("************************************************************")

inges.escribir_json("Entregable_1.json", datos_api)

#inges.escribir_json(nombre="entregable_json",datos=datos_api)
#inges.escribir_txt(nombre="archivo_json",datos=datos_json)
#inges.escribir_txt(nombre="archivo_txt",datos=datos_txt)
#inges.escribir_txt(nombre="archivo_txt_copy",datos=datos_txt_dos)
    

    


