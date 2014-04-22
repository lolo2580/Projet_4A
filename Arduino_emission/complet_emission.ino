#include <SPI.h>
#include <Mirf.h>
#include <nRF24L01.h>
#include <MirfHardwareSpiDriver.h>
#include <SoftwareSerial.h>

void Initialisation_RF();
int envoyer_carac(char envoi);

void setup(){
  Serial.begin(9600);
  Initialisation_RF();
  
}

void loop(){
  
  int i=0, val=0, envoi_ok=0;
  unsigned char code[11]="";
  
  if(Serial.available()){ //si données valides
  
    do
    {
      if( Serial.available() > 0)
      {
        val = Serial.read();
        code[i] = val;
        //Serial.println(code[i]);
        i++;
      }
    }while(i<11);
    
    for(i=0 ; i<11; i++)
    {
     envoi_ok = envoyer_carac(code[i]);
     Serial.println(code[i]);
    }
    
    if (envoi_ok == 1)
    {
     //alliumer led ok 
    }
Serial.flush();    //Vide le buffer série
}  
}




void Initialisation_RF(){
  
   //Setup pins / SPI.
  Mirf.cePin = 7;
  Mirf.csnPin = 8;
  
  Mirf.spi = &MirfHardwareSpi;
  Mirf.init(); //initialisation MIRF
   
  Mirf.channel = 0;
  Mirf.payload = 1;  //sizeof(unsigned long); taille en octet du message
  Mirf.config();  //on valide la config
  
  Mirf.setTADDR((byte *)"nrf02");   // echanger les deux pour la réception
  Mirf.setRADDR((byte *)"nrf01");
}


int envoyer_carac(char envoi){
  
  int k=0, j=0, recept_OK=0; 
  char recu;
  
  Mirf.send((byte *)&envoi); //on envoie tempo
  while(Mirf.isSending()); //on attend tant que la donnée n'est pas partie

  while(!Mirf.dataReady()){
    if ( k > 10000 ) {
      return 0; //On sort de la boucle si on arrive pas a envoyer
    }
    for (j=0; j<1000; j++); //on perd du temps
  }
  
  Mirf.getData((byte *) &recu); //on récupère l'octet
  
  if(recu != 0) recept_OK=1;
 
  return recept_OK;
}




