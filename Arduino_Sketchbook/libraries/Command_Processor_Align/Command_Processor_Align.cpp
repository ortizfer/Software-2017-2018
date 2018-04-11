#include <Command_Processor_Align.h>

#include <string.h>
#include <stdlib.h>
#include <Arduino.h>
#include <Razor_AHRS.h>
#include <avr/pgmspace.h>


#define HELP_BUFFER_SIZE 29
#define ENTER_ALIGN 2
#define EXIT_ALIGN 2
#define CONTROLLER_ALIGN 2


bool terminalOutput = false;
bool continuousOutput = true;
bool alignController = false;
bool clockwiseTurn = true;

bool outputImuMag = false;

float alignSetPoint = 0;
float alignGain = 0;
float alignBias = 29;

int threshFwEnter = ENTER_ALIGN;
int threshFwExit = EXIT_ALIGN;
int threshCont = CONTROLLER_ALIGN;


int moving = NOT_MOVING;
float timeForwards = 0;


char *firstItem;
char *secondItem;
char *thirdItem;
char *savePtr;

const char constHelp[] PROGMEM = "\n\r****************USER HELP GUIDE****************\n\rCommands: \n\r"
                "1. a - align controller commands\n\r"
                " Parameters:\n\r"
                "   s - assigns the set point\n\r"
                "     Sub-Parameters: \n\r"
                "	  0-9 | q,w,e,r,t,t - assigns the set point\n\r"
                "   g - sets the controller gain\n\r"
                "     Sub-Parameters: \n\r"
                "         0-9 - controller gain\n\r"
                "   m - Changes the set point to were you are\n\r"
                "   x - turns the controller off\n\r"
                "2. f - goes forward the amount you specify\n\r"
                "     Sub-Parameters: \n\r"
                "         0 - 9 sets the time to go forwards\n\r"
                "3. b - goes backwards the amount you specify\n\r"
                "     Sub-Parameters: \n\r"
                "         0 - 9 sets the time to go forwards\n\r"
                "3. u - prints information about the system\n\r"
                "4. k - prints actual align in feet\n\r"
                "5. l - prints align error\n\r"
                "6. p - prints indentification number\n\r"
                "5. x - turns the system off \n\r"
                "       - press s to start again\n\r"
                "6. h - help menu display\n\r"
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
		
		case 'a':
		switch(*(firstItem+1)){
			case 'n':
			alignController = true;
			break;
			case 's':
			alignSetPoint = atof(secondItem);
			 if(alignSetPoint > 360){
	            alignSetPoint -= 360;
	        }else if(alignSetPoint < 0){
	            alignSetPoint += 360;
	        }
			break;
			case 'm':
			razorRefreshValuesAnglesText();
			alignSetPoint = razorGetYaw();
			break;
			case 'd':
			clockwiseTurn = clockwiseTurn ? false : true;
			case 'g':
			alignGain = atof(secondItem);
			break;
			case 'b':
			alignBias = alignBias == 29 ? 14.5 : 29;
	   		break;
			case 'x':
			alignController = false;
			break;
			default:
			validCommand = false;
		}
		break;
		case 't':
		switch(*(firstItem+1)){
			case 'f':
			threshFwEnter = atoi(secondItem);
			break;
			case 'g':
			threshFwExit = atoi(secondItem);
			break;
			case 'h':
			threshCont = atoi(secondItem);
			break;
			default:
			validCommand = false;
		}
		break;
		case 'i':
		switch(*(firstItem+3)){
			case 'a':
			if(outputImuMag){
				outputImuMag = false;
				razorOuptutAnglesText();
			}
			
			break;
			case 'm':
			if(!outputImuMag){
				outputImuMag = false;
				razorOutputMagnetometer();
			}
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
		alignController = 0;
		break;
		case 'h':
		helpPrinter = constHelp;
		for (int i = HELP_BUFFER_SIZE; i != 0; --i){
			strncpy_P(help, (char*)pgm_read_word(helpPrinter), HELP_BUFFER_SIZE);
			Serial.println(help);
			helpPrinter += HELP_BUFFER_SIZE; 	
		}
		break;

		case 'f':
		if(!moving){
			moving = FORWARDS;
			timeForwards = atof(secondItem);
		}
		break;
		case 'b':
		if(!moving){
			moving = BACKWARDS;
			timeForwards = atof(secondItem);
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

bool getSlignController(){
	return alignController;
}

bool getOutputImuMag(){
	return outputImuMag;
}

bool getOutputMagnetometer(){
	return outputImuMag;
}

bool clockwise(){
	return clockwiseTurn;
}

bool getAlignController(){
	return alignController;
}

float getAlignSetPoint(){
	return alignSetPoint;
}
float getAlignGain(){
	return alignGain;
}
float getAlignBias(){
	return alignBias;
}

float getTimeForwards(){
	return timeForwards;
}

int getThreshFwExit(){
	return threshFwExit;
}

int getThreshFwEnter(){
	return threshFwEnter;
}

int getThreshCont(){
	return threshCont;
}
 
void setTerminalOutput(bool val){
	terminalOutput = val;
}

void setContinuousOutput(bool val){
	continuousOutput = val;
}

void setAlignController(bool val){
	alignController = val;
}

void setAlignSetPoint(float val){
	alignSetPoint = val;
}

void setAlignGain(float val){
	alignGain = val;
}

void setAlignBias(float val){
	alignBias = val;
}


int isMoving(){
	return moving;
}

void stopMoving(){
	moving = NOT_MOVING;
}