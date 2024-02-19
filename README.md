
# Project Solus

A reimagining of the HiJo Project from 2018, brought over to micropython for a low cost and low overhead product, using micropython and opensource hardware and pre-developed libraries for micropython reduce the dependancies of the overall project.

The Initial Pilot will be run offline to save development time and overhead, A re-write may be needed to move it to online.

As we add modules we may need to add new python libraries, these will need to be put in the libs folder and copied to the PICO with Thonny when testing



## Sensor Suite Currently

- SSD1306 O-led Display (Data Out)
- VL53L1X Laser Distance Sensor (For Height)
- On board Temperature sensor (This may be swapped out)
- LIS3DH 3 axis Accelerometer
- Rotary encoder with Button for user input
- Adafruit ADA254 MicroSD (Storing Data for review)

## Setting Up Dev Environment
Systems with the items installed/extensions in dot points below.

### Using Ubuntu 22.04
 - Visual Studio Code
 - Python 3.10.12
 - Git
 - Thonny Python IDE (for copying and saving files to the Pico)

### Visual Studio Code:
- [MicroPico Run the fix Permissions Script](https://github.com/paulober/MicroPico/wiki/Linux)
- Git Lense (Quality of Life)
- IntelliCode
- Pylance
- Python
- Python Debugger

### Setting up the PICO and PICO W 
- download one of the two files below
    - [Pico W](https://micropython.org/download/rp2-pico-w/rp2-pico-w-latest.uf2)
    - [Pico](https://micropython.org/download/rp2-pico/rp2-pico-latest.uf2)
- Hold the Button down on the Pico whilst plugging it in 
- A removable Device will appear in your system, drag the file you downloaded to the removable device.
- Once copied it will install Micropython on itself and reboot and vanish
- The Pico is now set up

### Brancing and keeping main safe
When writing code or working on a feature please ensure you checkout a new branch or switch to a branch thats being worked on if you are helping with that feature or something related to it for example

``` git checkout -b "Testing_New_Sensor" ```

This will help us keep the main working branch safe from un intended commits, and be sure to use naming that makes sense to other users.

If during this process you are adding new files you need to add them with ```git add filenamehere``` and if the file is in a subfolder ```git add foldername/filename```

Writing a commit message when getting ready to push changes is also a good idea you can do that with ```git commit -a -m "Added new files and fixed an issue" ```
