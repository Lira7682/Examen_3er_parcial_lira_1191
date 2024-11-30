print(" ")#espacio
print("Lira Hernandez Dayana Yamileth 1191")#datos
print(" ")#espacio

class Alumno(): #crea una clase 
    def __init__(self , nombre , nota):#define funcion
        self.nombre=nombre #da valores
        self.nota=nota #da valores

    def imprimir(self):#define funcion
        print(f"»Nombre:{self.nombre} \nNota: {self.nota}»")#imprime mensaje

    def resultados(self):#define funcion
        if self.nota >= 7: #verifica si la condicion es verdadera
            print("«Has APROBADO!»")#imprime mensaje
        else:#verifica si la condicion es falsa
            print("«Has REPROBADO!»")#imprime mensaje

estudiante=Alumno("Dayana" , 8)#imprime datos
estudiante.imprimir()#imprime
estudiante.resultados()#imprime resultados

print(" ")#espacio