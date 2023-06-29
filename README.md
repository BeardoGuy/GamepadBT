# GamepadBT for Symbian S60
![Screenshot_N-Gage_QD](https://github.com/BeardoGuy/GamepadBT/blob/main/Screenshots/ScreenshotMainv3.01.jpg?raw=true)
    ![Screenshot_N-Gage_QD](https://github.com/BeardoGuy/GamepadBT/blob/main/Screenshots/Scr.%20shot.Main.jpg?raw=true)

Project to convert Symbian Series60 mobile into a Bluetooth Gamepad specifically the Nokia N-Gage and N-Gage QD.  
It should work with all Symbian Series 60 1st and 2nd Edition devices.  
Tested on Nokia N-gage QD with v4.60 firmware.

# Software:
1) Requires "Python for S60" (PyS60) installed to work, download the appropriate version from here:
* For Series 60 1st Edition (N-Gage and N-Gage QD), download from this link: [Download](https://sourceforge.net/projects/pys60/files/pys60/1.3.1/PythonForS60_1stEd_1_3_1.SIS/download)  
* For Series 60 2nd Edition (6600, 3230, 7610 etc.), download from this link: [Download](https://sourceforge.net/projects/pys60/files/pys60/1.3.23/PythonForS60_1_3_23_2ndEd.SIS/download)  

2) Download the SIS file and Arduino Code from the [Releases](https://github.com/BeardoGuy/GamepadBT/releases/) 

# Hardware:
![Wiring_diagram_Digispark_HC06](https://github.com/BeardoGuy/GamepadBT/blob/main/Schematics/Digispark_Wiring_Diagram-001.jpg?raw=true)

1) You'll need to make a USB Bluetooth Receiver (no soldering required) for the client side (for PC, Android, or any other device supporting a USB Gamepad)

Required components:
* HC-05/HC-06 or any other Serial Bluetooth Module
* ATtiny85 USB development board (aka DigiSpark)  

2) Upload the Arduino Code to the Digispark using Arduino IDE. Make sure you have already added "Digistump AVR Boards" from Boards manager in the Arduino IDE by clicking on Tools > Boards > Boards Manager and type "Digistump" in the search box and click install.
* Requires Arduino DigisparkJoystick Library from: https://github.com/digistump/DigisparkArduinoIntegration/tree/master/libraries/DigisparkJoystick
* Requires Arduino Digispark_SoftSerial-INT0 Library from: https://github.com/J-Rios/Digispark_SoftSerial-INT0

# Connection Process:
* Plug the receiver you made into any USB Gamepad supporting device (PC, Android, Game console,etc.) and it will show up as a USB Gamepad. 
* Install GamepadBT app on N-Gage and search for your HC06 Bluetooth module and enter the passcode for pairing (default is 0000 or 1234)  
* Now the N-Gage should work seamlessly as a wireless gamepad.  


If you like my work, you can buy me a cup of coffee:)  
BTC address: bc1qgy37r3ns6lqr00yzxkc0ednhy76lf3yqrqcx5e
