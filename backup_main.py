import network
import socket
from time import sleep
from picozero import pico_temp_sensor, pico_led
import machine
ssid = 'Solus1'
password = 'thinkb81'

def connect():
    #Connecting to network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected()== False:
        print('waiting for connection...')
        sleep(1)
    ip = wlan.ifconfig()[0]
    print(f'connected on {ip}')
    return ip #returning IP address as a variable

#creating a function to open a socket
def open_socket(ip):
    adress = (ip, 80)
    connection = socket.socket()
    connection.bind(adress)
    connection.listen(1)
    return(connection)

def webpage(temperature, state):
    #template html
    html = f"""
            <!DOCTYPE html>
            <html>
            <body>
            <form action="./lighton">
            <input type="submit" value="Light on">
            </form>
            <form action="./lightoff">
            <input type="submit" value="Light off">
            </form>
            <p>LED is {state}</p>
            <p>Temp is {temperature}</p>
            </body>
            </html>
            """
    return str(html)
def serve(connection):
    state = 'OFF'
    pico_led.off()
    temperature = 0
    while True:
        client = connection.accept()[0]
        request = client.recv(1024)
        request = str(request)
        print(request)
        try:
            request = request.split()[1]
        except IndexError:
            pass
        if request == '/lighton?':
            pico_led.on()
        elif request =='/lightoff?':
            pico_led.off()
        html = webpage(temperature, state)
        client.send(html)
        client.close()

try:
    ip = connect()
    connection = open_socket(ip)
    serve(connection)
except KeyboardInterrupt:
    machine.reset()