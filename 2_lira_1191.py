print(" ")#espacio
print("Lira Hernandez Dayana Yamileth 1191")#datos
print(" ")#espacio

class Persona(): #crea una clase
    def __init__(self , nombre='' , edad=0):#define funcion 
        self.nombre=nombre #valor a nombre
        self.edad=edad #valor a edad

    def imprimir(self):#define funcion imprimir
        print(f"Nombre:{self.nombre} Edad {self.edad}")#imprime datos

    def mayor(self):#define funcion mayor
        return self.edad >= 18 #devuelve si edad es mayor q 18 

persona = Persona("Dayana", 15)#imprime datos
persona.imprimir()#imprime datos

print ("Es mayor de edad:", persona.mayor())#imprime mensaje
print(" ")#espacio