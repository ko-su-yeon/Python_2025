#플레이어가 공격(총알) 가능

import pygame
import random

pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Step 8 - Shooting Player")

clock = pygame.time.Clock()

# 이미지/사운드
player_img = pygame.image.load("dukbird.png").convert_alpha()
apple_img = pygame.image.load("apple.png").convert_alpha()
poop_img = pygame.image.load("poop.png").convert_alpha()
shoot_sound = pygame.mixer.Sound("shoot.wav")
eat_sound = pygame.mixer.Sound("eat.wav")
hit_sound = pygame.mixer.Sound("hit.wav")

# ----------------------------
# 플레이어
# ----------------------------
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(player_img,(50,50))
        self.rect = self.image.get_rect(center=(WIDTH//2, HEIGHT//2))
        self.speed=3

    def update(self):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: self.rect.x-=self.speed
        if keys[pygame.K_RIGHT]: self.rect.x+=self.speed
        if keys[pygame.K_UP]: self.rect.y-=self.speed
        if keys[pygame.K_DOWN]: self.rect.y+=self.speed
        self.rect.clamp_ip(screen.get_rect())

# ----------------------------
# 총알
# ----------------------------
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((5,15))
        self.image.fill((255,255,0))
        self.rect = self.image.get_rect(center=(x,y))
        self.speed_y = -7

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.bottom < 0:
            self.kill()

# ----------------------------
# 적
# ----------------------------
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(poop_img,(40,40))
        self.rect = self.image.get_rect(topleft=(random.randint(0,WIDTH-40), random.randint(0,HEIGHT-40)))
        self.speed_x = random.choice([-3,3])
        self.speed_y = random.choice([-2,2])
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.left<=0 or self.rect.right>=WIDTH: self.speed_x*=-1
        if self.rect.top<=0 or self.rect.bottom>=HEIGHT: self.speed_y*=-1

# ----------------------------
# 사과
# ----------------------------
class Apple(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(apple_img,(40,40))
        self.rect = self.image.get_rect(topleft=(random.randint(0,WIDTH-40), random.randint(0,HEIGHT-40)))
        self.speed_x = random.choice([-2,2])
        self.speed_y = random.choice([-2,2])
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.left<=0 or self.rect.right>=WIDTH: self.speed_x*=-1
        if self.rect.top<=0 or self.rect.bottom>=HEIGHT: self.speed_y*=-1

# ----------------------------
# 그룹
# ----------------------------
all_sprites = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
apple_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

for _ in range(5):
    e = Enemy()
    all_sprites.add(e)
    enemy_group.add(e)

for _ in range(5):
    a = Apple()
    all_sprites.add(a)
    apple_group.add(a)

score = 0
game_over=False
running=True

# ----------------------------
# 메인 루프
# ----------------------------
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running=False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not game_over:
                bullet = Bullet(player.rect.centerx, player.rect.top)
                all_sprites.add(bullet)
                bullet_group.add(bullet)
                shoot_sound.play()

    if not game_over:
        all_sprites.update()

        # 사과 충돌
        hits = pygame.sprite.spritecollide(player, apple_group, False)
        for h in hits:
            eat_sound.play()
            score += 1
            h.rect.topleft = (random.randint(0,WIDTH-40), random.randint(0,HEIGHT-40))
            h.speed_x=random.choice([-2,2])
            h.speed_y=random.choice([-2,2])

        # 똥 충돌
        if pygame.sprite.spritecollide(player, enemy_group, False):
            game_over=True

        # 총알과 적 충돌
        bullet_hits = pygame.sprite.groupcollide(bullet_group, enemy_group, True, True)
        for h in bullet_hits:
            hit_sound.play()
            # 새 적 추가
            e = Enemy()
            all_sprites.add(e)
            enemy_group.add(e)

    # ------------------ 그림 그리기 ------------------
    screen.fill((170,200,255))
    pygame.draw.rect(screen,(80,170,80),(0,HEIGHT-60,WIDTH,60))
    all_sprites.draw(screen)

    font = pygame.font.SysFont(None,24)
    text = font.render(f"Score: {score}" if not game_over else "GAME OVER",True,(0,0,0))
    screen.blit(text,(10,10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
