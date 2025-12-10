import pygame

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Step 8")

clock = pygame.time.Clock() #게임의 프레임 속도 조절하는 도구

img = pygame.image.load("dukbird.png")             
img = pygame.transform.scale(img, (50, 50))      
rect = img.get_rect()
rect.center = (WIDTH // 2, HEIGHT // 2)

speed = 3
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

  rect.clamp_ip(screen.get_rect()) #화면 밖으로 나가지 못하게 막아줌 

 
  screen.fill((170, 200, 255))   #하늘색으로 칠함(화면 전체)
  
  pygame.draw.rect(screen, (80, 170, 80), (0, HEIGHT - 60, WIDTH, 60))
  pygame.draw.rect(screen, (255, 80, 80), (50, 280, 40, 40))
  pygame.draw.circle(screen, (0, 255, 0), (450, 150), 20) 
  pygame.draw.line(screen, (0, 0, 0), (300, 300), (500, 300), 5)
  
  screen.blit(img, rect) 

  pygame.display.flip()

  clock.tick(60)  #이 코드가 실행될 때마다 최대 1초에 60번만 루프를 돌도록 제한하는 것 (속도가 너무 빨라지는거 방지)