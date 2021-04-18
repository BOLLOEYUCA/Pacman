import pygame
from configuracion import *
from tablero import *
from personaje import *
from teclas import *

jugador = Jugador()

def main():

    reloj = pygame.time.Clock()
    activar = True

    while activar:

        reloj.tick(fps)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                activar = False
        
        tecla = pygame.key.get_pressed()

        movimiento(tecla, personajeP)

        pantalla.blit(tablero, (0, 0))
        
        jugador.dibujarJugador()
              
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":

    main()

#resize = pygame.transform.scale(var que contiene la foto, (acho, alto))
#rotar = pygame.transform.rotate(lo que se va a rotar, angulo)