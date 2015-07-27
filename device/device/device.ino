//#define DEBUG
#define EDISON

#ifdef EDISON
    #define flowmeterPin 12
    #define InterruptADDR 12
#else
    #define flowmeterPin 3
    #define InterruptADDR 1
 #endif

#define echoPin 7 // Echo Pin
#define trigPin 8 // Trigger Pin
#define LEDPin 13 // Onboard LED

#define UPDATE_RATE 250

#include "device_io.h"

// HCSR04 trigger pulse
void trigger(){
    digitalWrite(trigPin, LOW);
    delayMicroseconds(2);
    digitalWrite(trigPin, HIGH);
    delayMicroseconds(10);
    digitalWrite(trigPin, LOW);
}

// YFS201 Interrupt function
volatile int  flow_frequency;  // Measures flow meter pulses
void flow (){
    flow_frequency++;
}

void setup() {
  
    // Serial.begin (9600);
    #ifdef DEBUG
        Serial.begin (9600);
    #endif
    
    pinMode(trigPin, OUTPUT);
    pinMode(echoPin, INPUT);
    pinMode(LEDPin, OUTPUT);
    pinMode(flowmeterPin, INPUT);
    
    attachInterrupt(InterruptADDR, flow, RISING); // Setup Interrupt
    
    #ifdef ARDUINO
       // IFDEF is not working
       //sei(); // Enable interrupts
    #endif
} 

unsigned long sensorMillis = 0;
unsigned long outputMillis = 0;
unsigned int duration = 0;

float total_liters = 0;
float distance = 0;

void loop() {
    
    unsigned long currentMillis = millis();
    // Every second, calculate and print litres/hour
    if(currentMillis - sensorMillis > 1000) {
        sensorMillis = currentMillis;
        /*
            YFS201
            Pulse frequency (Hz) = 7.5Q, Q is flow rate in L/min. (Results in +/- 3% range)
            (Pulse frequency x 60 min) / 7.5Q = flow rate in L/hour
        */
        float liters = ((float) flow_frequency  / (7.5 * 60.0));  
        total_liters += liters;
        flow_frequency = 0; // Reset Counter (flow function)
    }

    /*
        HCSR04
        constant sound speed: us per cm
        k = 29.104
    */
    trigger();
    duration = pulseIn(echoPin, HIGH);
    distance = ((float) duration / 29.104);

    delay(UPDATE_RATE);

    #ifdef DEBUG
        Serial.print("HCSR04 pulse duration:");
        Serial.println(duration);

        Serial.print("YFS201 liters per seconde:");
        Serial.println(liters);
    #else
        char ascii_buffer[256] = "";
        sprintf(ascii_buffer, "{\n    \"echo\": %f,\n    \"total_liters\": %f\n}\n", distance, total_liters);
        // Serial.println(ascii_buffer);
        writeFile(ascii_buffer); // Write on FS
    #endif
}
