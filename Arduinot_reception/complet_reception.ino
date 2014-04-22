
#include <SPI.h>
#include <Mirf.h>
#include <nRF24L01.h>
#include <MirfHardwareSpiDriver.h>


void Initialisation_RF();

void setup(){
  Serial.begin(9600);
  Initialisation_RF();
}  
  
  void loop(){
  char data; // Tableau de byte qui va stocker le message recu
   char ok =1;
   
  if(!Mirf.isSending() && Mirf.dataReady()){ // Si un message a été recu et qu'un autre n'est pas en cours d'emission
    Mirf.getData((byte *) &data); // on récupére le méssage
    Serial.println(data);
    Mirf.send((byte *)&ok);
  }
}
  





void Initialisation_RF(){
  
   //Setup pins / SPI.
  Mirf.cePin = 9;
  Mirf.csnPin = 8;
  
  Mirf.spi = &MirfHardwareSpi;
  Mirf.init(); //initialisation MIRF
   
  Mirf.channel = 0;
  Mirf.payload = 1;  //sizeof(unsigned long); taille en octet du message
  Mirf.config();  //on valide la config
  
  Mirf.setTADDR((byte *)"nrf01");   // echanger les deux pour la réception
  Mirf.setRADDR((byte *)"nrf02");
}
