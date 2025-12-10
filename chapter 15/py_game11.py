#11. 똥피하고 사과먹기 게임 완성
import pygame
import random             #추가: 사과 이동 방향 랜덤 재설정용

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("똥피하고 사과먹기")

clock = pygame.time.Clock() 

#추가: 사과 & 똥 이미지 로드
apple_img = pygame.image.load("apple.png")
apple_img = pygame.transform.scale(apple_img, (40, 40))

poop_img = pygame.image.load("poop.png")
poop_img = pygame.transform.scale(poop_img, (40, 40))


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


class Enemy(pygame.sprite.Sprite):
  def __init__(self, x, y):
    super().__init__()

    # (이전 코드) 단순 빨간 네모였음
    # self.image = pygame.Surface((40, 40))
    # self.image.fill((255, 80, 80))   #빨간 네모 (기존 아이템 느낌 살리기)

    self.image = poop_img             #변경: 똥 이미지로 교체
    self.rect = self.image.get_rect()
    self.rect.topleft = (x, y)

    self.speed_x = 3                  #추가: 좌우 이동 속도
    self.speed_y = 2                  #추가: 상하 이동 속도

  def update(self):
    # (이전 코드) 좌우로만 움직였음
    # self.rect.x += self.speed_x
    # if self.rect.left < 50 or self.rect.right > 200:
    #   self.speed_x *= -1

    self.rect.x += self.speed_x       #변경: 가로 + 세로 이동
    self.rect.y += self.speed_y

    #추가: 화면 가장자리에 닿으면 튕기기 (상하/좌우)
    if self.rect.left < 0 or self.rect.right > WIDTH:
      self.speed_x *= -1
    if self.rect.top < 0 or self.rect.bottom > HEIGHT:
      self.speed_y *= -1


all_sprites = pygame.sprite.Group()   
enemy_group = pygame.sprite.Group() 

player = Player()
all_sprites.add(player)

enemy = Enemy(50, 260)                #초기 위치
all_sprites.add(enemy)
enemy_group.add(enemy)

#(이전 코드) 코인(초록 원)용 Rect
coin_rect = pygame.Rect(430, 130, 40, 40)  # (450,150) 근처, 원을 감싸는 사각형

#추가: 사과 이동 속도 (가로 + 세로)
coin_speed_x = 2
coin_speed_y = 2

score = 0
running = True
game_over = False        #원래 코드에도 있었던 플래그

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

    #추가: 게임오버 상태에서 엔터(RETURN)를 누르면 게임 재시작
    if event.type == pygame.KEYDOWN:
      if game_over and event.key == pygame.K_RETURN:
        game_over = False         #추가: 다시 플레이 가능
        score = 0                 #추가: 점수 초기화

        #추가: 플레이어 위치 초기화
        player.rect.center = (WIDTH // 2, HEIGHT // 2)

        #추가: 적(똥) 초기화
        enemy.rect.topleft = (50, 260)
        enemy.speed_x = 3
        enemy.speed_y = 2

        #추가: 사과 초기화
        coin_rect.x = 430
        coin_rect.y = 130
        coin_speed_x = 2
        coin_speed_y = 2

  #변경: 게임 오버가 아닐 때만 전체 업데이트/충돌 처리 (원래도 이 구조는 유지)
  if not game_over:
    all_sprites.update()  # Player, Enemy 전부 update()

    # (이전 코드) 코인은 멈춰있었음
    # if player.rect.colliderect(coin_rect):
    #   score += 1
    #   coin_rect.x = 430 if score % 2 == 0 else 350

    #추가: 사과(코인)도 가로 + 세로 이동
    coin_rect.x += coin_speed_x
    coin_rect.y += coin_speed_y

    #추가: 벽에 닿으면 튕김
    if coin_rect.left < 0 or coin_rect.right > WIDTH:
      coin_speed_x *= -1
    if coin_rect.top < 0 or coin_rect.bottom > HEIGHT:
      coin_speed_y *= -1

    #변경: 사과 충돌 처리 (먹으면 위치 & 방향 랜덤 변경)
    if player.rect.colliderect(coin_rect):
      score += 1
      print("사과 먹음!")

      #추가: 사과를 화면 내 랜덤 위치로 순간 이동
      coin_rect.x = random.randint(0, WIDTH - coin_rect.width)
      coin_rect.y = random.randint(0, HEIGHT - coin_rect.height)

      #추가: 이동 방향도 랜덤하게 반전
      coin_speed_x *= random.choice([-1, 1])
      coin_speed_y *= random.choice([-1, 1])

    # 똥 충돌 (원래 코드와 같은 역할)
    hits = pygame.sprite.spritecollide(player, enemy_group, False)
    if hits:
      print("똥에 닿음! 게임 오버")
      game_over = True

  # ------------------ 그리기 ------------------
  screen.fill((170, 200, 255))  
  pygame.draw.rect(screen, (80, 170, 80), (0, HEIGHT - 60, WIDTH, 60))  # 땅

  # (이전 코드) 초록 원으로 코인 그리기
  # pygame.draw.circle(
  #   screen, (0, 255, 0),
  #   (coin_rect.x + coin_rect.width // 2, coin_rect.y + coin_rect.height // 2),
  #   20,
  # )

  #변경: 초록 원 대신 사과 이미지 사용
  screen.blit(apple_img, coin_rect)
  all_sprites.draw(screen)  # (Player + Enemy)

  # 점수 텍스트 (원래 코드와 거의 동일)
  font = pygame.font.SysFont(None, 24)
  text = font.render(f"Score: {score}", True, (0, 0, 0))
  screen.blit(text, (10, 10))

  if game_over:
    over_text = font.render("GAME OVER (Press Enter)", True, (255, 0, 0))
    over_x = (WIDTH - over_text.get_width()) // 2  # 글씨 정중앙에 배치
    over_y = (HEIGHT - over_text.get_height()) // 2 
    screen.blit(over_text, (over_x, over_y))

  pygame.display.flip()
  clock.tick(60)

pygame.quit()