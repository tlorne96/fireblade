# Project Solus

A reimagining of the HiJo Project from 2018, brought over to micropython for a low cost and low overhead product, using micropython and opensource hardware and pre-developed libraries for micropython reduce the dependancies of the overall project.

The initial pilot will be run offline to save development time and overhead, a re-write may be needed to move it to online.

As we add modules we may need to add new python libraries, these will need to be put in the libs folder and copied to the PICO with Thonny when testing.


## Current Sensor Suite
- SSD1306 O-led display (data out)
- VL53L1X laser distance sensor (for height)
- On board temperature sensor (this may be swapped out)
- LIS3DH 3 axis accelerometer
- Rotary encoder with button for user input
- Adafruit ADA254 MicroSD (storing data for review)

## Setting Up Dev Environment
Systems with the items installed/extensions in dot points below.

### Using Ubuntu 22.04 or Windows 10
 - Visual Studio Code
 - Python 3.10.12
 - Git
 - Thonny Python IDE (for copying and saving files to the Pico)

### Visual Studio Code:
- [MicroPico Run the fix Permissions Script](https://github.com/paulober/MicroPico/wiki/Linux) (Ubuntu only)
- Git Lense (quality of life)
- IntelliCode
- Pylance
- Python
- Python Debugger

### Setting up the PICO and PICO W
#### Setup firmware
- Download one of the two files below depending on which Pico you are using:
    - [Pico W](https://micropython.org/download/rp2-pico-w/rp2-pico-w-latest.uf2)
    - [Pico](https://micropython.org/download/rp2-pico/rp2-pico-latest.uf2)
- Hold the button down on the Pico whilst plugging it in 
- A removable device will appear in your system, drag the file you downloaded to the removable device.
- Once copied it will install Micropython on itself and reboot and vanish
- The Pico is now set up

#### Add lib files
- Close Visual Studio
- Open Thonny
- Go Run -> Configure Interpreter
- Change the interpreter to 'MicroPython (Raspberry Pi Pico)'
- Change the port eg 'Board CDC @ COM3'. If one option doesn't work try another
- Click ok
- The interpreter should start
- Go to File -> Open File
- Choose 'This computer'
- Select the first file from the libs folder in the repo
- Go to File -> Save As
- Select 'Raspberry Pi Pico'
- Type or copy in the name of file including the extension
- Repeat for the other lib files

### Run the code
- Open Visual Studio Code
- Open main.py
- Click Run from the bottom of the window

### Branching and keeping main safe
When writing code or working on a feature please ensure you checkout a new branch or switch to a branch thats being worked on if you are helping with that feature or something related to it for example

``` git checkout -b "Testing_New_Sensor" ```

This will help us keep the main working branch safe from unintended commits, and be sure to use naming that makes sense to other users.

If during this process you are adding new files you need to add them with ```git add filenamehere``` and if the file is in a subfolder ```git add foldername/filename```.
You can add all files with ```git add .```

Writing a commit message when getting ready to push changes is also a good idea you can do that with ```git commit -a -m "Added new files and fixed an issue" ```
