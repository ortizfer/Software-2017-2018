#ifndef Command_Processor_Depth_h
#define Command_Processor_Depth_h

#include <string.h>
#include <stdlib.h>


bool verifyCommand(char *inputCommand);
bool getTerminalOutput();
bool getContinuousOutput();
bool getDepthController();

float getDepthSetPoint();
float getDepthGain();
float getDepthBias();

 
void setTerminalOutput(bool val);
void setContinuousOutput(bool val);
void setDepthController(bool val);

void setDepthSetPoint(float val);
void setDepthGain(float val);
void setDepthBias(float val);

#endif
