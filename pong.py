import pygame #inicializar la librería

class Pong:

    def __init__(self) :
        print("Construyendo un objeto de la clase pong")
        pygame.init()
        self.pantalla = pygame.display.set_mode((600, 300))  #crear la pantalla para el juego

    def bucle_principal(self): #creación del bucle principal para que el juego permanezca abierto para ir actualizandose.
        print("Bucle pral")
        while True: 
            #dibujo un rectangulo
            pygame.draw.rect(self.pantalla, (245,184,65), pygame.Rect(30,60,100,150))
            pygame.display.flip()  #borra la pantalla y el bucle la vuelve a pintar

if __name__ == "__main__":
    juego = Pong()  #inicia el constructor
    juego.bucle_principal() #llamada al bucle principal