int wtime =30 * 1000 * 60;
bool initialized = 0;
short int measuretime = 20000;//20000;  //20sek
String channel ="0"; // set up used channel 

void LoRasetup(String channel){ //keep most parameters on delays are not necessary 
  Serial.println("mac set dr 0");             
  Serial.println("mac set ch drrange "+ channel +" 0 0"); 
  Serial.println("mac set ch dcycle "+ channel +" 0");    
  Serial.println("mac set ch status "+ channel +" on");   
  Serial.println("mac set retx 20");          
  Serial.println("mac set rxdelay1 1500");    
  Serial.println("mac set nwkskey 2b7e151628aed2a6abf7158809cf4f3c");  //default key
  Serial.println("mac set appskey 3C8F262739BFE3B7BC0826991AD0504D");  //default key
  Serial.println("mac set devaddr 001A0640");                          //default device adress
  Serial.println("mac save");                 
  Serial.println("mac join abp");             
  
  
} 

float getADC1val() // temperature conversion
{   
short int PA0value = analogRead(PA0);
float voltage = PA0value * (3.3 / 4095.0); //12bit ADC
float ohm = (voltage * (48.7342)) + 15.6899;//line from 100 Ohm = 0 degC to 138.5 Ohm = 100 degC
float degree = (ohm * (1/0.385)) - (100/0.385); // line from 100 Ohm = 138.5 Ohm
return degree;
}


float getADC2val(float deg)  // humidity conversion
{   
short int PA1value = analogRead(PA1);
float voltage = PA1value * (3.3 / 4095.0); //12bit ADC
//float humidity = (voltage * (44)) - 19;//line at 25deg
float humidity = ((voltage/3.3) - 0.1515)/(0.00636);
float truehumidity = (humidity)/(1.0546-(0.00216*deg));
return truehumidity;
}

float measureTemp(){  //measuring ADC inputs for temperature
  digitalWrite(PB0,HIGH);
  delay(measuretime);
  float degree = getADC1val();
  digitalWrite(PB0,LOW);
  delay(10);
  return degree;
}

float measureHum(float deg){   //measuring ADC inputs for humidity
  digitalWrite(PB1,HIGH);
  delay(0.4 * measuretime);
  float humidity = getADC2val(deg);
  delay(10);
  digitalWrite(PB1,LOW);
  return humidity;
}

String transmod(float d,float h){ /*
  modify temp and hum val into string sign+x+0.x+"c"+y+0.y
  (a/b) temp.t c hum.h
  */
  String s;
  if (h>=100)
  {h = 99.9;}
  if (h<0)
  {h = 0.0;}
  
  int deg = (int) d;//x.0
  float degr = (d - deg) * 10; //0.x->x.0
  int degre = (int) degr; // x.0 -> x

  int hum = (int) h;//y.0
  float humi =( h - hum)*10; //0.y -> y.0
  int humid = (int) humi; // y.0 -> y
  
  
  if (deg>=0){  //positive temperature 
  String s ="a"+(String)deg +(String)degre +"c"+ (String) hum + (String) humid;
  return s;
 // Serial.print(s);
  }
  else if (deg<0){ //negative temperature
    deg = deg * (-1);
    degre = degre * (-1);
  String s ="b"+(String)deg +(String)degre +"c"+ (String) hum + (String) humid;
 // Serial.print(s);
  return s;
  }
}

void fwaiting(float d, float h){ // temperature and humidity
  /*
  ideally this function would be functioning as a Sleep mode with an RTC interrupt but
  none of the libraries I found are working properly and different IDE's have also failed
  to provide a solution.
  x * 1000 = seconds
  x * 1000*60 = minutes
  x * 1000*60*60 = hours
  x * 1000*60*60*24 = days
  */
  initialized = 1;
  
  if (initialized > 0) {
    if (d < 10.0){
      wtime = wtime + (3600000); // below 10 degrees C +60 minutes
    }
    else if (d >= 10.0){
      wtime = wtime - (1800000); // above 10 degrees C -30 minutes
    }
    else if (d >= 20.0){
      wtime = wtime - (3600000); // above 10 degrees C +60 minutes
    }
    
    if (wtime >= (6*60*1000*60)){ // 21600000 = 3 hours
      wtime = (6*60*1000*60);   // max wait time is 6 hours
    }
    else if (wtime <= (30*1000*60)){  //
      wtime = (30*1000*60);   //min wait time is 30 min
    }
    //wtime = 1;  //comment to remove wait restriction 
    delay(wtime);
    
  }
}


void setup() {
  // put your setup code here, to run once:
  Serial.begin(57600);
  pinMode(PB0,OUTPUT);
  pinMode(PB1,OUTPUT);
  //LoRasetup(channel); // uncomment to setup LoRa RN2483 module 
}

void loop() {
  
  // put your main code here, to run repeatedly:
  
  float degree = measureTemp();
  float humidity = measureHum(degree);
  String str = transmod(degree,humidity);

  fwaiting(degree,humidity);
  
  Serial.println(str);
  //Serial.println(humidity);
  
  delay(5000);
}
