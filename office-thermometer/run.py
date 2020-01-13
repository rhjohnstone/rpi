from gpiozero import LED
from w1thermsensor import W1ThermSensor
import time


def update(final=False):
    global data
    with open(output_file, "a") as outf:
        np.savetxt(outf, data)
    if not final:
        data = np.zeros((buffer, 2), dtype=int)


def intround(x):
    return int(round(x))


red = LED(18)
blue = LED(24)
thermometer = W1ThermSensor()

output_file = "output.txt"
with open(output_file, "w") as outf:
    pass

upper = 27
lower = 25.5
buffer = 10

data = np.zeros((buffer, 2), dtype=int)
row = 0
try:
    while True:
        current_time = time.time()
        temp = thermometer.get_temperature(W1ThermSensor.DEGREES_C)
        if temp > upper:
            red.on()
            blue.off()
        elif temp < lower:
            blue.on()
            red.off()
        else:
            red.off()
            blue.off()
        data[row] = [intround(current_time), intround(10*temp)]
        row = (row + 1) % buffer
        if row == 0:
            update()
        time.sleep(1)
except KeyboardInterrupt:
    if row > 0:
        update(True)

