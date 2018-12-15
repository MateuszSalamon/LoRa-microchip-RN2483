
float getADC1val()
{   
int PA0value = analogRead(PA0);
float voltage = PA0value * (3.3 / 4095.0); //12bit ADC
float ohm = (voltage * (48.7342)) + 15.6899;//line from 100 Ohm = 0 degC to 138.5 Ohm = 100 degC
float degree = (ohm * (1/0.385)) - (100/0.385); // line from 100 Ohm = 138.5 Ohm
return degree;
}


float getADC2val()
{   
int PA0value = analogRead(PA0);
float voltage = PA0value * (3.3 / 4095.0); //12bit ADC
float ohm = (voltage * (52.921)) + 13.5007;//line from 100 Ohm = 0 degC to 138.5 Ohm = 100 degC
float degree = (ohm * (1/0.385)) - (100/0.385); // line from 100 Ohm = 138.5 Ohm
return degree;
}


void setup() {
  // put your setup code here, to run once:
Serial.begin(57600);

}

void loop() {
  
  // put your main code here, to run repeatedly:
  //int sensorValue = analogRead(PA0);
  // Convert the analog reading (which goes from 0 - 4095) to a voltage (0 - 3.3V):
  //float voltage = sensorValue * (3.3 / 4095.0);
  // print out the value you read:
  float degree = getADC1val();
  
  //int PA1value = analogRead(PA0);
  //float voltage = PA1value * (3.3 / 4095.0); //12bit ADC
 // float ohm = (voltage * (48.7342)) + 15.6899; //line from 100 Ohm = 0 degC to 138.5 Ohm = 100 degC
  //float degree = (ohm * (1/0.385)) - (100/0.385);// line from 100 Ohm = 138.5 Ohm
  
  Serial.println(degree);
  //Serial.println(ohm);
  //Serial.println(voltage);
  //Serial.println(analogRead(PA0));
  //Sleep()
  
  delay(5000);
}
