import  json
import webbrowser
print("Bienvenido")
input("Presione entrer para continuar")
def opciones():
    print("")
print("1.Cargar")
print("2.Seleccionar")
print("3.Maximo")
print("4.Minimo")
print("5.Suma")
print("6.Cuenta")
print("7.Reportar")


while True:
	opciones()

	seleccion = input("Ingresa el numero a tu seleccion:"+ "")

	if seleccion=="1":
		print ("Usted a seleccionado Cargar")
		y = input("Escriba el nombre del archivo que desea abrir")
		print("1. Vuelve al menu Principal ")
		print("2. Mostrar Archivos cargados")


		with open(y, "r") as file:
			CARGAR = json.loads(file.read())
			print(CARGAR)
			print("Aqui estan los datos cargados")
		break
	elif seleccion=="2":
		print ("Usted a seleccionado Seleccionar")



		def cargar_datos(ruta):
			with open(ruta) as contenido:
				nombres = json.load(contenido)
				x = input("Ingrese el campo")
				for nombre in nombres:
					edad = nombre.get('Edad')
					print(edad)
		if __name__ == '__main__':
			ruta = "Archivo2.json"
			cargar_datos(ruta)
		break
	elif seleccion=="3":
		print ("Usted a seleccionado Maximo")
		break
	elif seleccion=="4":
		print("Usted a seleccionado Minimo")
		break
	elif seleccion=="5":
		print("Usted a seleccionado Suma")
		break
	elif seleccion=="6":
		print("Usted a seleccionado Cuenta")
		with open("Archivo2.json") as f:
			y = input("Escriba el nombre del archivo que desea saber su numero de registros")
			with open(y, "r") as file:
				CARGAR = json.loads(file.read())
				print(CARGAR)
			contador = 0
			for registros in CARGAR:
				contador = contador + 1
				print(contador)
				print("Tiene un total de:"+ str(contador) +  "registros")
		break
	elif seleccion=="7":
		print("Usted a seleccionado Reportar")
		f = open("tarea.html", "wb")
		la = """<html>
		<head>
		<meta charset="utf8" />
		<title>Registros</title>
		<script src="bla.js"></script>
		</head>
		<style type="text/css">
		body{background-color: chartreuse;}
		h1{text-align: center;}
		.opciones {
		    width: 100%;
		    background-color: red;
		    display:flex;
		    justify-content:center;
		    width: 1000px;
		    height: 700px;
		}
		.nav{align-content: center;}
		</style>
		<body>
		<table id= "tabla">

		</table>
		</body>


		</html>"""
		f.write(bytes(la, "ascii"))
		f.close()
		webbrowser.open_new_tab("tarea.html")

		break
	else:
		print("Seleccione una opcione que sea valida")




