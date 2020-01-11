from gpiozero import Button
import pygame
from time import sleep

# tell RPi which GPIO pin to use
jelly_baby = Button(3)

# initialize audio
pygame.init()
pygame.mixer.init()
burp = pygame.mixer.Sound("burp.wav")

try:
    while True:
        jelly_baby.wait_for_press()
        burp.play()
        sleep(2)
        burp.stop()
except KeyboardInterrupt:
    # for clean escape from infinite loop
    burp.stop()
    jelly_baby.close()
