#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <Arduino.h>

int writeFile (char* string){
    FILE *fp = fopen("/tmp/arduino.json", "w");
    if (fp != NULL) {
        fwrite(string, strlen(string), sizeof(char), fp);
        fclose(fp);
        return EXIT_SUCCESS;
    } else {
        return EXIT_FAILURE;
    }
}
void printDouble(double val, unsigned int precision){
    /*
       prints val with number of decimal places determine by precision
       NOTE: precision is 1 followed by the number of zeros for the desired number of decimial places
       example: printDouble( 3.1415, 100); // prints 3.14 (two decimal places)
    */
    Serial.print (int(val));  //prints the int part
    Serial.print("."); // print the decimal point
    unsigned int frac;
    if(val >= 0)
        frac = (val - int(val)) * precision;
    else
        frac = (int(val)- val ) * precision;
    Serial.println(frac,DEC);
}

void blink(long duration){
    digitalWrite(LEDPin, LOW);
    delayMicroseconds(duration*100);
    digitalWrite(LEDPin, HIGH);
    delayMicroseconds(duration*100);
    digitalWrite(LEDPin, LOW);
}
