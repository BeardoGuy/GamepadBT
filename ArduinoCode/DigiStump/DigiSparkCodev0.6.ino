//GamepadBT Receiver code for DigiSpark Attiny85 
//Internal version QD 0.3 29/06/2023

#include "DigiJoystick.h"
#include <SoftSerial_INT0.h>

#define P_RX 2                        // Reception PIN (SoftSerial)
#define P_TX 1                        // Transmition PIN (SoftSerial)
#define BLE_TIMEOUT 10000  
byte lowb=0;
byte hib=0;
byte btnChange=0;
SoftSerial BLE(P_RX, P_TX);

void setup() {
  BLE.begin(9600); // Initialize the serial port
  
  DigiJoystick.setX((byte) (0x7F)); // scroll X left to right repeatedly
      DigiJoystick.setY((byte) (0x7F));
      DigiJoystick.setXROT((byte) 0x7F);
      DigiJoystick.setYROT((byte) 0x7F);
      DigiJoystick.setZROT((byte) 0x7F);
      DigiJoystick.setSLIDER((byte) 0x7F);
      DigiJoystick.setButtons((byte)0x00, (byte)0x00);
}


void loop() {
  
  static char cmd; // Get Command variable
    
    if(BLE.available()) // If there is any data incoming from the serial port
    {
        cmd = BLE.read(); // Get command
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
        
        //buttons start here*********************************************************************************************
        if(cmd=='f') //-----------------------------------5
        {
          lowb ^= (-0 ^ lowb) & (1 << 4);//5th button
          btnChange=1;
          }
        else if(cmd=='F')
        {
          lowb ^= (-1 ^ lowb) & (1 << 4);
          btnChange=1;
          }

        if(cmd=='e') //------------------------------------7
        {
          lowb ^= (-0 ^ lowb) & (1 << 6);//7th button 
          btnChange=1;
          }
        else if(cmd=='E'){
          lowb ^= (-1 ^ lowb) & (1 << 6);
          btnChange=1;
          }
          
        if(cmd=='o') //------------------------------------4
        {
          lowb ^= (-0 ^ lowb) & (1 << 3); //4th
          btnChange=1;
          }
        else if(cmd=='O'){
          lowb ^= (-1 ^ lowb) & (1 << 3);
          btnChange=1;
          }

        if(cmd=='n') //-------------------------------------1
        {
          lowb ^= (-0 ^ lowb) & (1 << 0); //1st button
          btnChange=1;
          }
        else if(cmd=='N'){
          lowb ^= (-1 ^ lowb) & (1 << 0);
          btnChange=1;
          }

         if(cmd=='t') //------------------------------------star
        {
          hib ^= (-0 ^ hib) & (1 << 2); //11th
          btnChange=1;
          }
        else if(cmd=='T'){
          hib ^= (-1 ^ hib) & (1 << 2);
          btnChange=1;
          }  

         if(cmd=='g') //-------------------------------------8
        {
          lowb ^= (-0 ^ lowb) & (1 << 7); //8th button
          btnChange=1;
          }
        else if(cmd=='G'){
          lowb ^= (-1 ^ lowb) & (1 << 7);
          btnChange=1;
          }  

        if(cmd=='w') //--------------------------------------2
        {
          lowb ^= (-0 ^ lowb) & (1 << 1); //2nd button L1
          btnChange=1;
          }
        else if(cmd=='W'){
          lowb ^= (-1 ^ lowb) & (1 << 1);
          btnChange=1;
          }  

        if(cmd=='h') //--------------------------------------3
        {
          lowb ^= (-0 ^ lowb) & (1 << 2); //3rd button
          btnChange=1;
          }
        else if(cmd=='H'){
          lowb ^= (-1 ^ lowb) & (1 << 2);
          btnChange=1;
          }  
 
              
        if(cmd=='s') //---------------------------------------select OK
        {
          hib ^= (-0 ^ hib) & (1 << 4); //13th button start
          btnChange=1;
          }
        else if(cmd=='S'){
          hib ^= (-1 ^ hib) & (1 << 4);
          btnChange=1;
          }
          
        if(cmd=='a') //----------------------------------------hash
        {
          hib ^= (-0 ^ hib) & (1 << 3); //12th button
          btnChange=1;
          }
        else if(cmd=='A'){
          hib ^= (-1 ^ hib) & (1 << 3);
          btnChange=1;
          }    

        if(cmd=='i') //-----------------------------------------9
        {
          hib ^= (-0 ^ hib) & (1 << 0); //9th button
          btnChange=1;
          }
        else if(cmd=='I'){
          hib ^= (-1 ^ hib) & (1 << 0);
          btnChange=1;
          }
          
        if(cmd=='x') //-----------------------------------------6
        {
          lowb ^= (-0 ^ lowb) & (1 << 5); //6th button
          btnChange=1;
          }
        else if(cmd=='X'){
          lowb ^= (-1 ^ lowb) & (1 << 5);
          btnChange=1;
          }
          
        if(cmd=='z') //-----------------------------------------0
        {
          hib ^= (-0 ^ hib) & (1 << 1); //10th button
          btnChange=1;
          }
        else if(cmd=='Z'){
          hib ^= (-1 ^ hib) & (1 << 1);
          btnChange=1;
          }
          
        if(cmd=='y') //-----------------------------------------GreenKey
        {
          hib ^= (-0 ^ hib) & (1 << 7); //16th button
          btnChange=1;
          }
        else if(cmd=='Y'){
          hib ^= (-1 ^ hib) & (1 << 7);
          btnChange=1;
          }
          
        if(cmd=='j') //-----------------------------------------LeftSoftKey
        {
          hib ^= (-0 ^ hib) & (1 << 5); //14th button
          btnChange=1;
          }
        else if(cmd=='J'){
          hib ^= (-1 ^ hib) & (1 << 5);
          btnChange=1;
          }
          
        if(cmd=='k') //-----------------------------------------RightSoftKey
        {
          hib ^= (-0 ^ hib) & (1 << 6); //15th button
          btnChange=1;
          }
        else if(cmd=='K'){
          hib ^= (-1 ^ hib) & (1 << 6);
          btnChange=1;
          }        
          
        if(cmd=='c') //-----------------------------------------Clear
        {
          DigiJoystick.setSLIDER((byte) 0x7F);
          btnChange=1;
          }
        else if(cmd=='C'){
          DigiJoystick.setSLIDER((byte) 0xFF);
          btnChange=1;
          }        

        if(btnChange==1){    
        DigiJoystick.setButtons((byte)lowb, (byte)hib);
        btnChange=0;}
    }
  
  DigiJoystick.delay(12); // wait 12 milliseconds
  
}