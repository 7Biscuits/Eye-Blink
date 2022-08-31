#include <Servo.h>

Servo myservo;  

int pos = 0;  
int x;
const int buzzer = 6;

void setup() {
  myservo.attach(9);
  Serial.begin(115200);
  Serial.setTimeout(1);
  pinMode(buzzer, OUTPUT);
}

void loop() {
  while (!Serial.available());
  x = Serial.readString().toInt();
  if (!x) {
    tone(buzzer, 1000);
    for (pos = 0; pos <= 180; pos--) {
    myservo.write(pos);
    delay(15);
    }
  }
}
