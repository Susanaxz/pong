import pygame
from random import randint

ANCHO = 800
ALTO = 600
FPS = 60
COLOR = (245, 184, 65)
COLOR_PANTALLA = (86, 110, 61)
COLOR_BLCO = (255, 255, 255)
COLOR_K = (0, 0, 0)
PUNTOS_PARTIDA = 2


ANCHO_PALETA = 10
ALTO_PALETA = 60
MARGEN_LATERAL = 60
MARGEN = 40

TAM_PELOTA = 10
TAM_LINEA = 5
VEL_MAX_PELOTA = 5


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
    def __init__(self, x, y):
        super(Pelota, self).__init__(
            x, y, TAM_PELOTA, TAM_PELOTA
        )  # metodo constructor del método que heredo
        # creamos la velocidad de la pelota de forma aleatoria
        self.velocidad_y = randint(-VEL_MAX_PELOTA, VEL_MAX_PELOTA)
        self.velocidad_x = 0
        while self.velocidad_x == 0:
            self.velocidad_x = randint(-VEL_MAX_PELOTA, VEL_MAX_PELOTA)

    def pintame(self, pantalla):
        pygame.draw.rect(pantalla, COLOR, self)

    def mover(self):
        self.x = self.x + self.velocidad_x
        self.y = self.y - self.velocidad_y
        # rebote de la pelota
        if self.y <= 0:
            self.y = 0
            self.velocidad_y = -self.velocidad_y
        if self.y >= ALTO - TAM_PELOTA:
            self.y = ALTO - TAM_PELOTA
            self.velocidad_y = -self.velocidad_y

    def colisionar(self, jugador):
        if self.colliderect(jugador):
            self.velocidad_x = -self.velocidad_x

    def comprobar_punto(self):
        resultado = 0
        if self.x < 0:
            self.x = (ANCHO - TAM_PELOTA) / 2
            self.y = (ANCHO - TAM_PELOTA) / 2
            self.velocidad_y = randint(-VEL_MAX_PELOTA, VEL_MAX_PELOTA)
            self.velocidad_x = randint(-VEL_MAX_PELOTA, -1)
            print("punto para jug 2")
            resultado = 2

        if self.x > ANCHO:
            self.x = (ANCHO - TAM_PELOTA) / 2
            self.y = (ANCHO - TAM_PELOTA) / 2
            self.velocidad_y = randint(-VEL_MAX_PELOTA, VEL_MAX_PELOTA)
            self.velocidad_x = randint(1, VEL_MAX_PELOTA)
            print("punto para jug 1")
            resultado = 1
        return resultado


class Marcador:
    ganador = 0

    def __init__(self):
        self.tipo_letra = pygame.font.Font("font/VT323-Regular.ttf", 40, bold=True)
        self.reset()
        self.mostrar()

    def reset(self):
        self.puntuacion = [0, 0]
        self.ganador = 0

    def sumar_punto(self, jugador):
        self.puntuacion[jugador - 1] += 1
        self.mostrar()

    def comprobar_ganador(self):
        if self.puntuacion[0] == PUNTOS_PARTIDA:
            self.reset()
            self.ganador = 1

        if self.puntuacion[1] == PUNTOS_PARTIDA:
            self.reset()
            self.ganador = 2
        return self.ganador > 0

    def pintar_ganador(self, pantalla):
        txt = pygame.font.Font.render(
            self.tipo_letra, "The winner is: PLAYER {self.ganador}", True, COLOR_K
        )
        pos_marcador_x = ANCHO / 2 - txt.get_width() / 2
        pos_marcador_y = ALTO / 2 - txt.get_height() / 2
        pygame.Surface.blit(pantalla, txt, [pos_marcador_x, pos_marcador_y])

    def mostrar(self):
        print(f"El marcador ahora es: ({self.puntuacion[0]}, {self.puntuacion[1]})")

