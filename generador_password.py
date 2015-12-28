#/usr/bin/python3

from random import choice
from string import ascii_letters , digits


print("""
 _ __   __ _ ___ _____      _____  _ __ __| |
| '_ \ / _` / __/ __\ \ /\ / / _ \| '__/ _` |
| |_) | (_| \__ \__ \\ V  V / (_) | | | (_| |
| .__/ \__,_|___/___/ \_/\_/ \___/|_|  \__,_|
|_|                                          
                                 _             
  __ _  ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
 / _` |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
| (_| |  __/ | | |  __/ | | (_| | || (_) | |   
 \__, |\___|_| |_|\___|_|  \__,_|\__\___/|_|   
 |___/                                        


By : https://www.facebook.com/archdesktop""")


lgtn = int(input("¿De que longitud desea generar la clave?: "))
claves = int(input("¿Cuantas claves deseas generar: "))
caracteres = ascii_letters + digits

for i in range(claves):
    final = ''.join([choice (caracteres) for i in range(lgtn)])
    print (final)
