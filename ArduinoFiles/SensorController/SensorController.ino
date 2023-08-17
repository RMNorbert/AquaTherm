#include <Servo.h>
#include <SimpleDHT.h>
#include <Ultrasonic.h>

String cmd;
String response;

class DHT22Sensor {
    float currentTemperature = 0.0f;
    float currentHumidity = 0.0f;
    bool isOn = false;
    SimpleDHT22 dht22;

    public:
    DHT22Sensor(int pin){
        // Constructor implementation
        this -> dht22 = SimpleDHT22(pin);
    }
    void SwitchIsOnState(bool state){
        isOn = state;
    }
    void GetReadings(){
       // We use read2 to get a float data, such as 10.1*C
       //    if user doesn't care about the accurate data, use read to get a byte data, such as 10*C.
      float temperature = 0;
      float humidity = 0;
      int err = SimpleDHTErrSuccess;
      if ((err = this->dht22.read2(&temperature, &humidity, NULL)) != SimpleDHTErrSuccess) {
        Serial.print("Read DHT22 failed, err=");
        Serial.print(SimpleDHTErrCode(err));
        Serial.print(",");
        Serial.println(SimpleDHTErrDuration(err));
        delay(1000);
        response = String(currentTemperature) + "," + String(currentHumidity) + ",";
      }
      currentTemperature = temperature;
      currentHumidity = humidity;

      // Update the global 'response' variable
      response = String(currentTemperature) + "," + String(currentHumidity) + ",";
    }

    bool IsSensorStateOn() {
      return isOn;
    }
    float GetCurrentHumidity() {
      return currentHumidity;
    }
    float GetCurrentTemperature() {
      return currentTemperature;
    }
};
// for 3 pin sensor
class DistanceSensor{
    Ultrasonic distanceSensor;
    int distance = 0;
    public:
    DistanceSensor(int pin){
        this -> distanceSensor = Ultrasonic(pin);
    }
    int GetDistanceInCm() {
        distance = ultrasonic.read();
        return distance;
    }
    bool IsWaterRefillNeeded() {
        int refillDistance = 20; // set the distance that will trigger the refill
        return refillDistance <= distance;
    }
};

class TapServo{
    Servo myServo;  // create servo object to control the positional rotation servo
    int initialPos = 0;
    int openingPos = 90;
    bool isOpen = false;

    public:

    void Attach(int pin) {
        myServo.attach(pin);
    }
    void Detach() {
        myServo.detach();
    }
    void Open() {
        myServo.write(openingPos);
        response += "Tap: turned on,";
    }
    void Close() {
        myServo.write(initialPos);
        response += "Tap: turned off,";
    }

    void AdjustDeviceByHumidity(float humidity) {
        float normalState = 50.0f;
        if(humidity < normalState) {
            Open();
        }
        else if(humidity > normalState && isOpen){
            Close();
        }
        else {
            response += "Tap: turned off,";
        }
    }
};

class Fan{
    bool isOn = false;
    int PWM = 0;
    public:
    Fan(int pin) {
        this -> PWM = pin;
        pinMode(PWM, OUTPUT);
    }

    void TurnOff() {
        isOn = false;
        digitalWrite(PWM, LOW);
        response += "Fan: turned off";
    }

    void TurnOn() {
        isOn = true;
        digitalWrite(PWM, HIGH);
        response += "Fan: turned on";
    }

    void TurnOnLowSpeed() {
        //The Gate pin is being set to an analog value of 300. It will change the specific position or speed.
        //In this case the speed
        //This means applying a PWM signal with a duty cycle corresponding to around 300/255 ≈ 1.18 (approximately 1.18%).
        isOn = true;
        analogWrite(PWM, 300); //if the device supports pulse-width modulation
        response += "Fan: turned on with low speed";
    }

    void TurnOnHighSpeed() {
        isOn = true;
        analogWrite(PWM, 1000);  //if the device supports pulse-width modulation
        response += "Fan: turned on with high speed";
    }

    void AdjustDeviceByTemperature(String aquariumType , float temp) {
       float lowerBound = GetLowerBound(aquariumType);
       float upperBound = GetUpperBound(aquariumType);
       float nearUpperBound = upperBound - 0.5f;
       bool isBetweenLowerAndUpperBound = temp > lowerBound && temp < upperBound;

       if(!isBetweenLowerAndUpperBound){
         if (temp <= lowerBound) {
            TurnOn();
         }
         else if (temp >= nearUpperBound && temp < upperBound ) {
            TurnOnLowSpeed();
         }
         else if (temp >= upperBound) {
            TurnOnHighSpeed();
         }
       }

       else if(isBetweenLowerAndUpperBound && isOn){
          TurnOff();
          return;
       }

       else if(isBetweenLowerAndUpperBound && !isOn) {
          response += "Fan: turned off";
       }
    }

    private:
    int GetLowerBound(String aquariumType) {
        return (aquariumType == "cold") ? 15.0f : (aquariumType == "tropical") ? 23.0f : 21.0f;
    }
    int GetUpperBound(String aquariumType) {
        return (aquariumType == "cold") ? 23.0f : (aquariumType == "tropical") ? 29.0f : 25.5f;
    }
}

TapServo tapServo;
Fan fan(3);  // change to the pin to which the Gate is connected to
DHT22Sensor dht22Sensor(2);  // change to the pin to which the sensor is connected to
DistanceSensor distanceSensor(13); // change to the pin to which the sensor is connected to

void setup(){
    Serial.begin(115200);
    tapServo.Attach(5);  // change to the pin to which the sensor is connected to
}

void manageWaterLevel(int humidity) {
        bool refillWater = distanceSensor.IsWaterRefillNeeded();
        bool distanceReadingIsUnSuccessful = distanceSensor.GetDistanceInCm() == 0;

        if (distanceReadingIsUnSuccessful){
            tapServo.AdjustDeviceByHumidity(humidity);
        }

        else if (refillWater && !distanceReadingIsUnSuccessful) {
            tapServo.Open();
        }

        else if (!refillWater && !distanceReadingIsUnSuccessful) {
            tapServo.Close();
        }
}

void loop(){

    cmd=Serial.readStringUntil('\r');

    if (cmd == "on"){
        dht22Sensor.SwitchIsOnState(true);
    }

    else if (cmd == "off"){
        dht22Sensor.SwitchIsOnState(false);
    }

    if(dht22Sensor.IsSensorStateOn(){
        dht22Sensor.GetReadings();
        delay(500);
        float humidity = dht22Sensor.GetCurrentHumidity;
        float temperature = dht22Sensor.GetCurrentTemperature;
        manageWaterLevel(humidity);
        delay(500);
        fan.AdjustDeviceByTemperature(aquariumType , temperature);

    }

    Serial.print(response);
    delay(1000);
    response = "";
}