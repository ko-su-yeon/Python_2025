import pygame

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Step 8")

clock = pygame.time.Clock() 

class Player(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.image = pygame.image.load("dukbird.png")         
    self.image = pygame.transform.scale(self.image, (50, 50))
    self.rect = self.image.get_rect()
    self.rect.center = (WIDTH // 2, HEIGHT // 2)
    self.speed = 3

def update(self): 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
      self.rect.x -= self.speed
    if keys[pygame.K_RIGHT]:
      self.rect.x += self.speed
    if keys[pygame.K_UP]:
      self.rect.y -= self.speed
    if keys[pygame.K_DOWN]:
      self.rect.y += self.speed

    self.rect.clamp_ip(screen.get_rect())

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

running = True

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  all_sprites.update() 

  screen.fill((170, 200, 255))  
  pygame.draw.rect(screen, (80, 170, 80), (0, HEIGHT - 60, WIDTH, 60))
  pygame.draw.rect(screen, (255, 80, 80), (50, 280, 40, 40))
  pygame.draw.circle(screen, (0, 255, 0), (450, 150), 20)
  pygame.draw.line(screen, (0, 0, 0), (300, 300), (500, 300), 5)

  all_sprites.draw(screen) #플레이어 이미지 화면에 표시

  pygame.display.flip()
  clock.tick(60)
pygame.quit()