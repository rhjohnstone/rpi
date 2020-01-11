import pygame

pygame.init()
pygame.mixer.init()
e = pygame.mixer.Sound("e.wav")
f = pygame.mixer.Sound("f.wav")
g = pygame.mixer.Sound("g.wav")
d = pygame.mixer.Sound("d.wav")

for note in [e, e, f, g, g, f, e, d]:
    note.play()
