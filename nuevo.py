
import os

# Directorio del USB y destino donde se guardarán las imágenes recuperadas
directorio_usb = r'\\.\D:'  # Cambia esto a la ruta correcta de tu dispositivo USB
directorio_destino = './imagenes_recuperadas'
contador = 0

# Crear el directorio de destino si no existe
if not os.path.exists(directorio_destino):
    os.makedirs(directorio_destino)

# Abrir el dispositivo USB en modo lectura binaria
with open(directorio_usb, 'rb') as usb:
    while True:
        # Leer datos en bloques de 1024 bytes
        datos = usb.read(1024)

        # Si no hay datos, terminar el bucle
        if not datos:
            break

        # Buscar el inicio de la imagen PNG (delimitador PNG \x89PNG\r\n\x1a\n)
        inicio = datos.find(b'\x89PNG\r\n\x1a\n')
        while inicio != -1:
            # Buscar el fin de la imagen PNG (delimitador PNG IEND\xae\x42\x60\x82)
            fin = datos.find(b'IEND\xae\x42\x60\x82', inicio)
            if fin != -1:
                # Calcular la longitud de la imagen
                longitud_archivo = fin + 8 - inicio  # 8 bytes es la longitud de IEND y su checksum
                # Guardar la imagen recuperada
                with open(os.path.join(directorio_destino, f'imagen_recuperada_{contador}.png'), 'wb') as img_file:
                    img_file.write(datos[inicio:inicio + longitud_archivo])
                contador += 1
                # Continuar buscando más imágenes PNG en el bloque de datos actual
                inicio = datos.find(b'\x89PNG\r\n\x1a\n', fin)
            else:
                # Leer más datos si no se encontró el final de la imagen
                datos_extra = usb.read(1024)
                if not datos_extra:
                    break
                datos += datos_extra
                continue
