#include <Servo.h>
#include <U8x8lib.h>

Servo myservo;
String InBytes;
int pos = 0;  
int x;
const int buzzer = 5;
const int ledPin = 4;
U8X8_SSD1306_128X64_NONAME_HW_I2C u8x8(U8X8_PIN_NONE);

void setup() {
  myservo.attach(9);
  Serial.begin(115200);
  Serial.setTimeout(1);
  pinMode(buzzer, OUTPUT);
  pinMode(ledPin, OUTPUT);
  u8x8.begin();
  u8x8.setFlipMode(1);
}

void loop() {
  if (Serial.available() > 0) {
    InBytes = Serial.readStringUntil('\n');
    if (InBytes == "onn") {
      delay(5000);
      tone(buzzer, 1000);
      digitalWrite(ledPin, HIGH);
      u8x8.clear();
      u8x8.setFont(u8x8_font_chroma48medium8_r);
      u8x8.setCursor(0, 0);
      u8x8.print("WARNING:");
      delay(100);
    }
    if (InBytes == "off") {
      delay(100);
      noTone(buzzer);
      digitalWrite(ledPin, LOW);
      u8x8.clear();
      u8x8.setFont(u8x8_font_chroma48medium8_r);
      u8x8.setCursor(0, 0);
      u8x8.print("CHILL");

      for (pos = 0; pos <= 180; pos += 1) { 
        myservo.write(pos);
        delay(15); 
      }
      for (pos = 180; pos >= 0; pos -= 1) { 
        myservo.write(pos); 
        delay(15); 
      }
      delay(100);
    }
  }
}
