#include <Command_Processor_Align.h>
#include <Motors.h>
#include <Razor_AHRS.h>

#define MOTOR_CAP 50
#define FORWARDS_SPEED 40
#define INPUT_BUFFER_LENGTH 200


//Serial Command Variables
char inputString[INPUT_BUFFER_LENGTH];
boolean stringComplete = false;

//Controller Variables
float yawActual;
float alignError;
float alignErrorAbs;
int motorSpeed;

//Status that controls printing system info
bool prints;


void setup() {
  Serial.begin(9600);                                                                           //Begin Serial to computer
  while (! Serial);                                                                             //Verify it is working
  initializeHorizontalMotors();
  razorSingleOutputSetup();
  razorOuptutAnglesText();
  Serial.println("Initialized");                                          
}


void loop(){


  //New Command has arrived
  //Process it
  if(stringComplete){  
    if(verifyCommand(inputString)){
      Serial.println("Entered a valid Command");
    }
    else{
      Serial.println("Entered an invalid Command");
    } 
    stringComplete = false;
    wipeString();
  }

  prints = getTerminalOutput() | getContinuousOutput();


  if(getOutputMagnetometer()){
   razorRefreshValuesAnglesText();
  }else if(isMoving()){


    
    unsigned long currentTime;
    unsigned long timeout;
    int direction = isMoving();
    float opPoint, currPoint, error, error_abss;

    
    //Get new values from IMU to set current point;
    razorRefreshValuesAnglesText();
    opPoint = razorGetYaw();
    if(opPoint < 0){
        opPoint +=  360;
    }
    
    //Send Speed to Motors
    setHorizontalMotorSpeed(direction*FORWARDS_SPEED, direction*FORWARDS_SPEED);
    
    
    //Start counting
    currentTime = millis();
    timeout = getTimeForwards()*1000+currentTime;

    int align_sat = 0;

    while(currentTime < timeout){
        setHorizontalMotorSpeed(direction*FORWARDS_SPEED, direction*FORWARDS_SPEED);
        delay(10);
        
        razorRefreshValuesAnglesText();
        currPoint = razorGetYaw();
        if(currPoint < 0){
            currPoint +=  360;
        }
        
        error = opPoint - currPoint;
        if(abs(error) > getThreshFwEnter()){
            align_sat = 1;
        }

        while(align_sat && currentTime < timeout){
     
            razorRefreshValuesAnglesText();
            currPoint = razorGetYaw();
            if(currPoint < 0){
                currPoint +=  360;
            }
            
            error = opPoint - currPoint;
            error_abss = abs(error);
            if(error > 0){
                if(error>180){
                    error = error - 360;
                }
            }else{
                if(error_abss > 180){
                    error = 360 - error_abss;
                }
            }
            
            if (error <= getThreshFwExit() && error >= -1*getThreshFwExit()){
                error = 0;
                align_sat = 0;
                break;
            }
            motorSpeed = error*getAlignGain();
            if(motorSpeed > MOTOR_CAP){
              motorSpeed = MOTOR_CAP;
            }
            if(clockwise()){
              if(clockwise()){
                setHorizontalMotorSpeed(direction*motorSpeed, direction*-1*motorSpeed);
              }else{
                setHorizontalMotorSpeed(direction*-1*motorSpeed, direction*motorSpeed);
              }
            }

            if(getContinuousOutput()){
                if(isMoving() == FORWARDS){
                  Serial.print("Forwards"); 
                }else{
                  Serial.print("Backwards");
                }
                Serial.print(" Forward set point: ");   Serial.print(opPoint);
                Serial.print(" F  Current angle: ");    Serial.println(currPoint);
            }
        }
    }
    setHorizontalMotorSpeed(0,0);

    
    
    
    
    
  }else if (getAlignController()){
    razorRefreshValuesAnglesText();
    yawActual = razorGetYaw();
  
    if(yawActual < 0){
      yawActual +=  360;
    }
  
    alignError = (getAlignSetPoint() - yawActual);
    alignErrorAbs = abs(alignError);
    if(alignError > 0){
      if(alignError > 180){
        alignError = alignError - 360;
      }
    }else{
      if(alignErrorAbs > 180){
        alignError = 360 - alignErrorAbs;
      }
    }
    if(alignError >= getThreshCont() && alignError <= -1*getThreshCont()){
      alignError = 0;
    }
  
    motorSpeed = alignError*getAlignGain();
    
    if(motorSpeed > MOTOR_CAP){
      motorSpeed = MOTOR_CAP;
    }      
    if(clockwise()){
      setHorizontalMotorSpeed(motorSpeed, -1*motorSpeed);
    }else{
      setHorizontalMotorSpeed(-1*motorSpeed, motorSpeed);
    }
  }else{
    setHorizontalMotorSpeed(0,0);
  }

  
  if(prints){
      Serial.print(" align set point: ");   Serial.print(getAlignSetPoint());
      Serial.print("  Current angle: ");    Serial.print(yawActual);
      Serial.print(" motor Speed:");        Serial.print(motorSpeed);
      Serial.print("  Clockwise: ");        Serial.println(clockwise());
      setTerminalOutput(false);
  }
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//Auxiliary functions

void serialEvent() {
  if(Serial.available()){
    int nullTerminator = 0;
    nullTerminator = Serial.readBytes(inputString, INPUT_BUFFER_LENGTH-1);
    inputString[nullTerminator] = '\0';
    stringComplete = true;
  }
}


void wipeString(){
  for(int i = 0; i < INPUT_BUFFER_LENGTH; i++){
    inputString[i] = '\0';
  }
}
