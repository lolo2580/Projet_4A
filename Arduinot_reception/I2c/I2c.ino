#include <Wire.h>
#include <SPI.h>
#include <Mirf.h>
#include <nRF24L01.h>
#include <MirfHardwareSpiDriver.h>
 
#define SLAVE_ADDRESS 0x04
int number = 0;
int state = 0;
//String data = "ABC";
//char a='3',b='d',c='S',d='5',e='R',f='0',g='7',h='/',x=0;
//char tab[8]={'3','a','0','0','0','0','0','0'};
//int i=0;
//char sendStatus[8] = "4C3456r"; // initialize the container variable
char sendStatus[8] = "abcdef"; // initialize the container variable
int index = 0; // initialize the index variable

void setup() 
{
    pinMode(13, OUTPUT);
    pinMode(8, INPUT);           // set pin to input
    digitalWrite(8, HIGH);       // turn on pullup resistors
    Serial.begin(9600);         // start serial for output
    // initialize i2c as slave
    Wire.begin(SLAVE_ADDRESS);

    // define callbacks for i2c communication
    Wire.onReceive(receiveData);
    Wire.onRequest(sendData);   

  //  Serial.println("Go !"); 
  //  Serial.println("Ready!");
  //Serial.println("Attente d'un scan de carte: ");
}

void loop() {

      delay(100);

}
/*
void receiveData(int byteCount){
   Serial.print("data received: ");
        String strMsg;
   while(Wire.available() > 0) {
           char c = Wire.read();
      strMsg += String(c);
   }
   Serial.println();
   Serial.print(strMsg);
   Serial.println();
   
}
*/

// callback for received data
void receiveData(int byteCount){

    while(Wire.available()) {
        number = Wire.read();
        Serial.print("Data received: ");
        Serial.println(number);

        if (number == 1) // Une lecture de
        {
          
            Serial.println("Scan de carte demande: ");
                //if (state == 0)
                //  digitalWrite(13, HIGH); // set the LED on
               // state = 1;
         }
         else if(number == 2)
         {
                  Serial.println("Lecture OK, Carte suivante: ");
                  //digitalWrite(13, LOW); // set the LED off
                //state = 0;
         }
        
     }
}

// callback for sending data
void sendData(){

Wire.write(sendStatus[index]);
++index;
if (index >= 8)
{
    index = 0;
}  
   // Wire.write(strMsg);
  //byte buffer[3];
  //buffer[0]=1;
  /*
  switch(number)
  {
  case 0:
  Wire.write(tab[0]);
  break;
  case 1:
  Wire.write(tab[1]);
  break;
  case 2:
  Wire.write(tab[2]);
  break;
  case 3:
  Wire.write(tab[3]); 
  break;
  case 4:
  Wire.write(tab[4]);
  break; 
  case 5:
  Wire.write(tab[5]); 
    break;
  case 6:
  Wire.write(tab[6]); 
    break;
  case 7:  
  Wire.write(tab[7]); 
    break;  
 */   
  
}
/*
void receiveData(int byteCount){
   Serial.print("data received: ");
        String strMsg;
   while(Wire.available() > 0) {
           char c = Wire.read();
      strMsg += String(c);
   }
   Serial.println();
   Serial.print(strMsg);
   Serial.println();
   
}
*/
