#ifndef Motors_h
#define Motors_h

#include <Servo.h>

void initializeVerticalMotors(); 
void setVerticalMotorSpeed(int speed);

//void initializeHorizontalMotors();
void initializeHorizontalMotors(char *old);
void setHorizontalMotorSpeed(int left_motor, int right_motor);
void setHorizontalMotorSpeed(int motor1, int motor2, int motor3, int motor4);

#endif
