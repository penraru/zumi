#include <Wire.h>
#include <MPU6050_tockn.h>
#define SLAVE_ADDRESS 0x04

MPU6050 mpu6050(Wire);

//for setting up motor controller
int STBY = 8;
int PWMB = 11;
int BIN2 = 10;
int BIN1 = 9;
int PWMA = 5;
int AIN1 = 7;
int AIN2 = 6;

int speedStepSize = 10;
int doOnce = 0;
int speed = 30;

float dAngle = 0.0;
float angle, initAngle;

void moveStop() {
  analogWrite(PWMA, 0);
  digitalWrite(AIN1, LOW);
  digitalWrite(AIN2, LOW);

  analogWrite(PWMB, 0);
  digitalWrite(BIN1, LOW);
  digitalWrite(BIN2, LOW);
}

void moveForward(int speedA, int speedB) {
  analogWrite(PWMA, speedA);
  digitalWrite(AIN1, HIGH);
  digitalWrite(AIN2, LOW);

  analogWrite(PWMB, speedB);
  digitalWrite(BIN1, HIGH);
  digitalWrite(BIN2, LOW);
}

void moveLeft(int speedA, int speedB) {
  analogWrite(PWMA, speedA);
  digitalWrite(AIN1, HIGH);
  digitalWrite(AIN2, LOW);

  analogWrite(PWMB, speedB);
  digitalWrite(BIN1, LOW);
  digitalWrite(BIN2, HIGH);
}

void moveRight(int speedA, int speedB) {
  analogWrite(PWMA, speedA);
  digitalWrite(AIN1, LOW);
  digitalWrite(AIN2, HIGH);

  analogWrite(PWMB, speedB);
  digitalWrite(BIN1, HIGH);
  digitalWrite(BIN2, LOW);
}

void moveBackward(int speedA, int speedB) {
  analogWrite(PWMA, speedA);
  digitalWrite(AIN1, LOW);
  digitalWrite(AIN2, HIGH);

  analogWrite(PWMB, speedB);
  digitalWrite(BIN1, LOW);
  digitalWrite(BIN2, HIGH);
}

void setup() {
  // put your setup code here, to run once:
  Wire.begin(SLAVE_ADDRESS);
  Wire.onReceive(receiveData);
  Wire.onRequest(sendData);

  mpu6050.begin();
  mpu6050.calcGyroOffsets(true);

  pinMode(STBY, OUTPUT);
  pinMode(PWMB, OUTPUT);
  pinMode(PWMA, OUTPUT);
  pinMode(AIN2, OUTPUT);
  pinMode(AIN1, OUTPUT);
  pinMode(BIN2, OUTPUT);
  pinMode(BIN1, OUTPUT);
  digitalWrite(STBY, HIGH);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(dAngle > 0.0){
    mpu6050.update();
    angle = mpu6050.getAngleZ();
    if(doOnce == 0){
      initAngle = angle;
      doOnce = 1;
    }
    if(abs(angle - initAngle) > dAngle){
      moveStop();
      dAngle = 0.0;
      doOnce = 0;
    }
  }
  delay(100);
}

void receiveData() {
  while (Wire.available()) {
    switch (Wire.read()) {
      case 64: // character "@"
        moveForward(Wire.read(), Wire.read());
        break;
      case 65: // character "A"
        moveRight(Wire.read(), Wire.read());
        break;
      case 66: // character "B"
        moveLeft(Wire.read(), Wire.read());
        break;
      case 67: // character "C"
        moveBackward(Wire.read(), Wire.read());
        break;
      case 68: // character "D"
        //Serial.println("Test");
        moveLeft(speed, speed);
        dAngle = Wire.read();
        dAngle *= 5;
        break;
      case 69: // character "D"
        moveRight(speed, speed);
        dAngle = Wire.read();
        dAngle *= 5;
        break;
      case 70: // character "F"
        speed = Wire.read();
        break;
      case 77:// character "M"
        moveForward(speed, speed);
        break;
      case 78:// character "N"
        moveBackward(speed, speed);
        break;
      case 79:// character "O"
        moveLeft(speed, speed);
        break;
      case 80://character "P"
        moveRight(speed, speed);
        break;
      case 81: //character "Q"
        moveStop();
        break;
      default:
        break;
    }
  }
}

void sendData(){
  if(dAngle > 0.0) Wire.write(1);
  else Wire.write(0);
}

