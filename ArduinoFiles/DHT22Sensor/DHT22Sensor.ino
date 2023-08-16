#include <SimpleDHT.h> 
//pinDHT22 where the sensor is connected
// for DHT22,
//      VCC: 5V or 3V
//      GND: GND
//      DATA: 2
int pinDHT22 = 2;
SimpleDHT22 dht22(pinDHT22);
//connection
void setup() {
  Serial.begin(115200);
}
//main loop
void loop() {
  // start working...
  // read without samples.
  // @remark We use read2 to get a float data, such as 10.1*C
  //    if user doesn't care about the accurate data, use read to get a byte data, such as 10*C.
  float temperature = 0;
  float humidity = 0;
  int err = SimpleDHTErrSuccess;
  if ((err = dht22.read2(&temperature, &humidity, NULL)) != SimpleDHTErrSuccess) {
    Serial.print("Read DHT22 failed, err="); Serial.print(SimpleDHTErrCode(err));
    Serial.print(","); Serial.println(SimpleDHTErrDuration(err)); delay(2000);
    return;
  }
  //this provide the temperature and humidity
  String response = String((float)temperature) + "," + String((float)humidity) + ",";
  Serial.print(response); for online response simulation
  // DHT22 sampling rate is 0.5HZ.
  delay(1500);
}
