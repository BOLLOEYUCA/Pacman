import pygame
from configuracion import *

class Jugador:

    def __init__(self):

       self.color = amarillo

    def dibujarJugador(self):

        pygame.draw.circle(pantalla, amarillo, (personajeP.x, personajeP.y), 10)

personajeP = pygame.Rect(250, 250, 20, 20)