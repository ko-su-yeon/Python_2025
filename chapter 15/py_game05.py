import pygame

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Step 5")

x, y = WIDTH // 2, HEIGHT // 2 #x,y는 사각형의 현재 위치(화면 중앙에서 시작)
speed = 1
size = 40  

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

#방향키를 누르고 있는 동안 계속 움직임
  if keys[pygame.K_LEFT]:
    x -= speed
  if keys[pygame.K_RIGHT]:
    x += speed
  if keys[pygame.K_UP]:
    y -= speed
  if keys[pygame.K_DOWN]:
    y += speed


#사각형이 왼쪽 화면 밖으로 나가면 x=0으로 고정
#오른쪽 화면 밖으로 나가면 x = WIDTH - size(사각형 크기만큼 빼줘야 화면 끝에 딱 맞음)
#위/아래도 똑같은 원리
#즉, 사각형이 화면 밖으로 못 나가도록 제한하는 코드
  if x < 0:
    x = 0
  if x > WIDTH - size:
    x = WIDTH - size
  if y < 0:
    y = 0
  if y > HEIGHT - size:
    y = HEIGHT - size

  screen.fill((200, 200, 200))
  pygame.draw.rect(screen, (0, 0, 255), (x, y, size, size))

  pygame.display.flip()

pygame.quit()