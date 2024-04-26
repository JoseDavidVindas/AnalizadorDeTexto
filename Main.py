texto =input("Ingresa el texto que gustes:")
letras = []

texto = texto.lower()

letras.append(input("Ingrese la primera letra:").lower())
letras.append(input("Ingrese la segunda letra:").lower())
letras.append(input("Ingrese la tercera letra:").lower())

print("\n")
print("La cantidad de letras es")
cantidad_letras1 = texto.count(letras[0])
cantidad_letras2 = texto.count(letras[1])
cantidad_letras3 = texto.count(letras[2])
print(f"Se ha encontrado la letra '{letras[0]}' repetida {cantidad_letras1} veces")
print(f"Se ha encontrado la letra '{letras[1]}' repetida {cantidad_letras2} veces")
print(f"Se ha encontrado la letra '{letras[2]}' repetida {cantidad_letras3} veces")

print("\n")
print("La cantidad de palabras es")
palabras = texto.split()
print(f"Se ha encontrado {len(palabras)}")

print("\n")
print("Letras de inicio y fin")
letra_inicio = texto[0]
letra_fin = texto[-1]
print(f"La letra inicial es {letra_inicio} y la letra final es {letra_fin}")

print("\n")
print("Texto invertido")
palabras.reverse()
texto_invertido = ''.join(palabras)
print(f"El texto de manera invertida se ve como: '{texto_invertido}'")

print("\n")
print("Buscando la palabra python")
buscar_python = 'python' in texto
dic = {True: "sí", False: "no"}
print(f"La palabra 'Python'{dic[buscar_python]} se encuentra en el texto")
