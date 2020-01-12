from pygame import mixer
from time import sleep

mixer.init()
c = mixer.Sound("c.wav")
d = mixer.Sound("d.wav")
e = mixer.Sound("e.wav")
f = mixer.Sound("f.wav")
g = mixer.Sound("g.wav")

first_bit = [e, e, f, g, g, f, e, d, c, c, d, e]

line1 = first_bit + [e, d, d]
line2 = first_bit + [d, c, c]
line3 = [d, d, e, c, d, e, f, e, c, d, e, f, e, d, c, d, g]
line4 = line2

sleep(2)  # I assume the mixer takes some time to load the sound files.
          # Whenever I don't include a long enough sleep, the first note gets skipped.
for note in line1+line2+line3+line4:
    note.play()
    sleep(0.4)
    note.stop()
