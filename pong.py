import pygame #inicializar la librería

ANCHO = 640
ALTO = 480
COLOR = (245,184,65)


class Pong:

    def __init__(self) :
        pygame.init()
        self.pantalla = pygame.display.set_mode((ANCHO, ALTO))  #crear la pantalla para el juego

    def bucle_principal(self): #creación del bucle principal para que el juego permanezca abierto para ir actualizandose.
        salir = False
        while not salir: 
            #creamos un evento para salir del bucle cuando le demos a salir en el display
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    salir = True

            #dibujo un rectangulo
            pygame.draw.rect(self.pantalla, (COLOR), pygame.Rect(30,60,100,150))
            pygame.display.flip()  #borra la pantalla y el bucle la vuelve a pintar

if __name__ == "__main__":
    juego = Pong()  #inicia el constructor
    juego.bucle_principal() #llamada al bucle principal