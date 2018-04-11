#include <Motors.h>
#include <Servo.h>
#include <string.h>

#define VERTICAL_PIN_0 2
#define VERTICAL_PIN_1 3
#define VERTICAL_PIN_2 4
#define VERTICAL_PIN_3 5
#define HORIZONTAL_PIN_0 6
#define HORIZONTAL_PIN_1 7
#define HORIZONTAL_PIN_2 8
#define HORIZONTAL_PIN_3 9

#define PWM_RANGE 4
#define PWM_NEUTRAL 1500

Servo vertSpeedController[4];
Servo horizontalSpeedController[4];

bool verticalInitialized = false;
bool horizontalInitialized = false;
bool oldDesign = true;



int speedToMicroseconds(int speed){
  if(speed >= -100 && speed <= 100){
    return PWM_RANGE*speed + PWM_NEUTRAL;
  }
  else{
    return 0;
  }
}


void initializeVerticalMotors(){
	vertSpeedController[0].attach(VERTICAL_PIN_0);
	vertSpeedController[1].attach(VERTICAL_PIN_1);
	vertSpeedController[2].attach(VERTICAL_PIN_2);
	vertSpeedController[3].attach(VERTICAL_PIN_3);
	verticalInitialized = true;
}


void setVerticalMotorSpeed(int speed){
	if(verticalInitialized){
		int microseconds = speedToMicroseconds(speed);
		vertSpeedController[0].writeMicroseconds(microseconds);
		vertSpeedController[1].writeMicroseconds(microseconds);
		vertSpeedController[2].writeMicroseconds(microseconds);
		vertSpeedController[3].writeMicroseconds(microseconds);
	}
}


void initializeHorizontalMotors(char *old){
	if(strcmp(old, "old") == 0){
		oldDesign = true;
		
	}else{
		oldDesign = false;
	}
	horizontalSpeedController[0].attach(HORIZONTAL_PIN_0);
	horizontalSpeedController[1].attach(HORIZONTAL_PIN_1);
	if(!oldDesign){
		horizontalSpeedController[2].attach(HORIZONTAL_PIN_2);
		horizontalSpeedController[3].attach(HORIZONTAL_PIN_3);
	}
	horizontalInitialized = true;
}	
	
void setHorizontalMotorSpeed(int left_motor, int right_motor){
	if(horizontalInitialized){
		horizontalSpeedController[0].writeMicroseconds(speedToMicroseconds(left_motor));
		horizontalSpeedController[1].writeMicroseconds(speedToMicroseconds(right_motor));
	}
}
void setHorizontalMotorSpeed(int motor1, int motor2, int motor3, int motor4){
	if(horizontalInitialized){
		horizontalSpeedController[0].writeMicroseconds(speedToMicroseconds(motor1));
		horizontalSpeedController[1].writeMicroseconds(speedToMicroseconds(motor2));
		if(!oldDesign){
			horizontalSpeedController[2].writeMicroseconds(speedToMicroseconds(motor3));
			horizontalSpeedController[3].writeMicroseconds(speedToMicroseconds(motor4));
		}
		
	}
}