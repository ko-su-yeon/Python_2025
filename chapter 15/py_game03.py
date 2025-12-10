import pygame

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Step 3")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #사용자가 창의 X 버튼을 누르면 발생.
            running = False

    screen.fill((200, 200, 200)) #밝은 회색
    pygame.display.flip()

pygame.quit()