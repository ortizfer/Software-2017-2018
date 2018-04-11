#include <Command_Processor_Depth.h>

#include <string.h>
#include <stdlib.h>
#include <Arduino.h>
#include <Motors.h>  
#include <avr/pgmspace.h>

#define HELP_BUFFER_SIZE 29

bool terminalOutput;
bool continuousOutput;
bool depthController;

float depthSetPoint = 0;
float depthGain = 0;
float depthBias = 29;



char *firstItem;
char *secondItem;
char *thirdItem;
char *savePtr;

const char constHelp[] PROGMEM = "\n\r****************USER HELP GUIDE****************\n\rCommands: \n\r"
                "1. o - depth controller commands\n\r"
                " Parameters:\n\r"
                "   n - turns on controller\n\r"
                "   s - sets the set point\n\r"
                "		Sub parameters:\n\r"
                "			0-9 | q,w,e,r,t,t - assigns the set point\n\r"
                "   g - sets the controller gain\n\r"
                "     Sub-Parameters: \n\r"
                "         0-9 - controller gain\n\r"
                "   d - Changes the sub bias point\n\r"
                "       Sub-Parameters: \n\r"
                "         1 - sets the bias to 29 (default)\n\r"
                "         2 - sets the bias to 14.5 (sens error)\n\r"
                "   x - turns the controller off\n\r"
                "2. u - prints information about the system\n\r"
                "3. j - Enables continuous output of the system \n\r"
                "4.	k - Disables continuous output\n\r"
                "5. p - prints identification number\n\r"
                "6. x - turns the system off \n\r"
                "       - press s to start again\n\r"
                "7. h - help menu display\n\r"
                "***********************************************\n\r";

char help[HELP_BUFFER_SIZE];
char *helpPrinter;

const char *delim = " ";



bool verifyCommand(char *inputCommand){
 	//Serial.println(inputString);
	firstItem = strtok_r(inputCommand, delim, &savePtr);
	if(firstItem != NULL){ 
	  //Serial.print("First Token: ");Serial.println(firstItem);
	  secondItem = strtok_r(NULL, delim, &savePtr);
	  if(firstItem != NULL){
	    //Serial.print("Second Token: ");Serial.println(secondItem);
	    thirdItem = strtok_r(NULL, delim, &savePtr);
	    //if(firstItem != NULL){Serial.print("Third Token: ");Serial.println(thirdItem);Serial.print("Whats Left: ");Serial.println(savePtr);}
	  }
	}
	char validCommand = true;
	switch(*firstItem){
		
		case 'o':
		switch(*(firstItem+1)){
			case 'n':
			depthController = true;
			break;
			case 's':
			depthSetPoint = atof(secondItem);
			break;
			case 'g':
			depthGain = atof(secondItem);
			break;
			case 'd':
			if(depthBias == 29){
	        	depthBias = 14.5;
	   	 	}else{
	        	depthBias = 29;
	   		}
	   		break;
			case 'x':
			depthController = true;
			break;
			default:
			validCommand = false;
		}
		break;
		case 'u':
		terminalOutput = true;
		break;
		case 'j':
		continuousOutput = true;
		break;
		case 'k':
		continuousOutput = false;
		break;
		case 'x':
		setVerticalMotorSpeed(0);
		depthController = 0;
		break;
		case 'h':
		helpPrinter = constHelp;
		for (int i = HELP_BUFFER_SIZE; i != 0; --i){
			strncpy_P(help, (char*)pgm_read_word(helpPrinter), HELP_BUFFER_SIZE);
			Serial.println(help);
			helpPrinter += HELP_BUFFER_SIZE; 	
		}
		break;
		default:
		validCommand = false;
	}
	return validCommand;
}


bool getTerminalOutput(){
	return terminalOutput;
}

bool getContinuousOutput(){
	return continuousOutput;
}

bool getDepthController(){
	return depthController;
}

float getDepthSetPoint(){
	return depthSetPoint;
}
float getDepthGain(){
	return depthGain;
}
float getDepthBias(){
	return depthBias;
}

 
void setTerminalOutput(bool val){
	terminalOutput = val;
}

void setContinuousOutput(bool val){
	continuousOutput = val;
}

void setDepthController(bool val){
	depthController = val;
}

void setDepthSetPoint(float val){
	depthSetPoint = val;
}

void setDepthGain(float val){
	depthGain = val;
}

void setDepthBias(float val){
	depthBias = val;
}
