import pygame
from configuracion import *

def movimiento(tecla, personajeP):

    if tecla[pygame.K_a] and personajeP.x - velocidad - personajeP.width//2 > 0:
            
        personajeP.x -= velocidad

    if tecla[pygame.K_d] and personajeP.x + velocidad + personajeP.width//2 < ancho :

        personajeP.x += velocidad
    
    if tecla[pygame.K_w] and personajeP.y - velocidad - personajeP.height//2 > 0:

        personajeP.y -= velocidad

    if tecla[pygame.K_s] and personajeP.y + velocidad + personajeP.height//2 < alto:

        personajeP.y += velocidad