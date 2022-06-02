from io import open

archivoTexto = open("achivo.txt", "w")

frase = "Vamos a ser Full Stack"

archivoTexto.write(frase)
