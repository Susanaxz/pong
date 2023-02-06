import pygame

ANCHO = 800
ALTO = 600
COLOR = (245, 184, 65)
COLOR_PANTALLA = (86, 110, 61)

ANCHO_PALETA = 10
ALTO_PALETA = 40
MARGEN_LATERAL = 40
MARGEN = 40

TAM_PELOTA = 10
TAM_LINEA = 5


class Jugador(pygame.Rect):
    def __init__(self, pos_x, pos_y):
        self.rectangulo = pygame.Rect(pos_x, pos_y, ANCHO_PALETA, ALTO_PALETA)

    def pintame(self, pantalla):
        pygame.draw.rect(pantalla, COLOR, self.rectangulo)


class Pelota(pygame.Rect):
    def __init__(self, x, y):
        self.rectangulo = pygame.Rect(x, y, TAM_PELOTA, TAM_PELOTA)

    def pintame(self, pantalla):
        pygame.draw.rect(pantalla, COLOR, self.rectangulo)


class Pong:
    def __init__(self):
        
        pygame.init()
        # Crear la Pantalla para el juego
        self.pantalla = pygame.display.set_mode((ANCHO, ALTO))
        # importar una imagen de fondo
        
        pos_y = (ALTO - ALTO_PALETA) / 2
        pos_x_2 = ANCHO - MARGEN_LATERAL - ANCHO_PALETA
        self.jugador1 = Jugador(MARGEN_LATERAL, pos_y)
        self.jugador2 = Jugador(pos_x_2, pos_y)
        pelota_x = (ANCHO - TAM_PELOTA) / 2
        pelota_y = (ALTO - TAM_PELOTA) / 2
        
        self.pelota = Pelota(pelota_x, pelota_y)
        
    def bucle_principal(self):  # bucle principal para que el juego permanezca abierto para ir actualizándose.
        salir = False
        while not salir:
            # creamos un evento para salir del bucle cuando le demos a salir en el display
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    salir = True
                    # salir con la tecla escape
                if evento.type == pygame.KEYUP:
                    if evento.key == pygame.K_ESCAPE:
                        salir = True
                    # evento capturamos teclas de movimiento
                    elif evento.key == pygame.K_a:
                        print("Jugador 1 - Arriba")
                    elif evento.key == pygame.K_z:
                        print("Jugador 1 - Abajo")    
                    elif evento.key == pygame.K_UP:
                        print("Jugador 2 - Arriba")
                    elif evento.key == pygame.K_DOWN:
                        print("Jugador 2 - Abajo")    
                                    
            self.pantalla.fill(COLOR_PANTALLA)
            
            fondo = pygame.image.load("img/campo.png").convert_alpha()  # importar
            self.pantalla.blit(fondo, (0, 0))  # posición de la imagen en pantalla 
            
            # pintar la red cada vez que se borre la pantalla           
            # self.pinta_red()
            
            # dibujo un rectangulo (x, y, ancho, alto)
            self.jugador1.pintame(self.pantalla)
            self.jugador2.pintame(self.pantalla)
            
            
           
            self.pelota.pintame(self.pantalla)
            
            pygame.display.flip()  # borra la pantalla y el bucle la vuelve a pintar.

    def pinta_red(self):
        tramo_pintado = 15
        tramo_vacio = 5
        for i in range(MARGEN, ALTO-MARGEN, tramo_pintado+tramo_vacio):
                pygame.draw.line(self.pantalla, COLOR, (ANCHO/2, i), (ANCHO/2, i+tramo_pintado), TAM_LINEA)


if __name__ == "__main__":
    juego = Pong()  # inicia el constructor
    juego.bucle_principal()  # llamada al bucle principal
