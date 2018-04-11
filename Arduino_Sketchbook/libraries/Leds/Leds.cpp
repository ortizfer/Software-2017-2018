#include <LEDS.h>
#include <Arduino.h>


#define R_PIN 1
#define G_PIN 2
#define B_PIN 3

bool initialized = false;

void initializeLEDS(){
	pinMode(R_PIN, OUTPUT);
	pinMode(G_BIN, OUTPUT);
	pinMode(B_PIN, OUTPUT);
	initialized = true;
}



void setRGBColor(int R, int G, int B){
	
	if(initialized){
		analogWrite(R_PIN, R);
		analogWrite(G_PIN, G);
		analogWrite(B_PIN, B);
	}
}

