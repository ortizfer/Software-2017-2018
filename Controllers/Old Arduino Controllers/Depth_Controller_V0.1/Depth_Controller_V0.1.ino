#include <MS5837.h>
#include <Command_Processor_Depth.h>
#include <Motors.h>
#include <Wire.h>

#define FEET_TO_PWM 6.25
#define FEET_TO_METERS 3.281
#define MOTOR_CAP 50
#define INPUT_BUFFER_LENGTH 200


//Serial Command Variables
char inputString[INPUT_BUFFER_LENGTH];
boolean stringComplete = false;

//Pressure Sensor
MS5837 pressureSensor;

//Controller Variables
float sensorPressure;
float depthActual;
float depthError;
int motorSpeed;

//Status that controls printing system info
bool prints;


void setup() {
  Serial.begin(9600);                                                                           //Begin Serial to computer
  while (! Serial);                                                                             //Verify it is working
  initializeVerticalMotors();
  Serial.println("Initialized");                                          

  Wire.begin();                                                                                 //Start I2C Communication

  // Initialize pressure sensor
  // Returns true if initialization was successful
  // We can't continue with the rest of the program unless we can initialize the sensor
  while (!pressureSensor.init()) {
    Serial.println("Init failed!");
    Serial.println("Are SDA/SCL connected correctly?");
    Serial.println("Blue Robotics Bar30: White=SDA, Green=SCL");
    Serial.println("\n\n\n");
    delay(5000);
  }
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
  
  if(getDepthController()){
      pressureSensor.read(); 
   
      //depthActual = pressureSensor.depth()/3.3;

      depthActual = pressureSensor.depth()*3.28;

      depthError = (getDepthSetPoint() - depthActual)*FEET_TO_METERS;      //calculate error

      motorSpeed = getDepthGain()*depthError;

      if(motorSpeed > MOTOR_CAP)
          motorSpeed = MOTOR_CAP;
      if(motorSpeed < -1*MOTOR_CAP)
          motorSpeed = -1*MOTOR_CAP;

      setVerticalMotorSpeed(motorSpeed);
      if(!prints){
         delay(10);
      }
  }
  else{
    setVerticalMotorSpeed(0);
  }


  if(prints){
      Serial.print("  pressurre: ");      Serial.print(sensorPressure);
      Serial.print(" depth set point: "); Serial.print(getDepthSetPoint());
      Serial.print("  depth: ");          Serial.print(depthActual);
      Serial.print("  error: ");          Serial.print(depthError);
      Serial.print("  motors: ");         Serial.println(motorSpeed);
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
