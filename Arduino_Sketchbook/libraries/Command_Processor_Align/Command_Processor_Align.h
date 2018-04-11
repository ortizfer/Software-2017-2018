#ifndef Command_Processor_align_h
#define Command_Processor_align_h

#include <string.h>
#include <stdlib.h>


#define FORWARDS 1
#define BACKWARDS -1
#define NOT_MOVING 0

bool verifyCommand(char *inputCommand);
bool getTerminalOutput();
bool getContinuousOutput();
bool getAlignController();
bool getOutputMagnetometer();
bool clockwise();


float getAlignSetPoint();
float getAlignGain();
float getAlignBias();
float getTimeForwards();

int getThreshFwEnter();
int getThreshFwExit();
int getThreshCont();


void setTerminalOutput(bool val);
void setContinuousOutput(bool val);
void setAlignController(bool val);

void setAlignSetPoint(float val);
void setAlignGain(float val);
void setAlignBias(float val);

int isMoving();
void StopMoving();

#endif
