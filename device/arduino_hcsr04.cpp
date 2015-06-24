#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int writeFile (char* string){
    FILE *fp = fopen("/tmp/arduino.txt", "w");
    if (fp != NULL) {
        fwrite(string, 1, sizeof(string), fp);
        fclose(fp);
        return EXIT_SUCCESS;
    } else {
        return EXIT_FAILURE;
    }
}
#define echoPin 7 // Echo Pin
#define trigPin 8 // Trigger Pin
#define LEDPin 13 // Onboard LED

#define UPDATE_RATE 250
//#define DEBUG

void blink(long duration){
    digitalWrite(LEDPin, LOW);
    delayMicroseconds(duration*100);
    digitalWrite(LEDPin, HIGH);
    delayMicroseconds(duration*100);
    digitalWrite(LEDPin, LOW);
}

void trigger(){
    digitalWrite(trigPin, LOW); 
    delayMicroseconds(2); 
    digitalWrite(trigPin, HIGH);
    delayMicroseconds(10); 
    digitalWrite(trigPin, LOW);

}

void setup() {
    #ifdef DEBUG
        Serial.begin (9600);
    #endif
    pinMode(trigPin, OUTPUT);
    pinMode(echoPin, INPUT);
    pinMode(LEDPin, OUTPUT);
}

long previousMillis = 0; 

void loop() {
    // Trigger
    trigger();

    // Echo
    long duration = pulseIn(echoPin, HIGH);
    blink(duration);

    // Output
    char ascii_buffer[8] = "";
    sprintf(ascii_buffer, "%d", duration);
    
    #ifdef DEBUG
        Serial.println(duration);
        delay(UPDATE_RATE);
    #else
        unsigned long currentMillis = millis();
        if(currentMillis - previousMillis > UPDATE_RATE) {
            previousMillis = currentMillis; 
            writeFile(ascii_buffer); // Write on FS
        }
    #endif
}
