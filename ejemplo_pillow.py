from PIL import Image

imagen = Image.open("imagen.png.png")

print("Tamaño:", imagen.size)
print("Formato:", imagen.format)
print("Modo:", imagen.mode)

imagen_redimensionada = imagen.resize((300, 300))
imagen_gris = imagen_redimensionada.convert("L")

imagen_gris.save("imagen_modificada.jpg")

print("Proceso finalizado correctamente.")