class Pong:
    def __init__(self):
        pygame.init()
        self.pantalla = pygame.display.set_mode(
            (ANCHO, ALTO)
        )  # Crear la Pantalla para el juego
        pygame.display.set_caption("SU Pong")

        self.fondo = pygame.image.load(
            "img/campo.png"
        ).convert_alpha()  # IMPORTAR IMAGEN DE FONDO

        self.reloj = (
            pygame.time.Clock()
        )  # Crea un nuevo objeto Reloj que es usado para rastrear una cantidad de tiempo

        pos_y = (ALTO - ALTO_PALETA) / 2
        pos_x_2 = ANCHO - MARGEN_LATERAL - ANCHO_PALETA
        self.jugador1 = Jugador(MARGEN_LATERAL, pos_y)
        self.jugador2 = Jugador(pos_x_2, pos_y)
        pelota_x = (ANCHO - TAM_PELOTA) / 2
        pelota_y = (ALTO - TAM_PELOTA) / 2

        self.pelota = Pelota(pelota_x, pelota_y)

        self.marcador = Marcador()

        pygame.font.init()

    def bucle_principal(
        self,
    ):  # bucle principal para que el juego permanezca abierto para ir actualizándose.
        salir = False
        empezar = False

        while not salir:
            # creamos un evento para salir del bucle cuando le demos a salir en el display
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    salir = True

                    # salir con la tecla escape
                if evento.type == pygame.KEYDOWN:  # pygame.key.get_pressed
                    if evento.key == pygame.K_ESCAPE:
                        salir = True

                    # empezar con la tecla espacio
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_SPACE:
                        empezar = True

            estado_teclas = pygame.key.get_pressed()

            # evento capturamos teclas de movimiento

            if estado_teclas[pygame.K_a]:
                self.jugador1.muevete(Jugador.ARRIBA)

            if estado_teclas[pygame.K_z]:
                self.jugador1.muevete(Jugador.ABAJO)

            if estado_teclas[pygame.K_UP]:
                self.jugador2.muevete(Jugador.ARRIBA)

            if estado_teclas[pygame.K_DOWN]:
                self.jugador2.muevete(Jugador.ABAJO)

            self.pantalla.blit(self.fondo, (0, 0))  # pintar el FONDO DEL CAMPO
            # self.pantalla.fill(COLOR_PANTALLA) -- PONER UN COLOR DE BACKGROUND

            ######### EMPEZAR TOCANDO LA TECLA ESPACIO ##########
            if not empezar:
                tipografia = pygame.font.Font("font/VT323-Regular.ttf", 40, bold=True)
                texto_intro = tipografia.render(
                    "Pulsa la tecla espacio para empezar", True, COLOR, COLOR_K
                )
                self.pantalla.blit(texto_intro, [120, 200])

            if empezar == True:
                self.pelota.mover()
            ######################################################

            ##### DIBUJO MARCADOR #####

            # self.txt = pygame.font.Font.render(self.tipo_letra, "hola", True, COLOR_K)
            # pos_marcador_x = ANCHO/2 - self.txt.get_width()/2
            # pos_marcador_y = ALTO/2 - self.txt.get_height()/2
            # self.pantalla.blit(self.txt, [pos_marcador_x, pos_marcador_y])

            self.pelota.colisionar(self.jugador1)
            self.pelota.colisionar(self.jugador2)

            self.reloj.tick(FPS)

            # pintar la red cada vez que se borre la pantalla
            # self.pinta_red()

            # dibujo un rectangulo (x, y, ancho, alto)
            self.jugador1.pintame(self.pantalla)
            self.jugador2.pintame(self.pantalla)

            self.pelota.pintame(self.pantalla)

            jugador_que_puntua = self.pelota.comprobar_punto()

            if jugador_que_puntua > 0:
                self.marcador.sumar_punto(jugador_que_puntua)

            if self.marcador.comprobar_ganador():
                self.marcador.pintar_ganador(self.pantalla)
                salir = True

            pygame.display.flip()  # borra la pantalla y el bucle la vuelve a pintar.

    def pinta_red(self):
        tramo_pintado = 15
        tramo_vacio = 5
        for i in range(MARGEN, ALTO - MARGEN, tramo_pintado + tramo_vacio):
            pygame.draw.line(
                self.pantalla,
                COLOR,
                (ANCHO / 2, i),
                (ANCHO / 2, i + tramo_pintado),
                TAM_LINEA,
            )


if __name__ == "__main__":
    juego = Pong()  # inicia el constructor
    juego.bucle_principal()  # llamada al bucle principal
