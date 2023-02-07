import pygame
from random import randint

ANCHO = 800
ALTO = 600
FPS = 40
COLOR = (245, 184, 65)
COLOR_PANTALLA = (86, 110, 61)

ANCHO_PALETA = 10
ALTO_PALETA = 40
MARGEN_LATERAL = 40
MARGEN = 40

TAM_PELOTA = 10
TAM_LINEA = 5


class Jugador(pygame.Rect):

    ARRIBA = True
    ABAJO = False
    VELOCIDAD = 5

    def __init__(self, pos_x, pos_y):
        super(Jugador, self).__init__(
            pos_x, pos_y, ANCHO_PALETA, ALTO_PALETA
        )  # si tengo una herencia tenemos que llamar al constructor del padre.

    def pintame(self, pantalla):
        pygame.draw.rect(pantalla, COLOR, self)  # pinto el rectángulo

    def muevete(self, direccion):
        if direccion == self.ARRIBA:
            self.y = self.y - self.VELOCIDAD
            if self.y < 0:
                self.y = 0

        else:
            self.y = self.y + self.VELOCIDAD
            if self.y > ALTO - ALTO_PALETA:
                self.y = ALTO - ALTO_PALETA


class Pelota(pygame.Rect):

    velocidad_x = randint(-5, 5) #creamos la velocidad de la pelota de forma aleatoria
    velocidad_y = randint(-5, 5)

    def __init__(self, x, y):
        super(Pelota, self).__init__(
            x, y, TAM_PELOTA, TAM_PELOTA
        )  # metodo constructor del método que heredo

    def pintame(self, pantalla):
        pygame.draw.rect(pantalla, COLOR, self)

    def mover(self):
        self.x = self.x + self.velocidad_x
        self.y = self.y - self.velocidad_y
        #rebote de la pelota
        if self.y <=0:
            self.y = 0
            self.velocidad_y = -self.velocidad_y
        if self.y >= ALTO - TAM_PELOTA:
            self.y = ALTO - TAM_PELOTA
            self.velocidad_y = -self.velocidad_y
     
    def colisionar(self, jugador):
        if self.colliderect(jugador):
            self.velocidad_x = -self.velocidad_x

class Pong:
    def __init__(self):

        pygame.init()
        # Crear la Pantalla para el juego
        self.pantalla = pygame.display.set_mode((ANCHO, ALTO))
        self.pantalla.fill(COLOR_PANTALLA)
        # importar una imagen de fondo
        fondo = pygame.image.load("img/campo.png").convert_alpha()  # importar
        self.pantalla.blit(fondo, (-1, 0))  # posición de la imagen en pantalla
        # visualizar
        pos_y = (ALTO - ALTO_PALETA) / 2
        pos_x_2 = ANCHO - MARGEN_LATERAL - ANCHO_PALETA
        self.jugador1 = Jugador(MARGEN_LATERAL, pos_y)
        self.jugador2 = Jugador(pos_x_2, pos_y)
        pelota_x = (ANCHO - TAM_PELOTA) / 2
        pelota_y = (ALTO - TAM_PELOTA) / 2
        linea_x = (ANCHO - TAM_LINEA) / 2
        self.pelota = Pelota(pelota_x, pelota_y)
        # self.linea = pygame.draw.lines(self.pantalla, COLOR, True, [(linea_x, 0),(linea_x,ALTO)], TAM_LINEA)

    def bucle_principal(
        self,
    ):  # bucle principal para que el juego permanezca abierto para ir actualizándose.
        salir = False
        while not salir:
            # creamos un evento para salir del bucle cuando le demos a salir en el display
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    salir = True
                    # salir con la tecla escape
                if evento.type == pygame.KEYUP:
                    if evento.tecla == pygame.K_ESCAPE:
                        salir = True

            # dibujo un rectangulo (x, y, ancho, alto)
            self.jugador1.pintame(self.pantalla)
            self.jugador2.pintame(self.pantalla)
            self.pelota.pintame(self.pantalla)

            pygame.display.flip()  # borra la pantalla y el bucle la vuelve a pintar.


if __name__ == "__main__":
    juego = Pong()  # inicia el constructor
    juego.bucle_principal()  # llamada al bucle principal
