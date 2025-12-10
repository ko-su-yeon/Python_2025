import pygame

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Step 6 - 이미지로 변경")

img = pygame.image.load("dukbird.png")
img = pygame.transform.scale(img, (50, 50)) #이미지를 가로 50, 세로 50 크기로 변환
rect = img.get_rect() #이미지를 보이지 않는 사각형(rect객체)만듦
rect.center = (WIDTH // 2, HEIGHT // 2) #이미지 중앙으로

speed = 1
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        rect.x -= speed
    if keys[pygame.K_RIGHT]:
        rect.x += speed
    if keys[pygame.K_UP]:
        rect.y -= speed
    if keys[pygame.K_DOWN]:
        rect.y += speed

    if rect.left < 0:
        rect.left = 0
    if rect.right > WIDTH:
        rect.right = WIDTH
    if rect.top < 0:
        rect.top = 0
    if rect.bottom > HEIGHT:
        rect.bottom = HEIGHT

    screen.fill((200, 200, 200))
    screen.blit(img, rect)  
    pygame.display.flip()

pygame.quit()