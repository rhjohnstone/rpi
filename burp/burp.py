from gpiozero import Button
from pygame import mixer
from time import sleep

# tell RPi which GPIO pin to use
jelly_baby = Button(3)

# initialize audio
mixer.init()
burp = mixer.Sound("burp.wav")
sleep(2)  # needed or it (sometimes) misses the first play
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
