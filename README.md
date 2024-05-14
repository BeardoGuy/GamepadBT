# GamepadBT for Symbian S60

![Screenshot_N-Gage_QD](https://github.com/BeardoGuy/GamepadBT/blob/main/Screenshots/GamepadBT_v3.01.jpg?raw=true)

Project to convert Symbian Series60 mobile into a Bluetooth Gamepad specifically the Nokia N-Gage and N-Gage QD.  
It should work with all Symbian Series 60 1st and 2nd Edition devices.  
Tested on Nokia N-gage QD with v4.60 firmware.

# Software for N-Gage:
1) Requires "Python for S60" (PyS60) installed to work, download the appropriate version from here:
* For Series 60 1st Edition (N-Gage and N-Gage QD), download from this link: [Download](https://sourceforge.net/projects/pys60/files/pys60/1.3.1/PythonForS60_1stEd_1_3_1.SIS/download)  
* For Series 60 2nd Edition (6600, 3230, 7610 etc.), download from this link: [Download](https://sourceforge.net/projects/pys60/files/pys60/1.3.23/PythonForS60_1_3_23_2ndEd.SIS/download)  

2) Download the SIS file from the [Releases](https://github.com/BeardoGuy/GamepadBT/releases/) 

# Software for Windows PC (NEW):  
If you want to use the N-Gage as Gamepad only for Windows PC then you can try the new [GamepadBT-Server](https://github.com/BeardoGuy/GamepadBT-Server/) program. Additional Hardware is not required.
* The Server Program will only work if your N-Gage/Symbian device can connect to your PC over Bluetooth normally and can transfer files without error.(otherwise see the Hardware section). Some modern inbuilt Bluetooth adapters cannot connect to these older Symbian devices, so please try to pair and send a file before using.
  
# Hardware: (Only needed if you want to make a Universal USB dongle for all devices or if the Server program doesn't work for you or if you want native Direct Input Joystick support)
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
