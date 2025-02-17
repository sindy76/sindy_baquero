# class relacion directa con un objeto (entidad o objeto)
# def  - acciones o funciones del objeto

class Personas():
    def __init__(self):
        #atributos del objeto
            self.nombre = "camilo" #variable de tipo texto ""
            self.edad = 0 #variable de tipo numerico
            self.estatura = 100.0 #variable de tipo decimal 
            self.peso = 35.6 #variable de tipo decimal 


personas =Personas()
personas.edad = 42
personas.estatura = 193
print("nombre: ", personas.nombre,"edad:", personas.edad, "Cms: ", personas.estatura)
