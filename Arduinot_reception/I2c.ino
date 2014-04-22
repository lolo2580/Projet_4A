#include <Wire.h>
#include <SPI.h>
#include <Mirf.h>
#include <nRF24L01.h>
#include <MirfHardwareSpiDriver.h>
 
#define SLAVE_ADDRESS 0x04
int number = 0;
int state = 0;
String data = "ABC";
char a='3',b='d',c='S',d='5',e='R',f='0',g='7',h='/',x=0;
char tab[8]={'0','0','0','0','0','0','0','0'};
int i=0;
void setup() {
    pinMode(13, OUTPUT);
    pinMode(8, INPUT);           // set pin to input
    digitalWrite(8, HIGH);       // turn on pullup resistors
    Serial.begin(9600);         // start serial for output
    // initialize i2c as slave
    Wire.begin(SLAVE_ADDRESS);

    // define callbacks for i2c communication
    Wire.onReceive(receiveData);
    Wire.onRequest(sendData);   
  Mirf.cePin = 8; // CE sur D8
  Mirf.csnPin = 7; // CSN sur D7
  Mirf.spi = &MirfHardwareSpi; // On veut utiliser le port SPI hardware
  Mirf.init(); // Tout est bon ? Ok let's go !
  Mirf.channel = 0; // On va utiliser le canal 0 pour communiquer (128 canaux disponible, de 0 ‡ 127)
  Mirf.payload = sizeof(unsigned long); // = 4, ici il faut dÈclarer la taille du "payload" soit du message qu'on va transmettre, au max 32 octets
  Mirf.config(); // Tout est bon ? Ok let's go !
   
  Mirf.setTADDR((byte *)"nrf01"); // Le 2eme module va envoyer ses info au 1er module
  Mirf.setRADDR((byte *)"nrf02"); // On dÈfinit ici l'adresse du 2eme module
   
  Serial.println("Go !"); 

    Serial.println("Ready!");
}

void loop() {
      char texteRecu[8]="";
      delay(100);
      byte data[Mirf.payload]; // Tableau de byte qui va stocker le message recu
      if(!Mirf.isSending() && Mirf.dataReady()){ // Si un message a ÈtÈ recu et qu'un autre n'est pas en cours d'emission
      //Mirf.getData(data); // on rÈcupÈre le mÈssage
      Mirf.getData((byte *)texteRecu);
      //Mirf.getData((byte *)&texteRecu);

     // Serial.println(texteRecu);
 
    String Mac = texteRecu;
     Serial.println(data[0], DEC);

      if(data[0]!=NULL)
      {
        for(int a=0; a<7;a++)
       { 
          Serial.println("Donnee recu");
          tab[a]=data[a];
          Serial.println(data[0], DEC);
       }  
      }
    //  Mirf.send(data); // Et on le renvoi tel quelle (comme pour un ping rÈseau)
 
        }
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
        Serial.print("data received: ");
        Serial.println(number);

        if (number == 1){

            if (state == 0){
                digitalWrite(13, HIGH); // set the LED on
                state = 1;
            }
            else{
                digitalWrite(13, LOW); // set the LED off
                state = 0;
                }
         }
     }
}

// callback for sending data
void sendData(){
   // Wire.write(strMsg);
  //byte buffer[3];
  //buffer[0]=1;
  switch(number)
  {
  case 0:
  Wire.write(tab[0]);
  break;
  case 1:
  Wire.write(tab[1]);
  break;
/*  
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
}

