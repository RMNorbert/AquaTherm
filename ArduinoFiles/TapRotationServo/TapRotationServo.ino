#include <Servo.h>

Servo myServo;  // create servo object to control the positional rotation servo
String cmd;
int initialPos = 0;
int openingPos = 90;

void setup() {
  myServo.attach(5);  // attaches the servo on pin 5 to the servo object
  Serial.begin(115200);
  myServo.write(initialPos);
}

void loop() {
   while(Serial.available()==0) {

  }
  cmd=Serial.readStringUntil('\r');
  // sets the servo position according to the scaled value use 0 or 90 
  if(cmd=="on"){
    myServo.write(openingPos); //open the tap
  }
  if(cmd=="off"){
    myServo.write(initialPos); // closing the tap
  }
  delay(1000);  // waits for the servo to get there
}
