import pygame
import sys

# 1. Inicialización
# 1.1. Tamaño de pantalla
tamano = 800, 600
pantalla = pygame.display.set_mode(tamano)
# 1.2. Título de la ventana
pygame.display.set_caption("Mi juego")
# 1.3. Variables de control
jugar = True

# 2. Bucle del juego
while jugar:
    # 2.1. Gestión de eventos (salir, en este caso)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugar = False

    # 2.2. Actualizar la pantalla
    pygame.display.flip()

    # 2.3. Agregar un pequeño retraso para evitar un bucle demasiado rápido
    pygame.time.delay(10)

# 3. Finalizar
pygame.quit()
sys.exit()
