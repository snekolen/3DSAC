import pygame
import time
import sys

#Code below works:
def play(vol1, vol2):
    #pygame.init()
    #pygame.mixer.init()


    channel = pygame.mixer.find_channel()#Getting a Free Channel
    channel.set_volume(vol1, vol2)#1.0 volume for left and 0.0 for right

    channel.play(pygame.mixer.Sound('sample-3s.wav'))

    time.sleep (4)

#Code below works:

'''
pygame.init()
pygame.mixer.init()
sounda= pygame.mixer.Sound("sample-3s.wav")

sounda.play()
time.sleep (20)

'''