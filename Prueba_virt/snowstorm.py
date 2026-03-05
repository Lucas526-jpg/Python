import os, random, time, sys

ARRIBA = chr(9600)
ABAJO = chr(9604)
COMPLETO = chr(9608)
DENSIDAD = 4

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

#os.system ejecuta el texto que esta en el parentesis como si fuera escrito desde la terminal
#os.name devuelve el nombre del sistema operativo(nt si es windows, posix si es linux o mac)

if len(sys.argv) > 1:
    try:
        DENSIDAD = int(sys.argv[1])
    except ValueError:
        pass

try:
    while True:
        limpiar_pantalla()

        for i in range(20):
            for j in range(20):
                if random.randint(0,99) < DENSIDAD:
                    print(random.choice([ARRIBA,ABAJO]), end="")
                else:
                    print(" ", end="")
            print()

        print(COMPLETO * 20 + "\n" + COMPLETO * 20)
        print('(Presiona Ctrl-C para detener.)')
        time.sleep(0.2)
        
except KeyboardInterrupt:
    print("\n¡Tormenta detenida!")