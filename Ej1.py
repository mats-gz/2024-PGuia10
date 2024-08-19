from PIL import Image

def color_pixeles(imagen_ruta, tono_buscado):
    
    with Image.open(imagen_ruta) as imagen:
        imagen = imagen.convert("L")

    ancho_imagen, alto_imagen = imagen.size
    pixeles_finales = {}
    
    for x in range(ancho_imagen):
        for y in range(alto_imagen):
            tono_pixel = imagen.getpixel((x, y))
            if tono_pixel == tono_buscado:
                pixeles_finales[(x, y)] = tono_pixel
    
    return pixeles_finales

imagen_ruta = "flor.jpg"
tono_buscado = 255
pixeles_encontrados = color_pixeles(imagen_ruta, tono_buscado)

for posicion, tono in pixeles_encontrados.items():
    print(f"Posición: {posicion}, Tono: {tono}")
