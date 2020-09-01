import json
campos = ["Apex Pro", "Apple Magic Keyboard"];
def cargar_datos(ruta):
    with open(ruta) as contenido:
        nombres = json.load(contenido)
        x = input("Escribe el nombre a encontrar")

        for nombre in nombres:
            atributo = nombre.get(min(x))
            print(atributo)
if __name__ == '__main__':
    ruta = "Archivo2.json"
    cargar_datos(ruta)
