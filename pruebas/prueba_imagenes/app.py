from PIL import Image

im = Image.open("imagen1.png")
""" im.show() # Abre una nueva ventana con la imagen imagen1.png () """
print(im.format, im.size, im.mode) # Muestra el formato, tamaño y modo (si es RGBA y eso)

box = (200,200,600,600)
region = im.crop(box) # Recorta una imagen tomando como parámetros los valores de 'box'
region.save("recorte.png") # Guarda 'region' en "recorte.png"

r, g, b, a = region.split() # Divide el RGB de region
region = Image.merge("RGB", (b, g, r)) # Cambia los valores de rgb en region, y los combina
region.save("cambio.png") # Guarda el region actual (con rgb intercambiado) en "cambio.png"

out = region.rotate(45) # Rotar la imagen 45 grados
out.save("giro.png") # Guarda 'out' en "giro.png"