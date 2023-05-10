//Gamepad BT receiver code for Arduino (DigiSpark) v0.4 by BeardoGuy
//22/05/2021
//based on DigisparkJoystick by Digistump LLC https://github.com/digistump/DigisparkArduinoIntegration/tree/master/libraries/DigisparkJoystick

#include "DigiJoystick.h"
#include <SoftSerial_INT0.h>

#define P_RX 2                        // Reception PIN (SoftSerial)
#define P_TX 1                        // Transmition PIN (SoftSerial)
#define BLE_TIMEOUT 10000  
byte lowb=0; // how to change individual bits: byte ^= (-newValue ^ byte) & (1 << n);
byte hib=0;
byte btnChange=0;
SoftSerial BLE(P_RX, P_TX);

void setup() {
  BLE.begin(2400); // Initialize the serial port
  
  //Centering all Joysticks and resetting the buttons
  DigiJoystick.setX((byte) (0x7F));
  DigiJoystick.setY((byte) (0x7F));
  DigiJoystick.setXROT((byte) 0x7F);
  DigiJoystick.setYROT((byte) 0x7F);
  DigiJoystick.setZROT((byte) 0x7F);
  DigiJoystick.setSLIDER((byte) 0x7F);
  DigiJoystick.setButtons((byte)0x00, (byte)0x00);
}


void loop() {
  // If not using plentiful DigiJoystick.delay() calls, make sure to
  //DigiJoystick.update(); // call this at least every 50ms
  // calling more often than that is fine
  // this will actually only send the data every once in a while unless the data is different  
 
  static char cmd; // Get Command variable
    
    if(BLE.available()) // If there is any data incoming from the serial port
    {
        cmd = BLE.read(); // Get command
        if(cmd == 'C')
        {
          }
        // Manage the command received
        if(cmd=='u' || cmd=='d')
            DigiJoystick.setY((byte) (0x7F));
        else if(cmd == 'U')
            DigiJoystick.setY((byte) 0x00);
        else if(cmd == 'D')
            DigiJoystick.setY((byte) 0xFF);
                 
        // ...
        if(cmd=='l' || cmd=='r')
            DigiJoystick.setX((byte) (0x7F));
        else if(cmd == 'L')
            DigiJoystick.setX((byte) (0x00));
        else if(cmd == 'R')
            DigiJoystick.setX((byte) (0xFF)); 
        
        //buttons start here
        if(cmd=='f') //5
        {
          lowb ^= (-0 ^ lowb) & (1 << 1);//2nd button B
          btnChange=1;
          }
        else if(cmd=='F')
        {
          lowb ^= (-1 ^ lowb) & (1 << 1);
          btnChange=1;
          }

        if(cmd=='e') //7
        {
          lowb ^= (-0 ^ lowb) & (1 << 2);//3rd button A
          btnChange=1;
          }
        else if(cmd=='E'){
          lowb ^= (-1 ^ lowb) & (1 << 2);
          btnChange=1;
          }
          
        if(cmd=='o') //4
        {
          lowb ^= (-0 ^ lowb) & (1 << 3); //4th button X
          btnChange=1;
          }
        else if(cmd=='O'){
          lowb ^= (-1 ^ lowb) & (1 << 3);
          btnChange=1;
          }

        if(cmd=='n') //1
        {
          lowb ^= (-0 ^ lowb) & (1 << 0); //4th button X
          btnChange=1;
          }
        else if(cmd=='N'){
          lowb ^= (-1 ^ lowb) & (1 << 0);
          btnChange=1;
          }

         if(cmd=='t') //star
        {
          lowb ^= (-0 ^ lowb) & (1 << 6); //7th button L2
          btnChange=1;
          }
        else if(cmd=='T'){
          lowb ^= (-1 ^ lowb) & (1 << 6);
          btnChange=1;
          }  

         if(cmd=='g') //8
        {
          lowb ^= (-0 ^ lowb) & (1 << 7); //8th button R2
          btnChange=1;
          }
        else if(cmd=='G'){
          lowb ^= (-1 ^ lowb) & (1 << 7);
          btnChange=1;
          }  

        if(cmd=='w') //2
        {
          lowb ^= (-0 ^ lowb) & (1 << 4); //5th button L1
          btnChange=1;
          }
        else if(cmd=='W'){
          lowb ^= (-1 ^ lowb) & (1 << 4);
          btnChange=1;
          }  

        if(cmd=='h') //3
        {
          lowb ^= (-0 ^ lowb) & (1 << 5); //6th button R1
          btnChange=1;
          }
        else if(cmd=='H'){
          lowb ^= (-1 ^ lowb) & (1 << 5);
          btnChange=1;
          }  
 
              
        if(cmd=='s') //select OK
        {
          hib ^= (-0 ^ hib) & (1 << 1); //10th button start
          btnChange=1;
          }
        else if(cmd=='S'){
          hib ^= (-1 ^ hib) & (1 << 1);
          btnChange=1;
          }
          
        if(cmd=='a') //hash
        {
          hib ^= (-0 ^ hib) & (1 << 0); //9th button select
          btnChange=1;
          }
        else if(cmd=='A'){
          hib ^= (-1 ^ hib) & (1 << 0);
          btnChange=1;
          }    

        if(cmd=='i') //9
        {
          hib ^= (-0 ^ hib) & (1 << 2); //11th button select
          btnChange=1;
          }
        else if(cmd=='I'){
          hib ^= (-1 ^ hib) & (1 << 2);
          btnChange=1;
          }        
        
        if(btnChange==1){    
        DigiJoystick.setButtons((byte)lowb, (byte)hib);
        btnChange=0;}
        
    }
    
  // it's best to use DigiJoystick.delay() because it knows how to talk to
  // the connected computer - otherwise the USB link can crash with the 
  // regular arduino delay() function
  DigiJoystick.delay(12); // wait 12 milliseconds
}
