import pygame

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Step 2")

screen.fill((255, 255, 255)) #화면색을 흰색으로 채움
pygame.display.flip() #Pygame에서 화면을 그린 후에는 flip()으로 실제 창에 반영해야 함.

pygame.time.delay(2000) #게임 화면을 2초 동안 그대로 유지

pygame.quit()