import pygame

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Step 4")

running = True

while running:
  for event in pygame.event.get(): 
    if event.type == pygame.QUIT:      
      running = False
    if event.type == pygame.KEYDOWN: #키보드 자판을 누르는 순간 발생
      print("KEYDOWN:", event.key)
    if event.type == pygame.KEYUP:    
      print("KEYUP:", event.key)
    if event.type == pygame.MOUSEBUTTONDOWN:  
      print("Mouse Click:", event.pos)

  screen.fill((200, 200, 200))
  pygame.display.flip()

pygame.quit()