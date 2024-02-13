import _thread
from PiicoDev_SSD1306 import create_PiicoDev_SSD1306
import machine
import utime
import math

temp_data = 0.0

sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / 65535
display = create_PiicoDev_SSD1306()

def display_data(temperature):
    display.text("The current Temperature is", 0, 0, 1)
    display.text(str(temperature), 0, 15, 1)
    display.show()


def get_temp_data():
    reading = sensor_temp.read_u16() * conversion_factor
    ug_temp = 27 - (reading - 0.706) / 0.001721
    temperature = math.trunc(ug_temp)
    return temperature

_thread.start_new_thread(display_data, (temp_data,))

while True:
    temp_data = get_temp_data()
    display_data(temp_data)
    utime.sleep(2)
    display.fill(0)
    display.show()
