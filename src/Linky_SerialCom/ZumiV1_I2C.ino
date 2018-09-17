#include <Wire.h>
#define SLAVE_ADDRESS 0x04
#define MPU6050_ADDRESS 0x68

//for setting up motor controller
int STBY = 8;
int PWMB = 11;
int BIN2 = 10;
int BIN1 = 9;
int PWMA = 5;
int AIN1 = 7;
int AIN2 = 6;

short int inBuffer[16];
int gyroData[6];
int binData[16];
int hexData[12];
short int i,j,k;
int16_t ax,ay,az,temp,gx,gy,gz;
int speedStepSize = 10;
int speed = 30;

bool isReading = 1;

void moveStop(){
  analogWrite(PWMA,0);
  digitalWrite(AIN1,LOW);
  digitalWrite(AIN2,LOW);

  analogWrite(PWMB,0);
  digitalWrite(BIN1,LOW);
  digitalWrite(BIN2,LOW);
}

void moveForward(int speedA, int speedB){
  analogWrite(PWMA,speedA);
  digitalWrite(AIN1,HIGH);
  digitalWrite(AIN2,LOW);

  analogWrite(PWMB,speedB);
  digitalWrite(BIN1,HIGH);
  digitalWrite(BIN2,LOW);
}

void moveLeft(int speedA, int speedB){
  analogWrite(PWMA,speedA);
  digitalWrite(AIN1,HIGH);
  digitalWrite(AIN2,LOW);

  analogWrite(PWMB,speedB);
  digitalWrite(BIN1,LOW);
  digitalWrite(BIN2,HIGH);
}

void moveRight(int speedA, int speedB){
  analogWrite(PWMA,speedA);
  digitalWrite(AIN1,LOW);
  digitalWrite(AIN2,HIGH);

  analogWrite(PWMB,speedB);
  digitalWrite(BIN1,HIGH);
  digitalWrite(BIN2,LOW);
}

void moveBackward(int speedA, int speedB){
  analogWrite(PWMA,speedA);
  digitalWrite(AIN1,LOW);
  digitalWrite(AIN2,HIGH);

  analogWrite(PWMB,speedB);
  digitalWrite(BIN1,LOW);
  digitalWrite(BIN2,HIGH);
}

void intToBin(int x){
  //Takes a signed int and stores the bits in an array
  int i;
  
  //Set leftmost bit to 1 if negative, 0 otherwise
  if(x<0){
    x =- x;
    binData[0] = 1;
  }
  else binData[0] = 0;

  //Store the rest of the bits in an array, from right to left
  for(i=15;i>0;i--){
    binData[i] = x%2;
    x -= x%2;
    x /= 2;
  }
}

void binToHex(int x){
  //Takes the array created from intToBin(int x), converts it to hex, then inserts the
  //two values at index x
  int i,j,k;
  int a = 0;
  int b = 1;

  //For each of the 2 bytes....
  for(i=0;i<2;i++){
    //For each of the 8 bits per byte...
    for(j=0;j<8;j++){
      //Multiply each bit by 2^b, where b is the index of the bit, from right-to-left
      for(k=0;k<j;k++) b*=2;
      //Add the results into one total i.e. the hexadecimal value
      a+=binData[15-(i*8+j)]*b;
      b = 1;
    }
    //Insert the hexidecimal value into an array at index x
    hexData[x+i] = a;
    a = 0;
  }
}

void setup() {
  // put your setup code here, to run once:
  Wire.begin(SLAVE_ADDRESS);
  Wire.onReceive(receiveData);
  Wire.onRequest(sendData);

  pinMode(STBY,OUTPUT);
  pinMode(PWMB,OUTPUT);
  pinMode(PWMA,OUTPUT);
  pinMode(AIN2,OUTPUT);
  pinMode(AIN1,OUTPUT);
  pinMode(BIN2,OUTPUT);
  pinMode(BIN1,OUTPUT);
  digitalWrite(STBY,HIGH);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(isReading == 0){
    for(j=0;j<i;j++){
      switch(inBuffer[j]){
        case 64: // character "@"
          moveForward(inBuffer[j+1], inBuffer[j+2]);
          break;
        case 65: // character "A"
          moveRight(inBuffer[j+1], inBuffer[j+2]);
          break;
        case 66: // character "B"
          moveLeft(inBuffer[j+1], inBuffer[j+2]);
          break;
        case 67: // character "C"
          moveBackward(inBuffer[j+1], inBuffer[j+2]);
          break;
        case 68: // character "D"
          Wire.beginTransmission(MPU6050_ADDRESS);
          Wire.write(0x3B);
          Wire.endTransmission();
          Wire.requestFrom(MPU6050_ADDRESS,14,true);
          ax=Wire.read()<<8|Wire.read();
          ay=Wire.read()<<8|Wire.read();
          az=Wire.read()<<8|Wire.read();
          temp=Wire.read()<<8|Wire.read();
          gx=Wire.read()<<8|Wire.read();
          gy=Wire.read()<<8|Wire.read();
          gz=Wire.read()<<8|Wire.read();
          gyroData[0] = ax / 163.84;
          gyroData[1] = ay / 163.84;
          gyroData[2] = az / 163.84;
          gyroData[3] = gx / 1.31;
          gyroData[4] = gy / 1.31;
          gyroData[5] = gz / 1.31;
          for(k=0;k<6;k++){
            intToBin(gyroData[k]);
            binToHex(k*2);
          }
          break;
        case 77:// character "M"
          moveForward(speed,speed);
          break;
        case 78:// character "N"
          moveBackward(speed,speed);
          break;
        case 79:// character "O"
          moveLeft(speed,speed);
          break;
        case 80://character "P"
          moveRight(speed, speed);
          break;
        case 81: //character "Q"
          moveStop();
          break;
        case 86: //character "V"
          speed = speed - speedStepSize;//decrease the speed
          if(speed<0) speed = 0;
          break;
        case 87: //character "W"
          speed = speed + speedStepSize;//increase the speed
          if(speed>100) speed = 100;
          break;
        default:
          break;
      }
    }
    i = 0;
    isReading = 1;
  }
}

void receiveData(){
  if(isReading == 1){
    while(Wire.available()){
      inBuffer[i] = Wire.read();
      if(inBuffer[i] == 126){
        j = 0;
        isReading = 0;
      }
      else i++;
    }
  }
}

void sendData(){
  for(k=0;k<12;k++) Wire.write(hexData[k]);
}

