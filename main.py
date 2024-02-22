import _thread
from PiicoDev_SSD1306 import create_PiicoDev_SSD1306
import machine
import utime
import PiicoDev_VL53L1X as dista
import PiicoDev_LIS3DH as accel
import math
from PiicoDev_TMP117 import PiicoDev_TMP117, sleep_ms
from rotary_irq_rp2 import RotaryIRQ

# Initialize variables
temp_data = 0.0
distsensor = dista.PiicoDev_VL53L1X()  # Create an instance of the VL53L1X distance sensor
motion = accel.PiicoDev_LIS3DH()  # Create an instance of the LIS3DH accelerometer
sensor_temp = PiicoDev_TMP117()
display = create_PiicoDev_SSD1306()  # Create an instance of the SSD1306 display
motion.range = 2  # Set the range of the accelerometer

# Function to get accelerometer data
def get_movements():
    x, y, z = motion.acceleration  # Read accelerometer data
    x = round(x, 2)  # Round x-axis acceleration to 2 decimal places
    y = round(y, 2)  # Round y-axis acceleration to 2 decimal places
    z = round(z, 2)  # Round z-axis acceleration to 2 decimal places
    myString = "X: " + str(x) + ", Y: " + str(y) + ", Z: " + str(z)  # Build string with accelerometer data
    return myString, x, y, z  # Return accelerometer data

# Function to display data on SSD1306 display
def display_data(temperature, dist):
    myString, x, y, z = get_movements()  # Get accelerometer data
    display.fill(0)  # Clear display buffer
    display.text("Temp: ", 0, 0, 1)
    display.text(str(temperature),44,0,1)
    display.text("Dist: ",0,15,1)
    display.text(str(dist),44,15,1)
    display.text(myString, 0, 45, 1)  # Display accelerometer data
    display.show()  # Update display

# Function to read temperature and distance
def get_temp_data():
    temperature = math.trunc(sensor_temp.readTempC())
    dist = distsensor.read() / 10  # Read distance from VL53L1X sensor and convert to centimeters
    return temperature, dist  # Return temperature and distance

# Start a new thread to display initial data on SSD1306 display
_thread.start_new_thread(display_data, (temp_data,))

# Main loop
while True:
    temp_data, dist = get_temp_data()  # Get temperature and distance data
    display_data(temp_data, dist)  # Display temperature and distance data
    utime.sleep(0.2)  # Wait for 2 seconds before next reading
    print(dist)
