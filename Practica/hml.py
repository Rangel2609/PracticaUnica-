import webbrowser

f= open("HtmlPage.html", "wb")

mensaje = """<html>
<head> Archivo Exportado</head>
<body><p>Hola Mundo!</p></body>
</html>"""

f.write(bytes(mensaje, "ascii"))
f.close()

webbrowser.open_new_tab("HtmlPage.html")
