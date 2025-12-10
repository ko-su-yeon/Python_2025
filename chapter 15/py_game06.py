import pygame

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Step 6")

img = pygame.Surface((40, 40)) #가로 40, 세로 40인 빈 이미지 공간 생성   
img.fill((0, 0, 255))    # surface공간을 파란색으로 채움          

rect = img.get_rect()              
rect.center = (WIDTH // 2, HEIGHT // 2)

speed = 1
running = True

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if event.type == pygame.KEYDOWN:
      print("KEYDOWN:", event.key)
    if event.type == pygame.KEYUP:
      print("KEYUP:", event.key)
    if event.type == pygame.MOUSEBUTTONDOWN:
      print("Mouse Click:", event.pos)

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
  screen.blit(img, rect)   #bilt = 이미지 붙여넣기

  pygame.display.flip() #화면 업데이트

pygame.quit()