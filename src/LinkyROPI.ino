/*------ Board Select ----------------------------
    Arduino Pro or Pro Mini
    Atmega328 (5V, 16Mhz)
  ------------------------------------------------*/
/*-------------------------------------------------
  tunning sensor -linetracer
  Remocon set channel (0~4) - tv remocon
  Low Battery check - 3.7v
  Speed Change => Remocon Mode
  ------------------------------------------------*/
#include "config.h"
#include "ex_Linky.h"
#include "ex_Unplugged.h"
#include "RokitFirmata.h"

int mode = 0;
int basicSpeed = 0;
int speed = 100;
void setup()
{
  Serial.begin(115200);
  LowBatCheck();        //  Low Battery check - 3.7v
  initialize();

  //-------------------------------------------------------------------------------------------------------------------------------------------//
  // if (!digitalRead(SW1) && !digitalRead(SW2))     TestMode(); // sw1, sw2 Push hold and Power On
  //-------------------------------------------------------------------------------------------------------------------------------------------//

  //mode = ModeSelect();
  mode = AVOID;
  //if (mode == FIRMATA)  RokitFiramata();
 // basicSpeed = DCSpeedLoad();
 basicSpeed = 100;

  Sound_1up();
  LedDisplay(1, 100);
}

void loop()
{
 // if (mode == AVOID)              Avoid(basicSpeed);      //  sensor Left
 // else if (mode == LINE_TRACER)   LineTracer(basicSpeed); //  sensor Right
 // else if (mode == UNPLUGGED)     Unplugged(basicSpeed);   //  sensor Front  (Unplugged & Remocon)
  //Avoid(basicSpeed);

  int sound = ReadMic();      // Sensing clap sound
  float vin = ReadVoltage();  // Read Voltage

  if (vin < 3.7)  LEDColorR(100);       //  Low battery, red color
  else if (sound > 600) LEDColorG(100); //  bright 0~100 ,100: always on
  else  LEDColorG(0); //0: off

  //PrintSensor();
  //Sound_FireBall();
  //Sound_Coin();
  ropiSwitch();
}

void ropiSwitch(){
  byte readbyte = 0;

  //check if the serial monitor has anything sent
 if(Serial.available() > 0)
 {
  readbyte = Serial.read();
  //if there is something sent via the serial monitor save the byte
 }
 //readbyte will be an ASCII character or letter
  switch(readbyte)
  { 
   //------------------------------------------------------------------------  
   case 76: //character "L"
   //Print all the data
   //top Left IR
  Serial.print(analogRead(SFL));
  Serial.print(",");
  //top Middle IR
  Serial.print(analogRead(SFF));
  Serial.print(",");
  //top Right IR
  Serial.print(analogRead(SFR));
  Serial.print(",");
  //Bottom Left IR
  Serial.print(analogRead(SBL));
  Serial.print(",");
  //Bottom Right IR
  Serial.print(analogRead(SBR));
  Serial.print(",");
  //Read Voltage
  Serial.print(ReadVoltage());
  Serial.print(",");
  //Read the MIC
  Serial.println(ReadMic());
 
  break; 
  //------------------------------------------------------------------------  
  case 77:// character "M" 
  //SmartInventor.DCMove(forward,speed);
  DCMove(forward,speed);
                       
  break;  
  //------------------------------------------------------------------------
  case 78:// character "N" 
  //SmartInventor.DCMove(backward,speed); 
  DCMove(backward,speed);        
  break; 
  //------------------------------------------------------------------------
  case 79:// character "O" 
  //SmartInventor.DCMove(left,speed);
  DCMove(left,speed); 
  break;
  //------------------------------------------------------------------------
  case 80://character "P"
  //SmartInventor.DCMove(right,speed); 
  DCMove(right,speed);       
  break;
  //------------------------------------------------------------------------
  case 81: //character "Q"
  //SmartInventor.DCMove(stop,speed);
  DCMove(stop,speed);
  break;
  //------------------------------------------------------------------------
  default:
  break;
  
  }
}

