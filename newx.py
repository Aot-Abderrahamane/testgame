import pygame, time

pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))
myfont= pygame.font.SysFont("Arial",60)
label= myfont.render("Hello Pygame!",1,(255,255,0))
self.screen_rect = screen.get_rect()
pygame.display.update()
time.sleep(5)
pygame.quit()