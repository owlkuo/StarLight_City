# +=========================+ #
# | { StarLight City Game } | #
# | { By Isaac And Topper } | #
# | {+-------------------+} | #
# | { Do Not Go Read More } | #
# | { Hey Did You Hear Me } | #
# | { But I Don't want to } | #
# | { Get In Trouble!!!!! } | #
# | { Ok Fine!!!!!! ): ): } | #
# +=========================+ #
import time
import pygame
from pygame import mixer
import sys
(num_pass, num_fail) = pygame.init()
mixer.init()
if not pygame.get_init():
    print("Pygame init failed")
    time.sleep(5)
    sys.exit()
print("Pygame init succeeded")
print('Number of modules init successfully:', num_pass)
print('Number of modules fail successfully:', num_fail)
pygame.display.set_caption('StarLight City')
icon = pygame.image.load('Icon.ico')
screen = pygame.display.set_mode((800, 600))
window = pygame.display.set_mode((600, 500), pygame.RESIZABLE)
pygame.display.set_icon(icon)
time.sleep(0.01)
mixer.music.load("StarLight.ogg")
mixer.music.set_volume(1)
mixer.music.play(1000000000, 0, 10)
running = True
StartMenu = True
Screen_Setting = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if StartMenu:
        X_screen, Y_screen = screen.get_size()
        if X_screen > Y_screen:
            Screen_Setting = Y_screen
        elif X_screen < Y_screen:
            Screen_Setting = X_screen
        else:
            Screen_Setting = X_screen * Y_screen
        clock = pygame.time.Clock()
        image = pygame.image.load('Menu.jpg')
        DEFAULT_IMAGE_SIZE = (Screen_Setting, Screen_Setting)
        image = pygame.transform.scale(image, DEFAULT_IMAGE_SIZE)
        image = pygame.transform.rotate(image, 0)
        screen.blit(image, image.get_rect(center=screen.get_rect().center))
        pygame.display.flip()
        clock.tick(30)
        mouse = pygame.mouse.get_pos()

