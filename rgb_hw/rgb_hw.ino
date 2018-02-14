//Buttons on Pins 2,3,4
#define R 2
#define G 3
#define B 4

int pin[3];

void setup(){
  pinMode(R, INPUT_PULLUP);
  pinMode(G, INPUT_PULLUP);
  pinMode(B, INPUT_PULLUP);

  Serial.begin(9600);
}
void loop(){
  //wait for a character from Python
  while(Serial.available()==0);
  //read in the character
  char c = Serial.read();
  if(c == 'p'){
    pin[0] = digitalRead(R);
    pin[1] = digitalRead(G);
    pin[2] = digitalRead(B);
    
    for (int i = 0; i < 3; i++){
      if(pin[i] == 1){
        pin[i] = 0;
      } else {
        pin[i] = 1;
      }
    }
    Serial.print(pin[0]);
    Serial.print(',');
    Serial.print(pin[1]);
    Serial.print(',');
    Serial.print(pin[2]);
    Serial.print('\n');
  }
}
