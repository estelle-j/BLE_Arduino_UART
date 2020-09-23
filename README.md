# Bluetooth Communication with Arduino board using a Bluefruit LE UART Friend

This repository shows how to use the Bluefruit LE UART Friend to communicate with an Arduino board using Bluetooth.

![uart_image](images/uart.png)

Using this repository, you'll be able to communicate with the Arduino board and make it execute command (switch on/off a LED, blink Arduino internal LED, get temperature...) using two methods:

- the [Bluefruit LE Conect](https://learn.adafruit.com/bluefruit-le-connect) app to control the Arduino from your iOS/Android phone
- a Python script to control the Arduino from your computer

---

## Setup the Arduino board

To use all of the commands executable by the program, you'll need:

- an Arduino Uno board
- a [Bluefruit LE UART Friend](https://learn.adafruit.com/introducing-the-adafruit-bluefruit-le-uart-friend)
- a breadboard and several M-to-M wires
- a LED, a RGB LED and 4 resistors (220 ohms)
- a DHT11 Temperature and Humidity sensor


### Possible commands

With this program, you'll be able to execute several commands:
- Switch on and switch off a LED
- Blink the internal LED of the Arduino
- Switch on/off a RGB LED and specify the colors
- Get the temperature and the humidity from the DHT11 sensor

### Wiring the Arduino board

#### Bluefruit LE UART Friend

To use the [Bluefruit LE UART Friend](https://learn.adafruit.com/introducing-the-adafruit-bluefruit-le-uart-friend/wiring), connect the pins up as follows:

- **MOD** to **Pin 12**
- **CTS** to **Pin 11**
- **TXO** to **Pin 10**
- **RXI** to **Pin 9**
- **VIN** to **5V**
- **RTS** to **Pin 8**
- **GND** to **GND**

#### LED

To use a LED (switch on/off), connect the LED to the ground and to digital **pin 3**. Do not forget the resistor.

#### RGB LED

To use the RGB LED, connect the **blue** lead to digital **pin 4**, the **green** lead to digital **pin 5** and the **red** lead to digital **pin 6**. Do not forget the resistors. Connect the LED to the ground.

#### DHT11 Temperature and Humidity sensor

To use the DHT11 sensor, connect the sensor pin to digital **pin 2** and to the ground and to 5V power.

To use this sensor, you also need to import the DHT library.

---

## Using Python program

The Python program uses the [Adafruit Python BluefruitLE](https://github.com/adafruit/Adafruit_Python_BluefruitLE) library. Make sure it's installed before using the program. The library only supports Linux (with Bluez) and Mac OSX (with Apple's CoreBluetooth library).

To run the program, just enter the following command-line in a terminal

```bash
python command_uart.py
```

The program will connect to the UART and you'll be able to choose what you want to do.

--- 
## Using Bluefruit LE Connect

To control your Arduino board, you can also use the Bluefruit LE Connect app.

Launch the app and connect your phone to the UART.

Once you are connected, select the UART mode. You'll be able to send messages to the UART.

The Python program handles the creation of the command to send to the UART.
But with the app, you'll have to enter the command yourself.

<br />

To switch on the led, type and send:
```bash
on
```
<br />

To switch off the led, type and send:
```bash
off
```
<br />

To get the temperature, type and send:
```bash
temperature
```
<br />

To get the humidity, type and send:
```bash
humidity
```
<br />

To blink the internal LED, choose a number of times, *repetition*, you want to blink the LED, the duration (in milliseconds), *duration_on*, you want the LED to be switched on and the duration (in milliseconds), *duration_off*, you want the LED to be switched off. Then type and send
```bash
blink repetition duration_on duration_off
```
<br />

To switch on the RGB LED, choose values *red*, *green* and *blue* for the red, green and blue colors. These values should be between 0 and 255 Then type and send:
```bash
rgb red green blue
```

If you want to switch off the RGB LED, type and send;
```bash
rgb 0 0 0
```