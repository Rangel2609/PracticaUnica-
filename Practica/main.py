import json
nombres = []
def cargar_datos(ruta):
    with open(ruta) as contenido:
        nombres = json.load(contenido)
        x = input("Escribe el campo a encontrar el minimo")
        for nombre in nombres:
            atributo = nombre.get(x)
            print(atributo)
            return (atributo)
if __name__ == '__main__':
    ruta = "Archivo2.json"
    cargar_datos(ruta)



