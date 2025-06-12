import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Game")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
FONT = pygame.font.SysFont(None, 48)

player_pos = [WIDTH // 2, HEIGHT // 2]
speed = 5

def draw_menu():
    screen.fill(WHITE)
    title = FONT.render("START GAME", True, BLUE)
    screen.blit(title, (50, HEIGHT // 2 - 24))
    pygame.display.flip()

def game_loop():
    while True:
        screen.fill(WHITE)
        pygame.draw.circle(screen, BLUE, player_pos, 20)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]: player_pos[1] -= speed
        if keys[pygame.K_s]: player_pos[1] += speed
        if keys[pygame.K_a]: player_pos[0] -= speed
        if keys[pygame.K_d]: player_pos[0] += speed
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()

        pygame.time.Clock().tick(60)

# 시작 화면
draw_menu()
waiting = True
while waiting:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
        elif event.type == pygame.KEYDOWN:
            waiting = False

game_loop()
