import pygame
from random import randrange

def func():
    RES = 600
    SIZE = 10

    x, y = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
    apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
    length = 1
    snake = [(x, y)]
    dx, dy = 0, 0
    fps = 20

    pygame.init()
    screen = pygame.display.set_mode([RES, RES])
    clock = pygame.time.Clock()

    while True:

        screen.fill((0, 10, 50))

        [(pygame.draw.rect(screen, (0, 255, 0), (i, j, SIZE - 1, SIZE - 1))) for i, j in snake]
        pygame.draw.rect(screen, (255, 0, 0), (*apple, SIZE, SIZE))
        x += dx * SIZE
        y += dy * SIZE
        snake.append((x, y))
        snake = snake[-length:]

        if snake[-1] == apple:
            apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
            length += 1
            if fps < 20:
                fps += 1
        if x < 0 or x > RES - SIZE or y > RES - SIZE or y < 0:
            break
        if len(snake) != len(set(snake)):
            break

        pygame.display.flip()
        clock.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        key = pygame.key.get_pressed()
        if key[pygame.K_w] and dy != 1:
            dx, dy = 0, -1
        elif key[pygame.K_s] and dy != -1:
            dx, dy = 0, 1
        elif key[pygame.K_a] and dx != 1:
            dx, dy = -1, 0
        elif key[pygame.K_d] and dx != -1:
            dx, dy = 1, 0
    func()


func()