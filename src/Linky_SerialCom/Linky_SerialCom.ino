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
int basicSpeed = 100;
int speed = 100;
int speedStepSize = 10;

int inBuffer[64];
bool isReading = 1;
short int i;
short int j;

void setup()
{
  Serial.begin(115200);
  LowBatCheck();        //  Low Battery check - 3.7v
  initialize();
  setupLineTracer();
  LedDisplay(1, 100);
}

void loop()
{
  if (ReadVoltage() < 3.7)  LEDColorR(100); //  Low battery, red color
  else if (ReadMic() > 600) LEDColorG(100); //  bright 0~100 ,100: always on
  else  LEDColorG(0); //0: off

  if(isReading == 1)
  {
    //check if the serial monitor has anything sent
    if(Serial.available() > 0)
    {
      inBuffer[i] = int(Serial.read());
      if(inBuffer[i] == 10)
      {
        j = 0;
        isReading = 0;
      }
      else ++i;
    }
  }
  else
  {
    for(j=0;j<i;++j)
    {
      switch(inBuffer[j])
      {
        case 64: // character "@"
          DCMotor(M1, CCW, inBuffer[j+1]);
          DCMotor(M2, CW, inBuffer[j+2]);
          j=i;
          break;
        case 65: // character "A"
          DCMotor(M1, CCW, inBuffer[j+1]);
          DCMotor(M2, CCW, inBuffer[j+2]);
          j=i;
          break;
        case 66: // character "B"
          DCMotor(M1, CW, inBuffer[j+1]);
          DCMotor(M2, CW, inBuffer[j+2]);
          j=i;
          break;
        case 67: // character "C"
          DCMotor(M1, CW, inBuffer[j+1]);
          DCMotor(M2, CCW, inBuffer[j+2]);
          j=i;
          break;
        case 75: // letter "K"
          LineTracer(speed);
          break;
  
        //------------------------------------------------------------------------
        case 76: //character "L"
          //Print all the data
          //top Left IR sensor
          Serial.print(analogRead(SFL));
          Serial.print(",");
          //top Middle IR
          Serial.print(analogRead(SFF));
          Serial.print(",");
          //top Right IR sensor
          Serial.print(analogRead(SFR));
          Serial.print(",");
          //Bottom Left IR sensor
          Serial.print(analogRead(SBL));
          Serial.print(",");
          //Bottom Right IR sensor
          Serial.print(analogRead(SBR));
          Serial.print(",");
          //Read Voltage of battery
          Serial.print(ReadVoltage());
          Serial.print(",");
          //Read the MIC
          Serial.println(ReadMic());
          break;

        //------------------------------------------------------------------------
        case 77:// character "M"
          DCMove(forward,speed);
          break;

        //------------------------------------------------------------------------
        case 78:// character "N"
          DCMove(backward,speed);
          break;
  
        //------------------------------------------------------------------------
        case 79:// character "O"
          DCMove(left,speed);
          break;
  
        //------------------------------------------------------------------------
        case 80://character "P"
          DCMove(right,speed);
          break;
  
        //------------------------------------------------------------------------
        case 81: //character "Q"
          DCMove(stop,speed);
          break;
  
        //------------------------------------------------------------------------
        //MOTOR SPEED
        //========================================================
        case 86: //character "V"
          speed = speed - speedStepSize;//decrease the speed
          if(speed<0)
          {
            speed = 0;
          }
          break;
  
        //========================================================
        case 87: //character "W"
          speed = speed + speedStepSize;//increase the speed
          if(speed>100)
          {
            speed = 100;
          }
          break;


        case 90: //character "Z"
          //Currently placing dummy variables
          //since RoPi library is expecting data
          Serial.print("0");
          Serial.print(" ");
          Serial.print("0");
          Serial.print(" ");
          Serial.print("0");
          Serial.print(" ");
          Serial.print(speed);
          Serial.print(" ");
          Serial.print("0");
          Serial.print(" ");
          Serial.print("0");
          Serial.print(" ");
          Serial.println("0");
          //Serial.println(" ");
          break;
    
        //========================================================
        case 112: //character "p"
          Sound_Coin();
          break;
  
        //========================================================
        default:
          break;
      }
    }
    i=0;
    isReading=1;
  }
}
