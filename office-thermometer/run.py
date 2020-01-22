from gpiozero import PWMLED
from w1thermsensor import W1ThermSensor
import time


def intround(x):
    return int(round(x))


red = PWMLED(18)
blue = PWMLED(24)
thermometer = W1ThermSensor()

lowest = 24
low = 25.5
high = 26.5
highest = 28

cold = lambda temp: 1 - (temp - lowest) / (low - lowest)
hot = lambda temp: (temp - high) / (highest - high)

wait = 10

output_file = "output.txt"

latest = time.time()
try:
    with open(output_file, "w") as outf:
        while True:
            current_time = time.time()
            temp = thermometer.get_temperature(W1ThermSensor.DEGREES_C)
            '''print(temp)'''
            if temp <= lowest:
                red.value = 0
                blue.value = 1
            elif lowest < temp <= low:
                red.value = 0
                blue.value = cold(temp)
            elif low < temp < high:
                red.value = 0
                blue.value = 0
            elif high <= temp < highest:
                blue.value = 0
                red.value = hot(temp)
            elif highest <= temp:
                blue.value = 0
                red.value = 1
            if current_time - latest >= 60:
                outf.write(f"{intround(current_time)} {intround(10*temp)}\n")
                latest = current_time
            time.sleep(1)
except KeyboardInterrupt:
    pass
