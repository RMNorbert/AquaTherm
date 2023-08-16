int PWM = 3;
String cmd;
// arduino(Micro controller) output is 5v at best so i created two way to achieve controlling the fan/fan's

// The first one :
// an outer power source have to be used with N chanel MOSFET transistor there is a picture about its working in the readme
void setup() {
 Serial.begin(125200);
 // Setting PVM pin of the gate to output
 pinMode(PWM, OUTPUT);
 // turn fan off
 digitalWrite(PWM, LOW);
 }

 void loop() {
  while(Serial.available()==0) {

  }
  cmd=Serial.readStringUntil('\r');
  if(cmd=="on"){
    digitalWrite(PWM, High); //open the gate
  }
  if(cmd=="off"){
    digitalWrite(PWM, LOW); // closing the gate
  }
  if(cmd=="on with low speed"){
    //The Gate pin is being set to an analog value of 300. It will change the specific position or speed.
    //In this case the speed
    //This means applying a PWM signal with a duty cycle corresponding to around 300/255 ≈ 1.18 (approximately 1.18%).
    analogWrite(PWM, 300); //if the device supports pulse-width modulation
  }
  if(cmd=="on with high speed"){
    analogWrite(PWM, 1000);  //if the device supports pulse-width modulation
  }

 } 

// The second way:
// A voltage divider network with 10k NTC thermistor (when the heat ↑ then the resistance ↓ and the voltage divider is start to increase
// at normal the resistance is 10k at around 25 C) and a 10k resistor to ground a potentiometer can used in addition to tune this.
// connected to Analog input(0) , use N chanel MOSFET transistor (a voltage controlling device the source go down to ground and
// the drain goes up to the negative terminal of the fan motor the other side of the fan goes to the the other for example plus 12v power source )
// its important to look for the maximum gate threshold voltage to be lower than the micro controllers maximum output voltage to be able to work
// its also important to dont make a connection between the positive lead of the higher voltage supply(HVS) and the breadboard
// it will go straight into the device that need the higher voltage, the ground of the HVS will go to the breadboard and the output of the
// N chanel MOSFET will goes out to the ground on our outer device (Fan), The ground of the Micro controller is tied to the ground of the breadboard
// so both the ground of the MC and HVS is connected to the ground of the breadboard to have the actual current flowing to the signals
// the 5v from the MC going into the positive rail of the BB the MOSFET source is tied to the BB ground the MOSFET gate going to MC digital pin 3