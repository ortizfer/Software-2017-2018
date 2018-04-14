#include <Arduino.h>
#include <ros.h>
#include <geometry_msgs/Twist.h>
#include <std_msgs/Int32.h>
#include <std_msgs/Float32.h>
#include <rumarino_package/HorizontalMotors.h>
#include <Motors.h>
#include <Wire.h>
#include <MS5837.h>


std_msgs::Float32 depth;
MS5837 pressureSensor;


// Callback function for left motors
void setHorizontalMotors(const rumarino_package::HorizontalMotors&  motorIntensity)
{
   setHorizontalMotorSpeed(motorIntensity.rightMotor, motorIntensity.leftMotor);
}

// Callback function for simultaneous usage of motors
void setVerticalMotors(const std_msgs::Int32& motorIntensity)
{
    setVerticalMotorSpeed(motorIntensity.data);
}


ros::NodeHandle nh;

// Creates all the ROS subscriber objects 
ros::Subscriber<std_msgs::Int32> subVerticalMotors("vertical_motors", setVerticalMotors);
ros::Subscriber<std_msgs::Int32> subHorizontalMotors("horizontal_motors", setHorizontalMotors);

// Create the pressure sensor publisher 
ros::Publisher pubToPressureSensor("depth_current", &depth);


void setup() {
  // Initializes the node and preparehoris for publishing and subscribing.
  nh.initNode();
  nh.advertise(pubToPressureSensor);
  nh.subscribe(subVerticalMotors);
  nh.subscribe(subHorizontalMotors);

  // Initializes all the motors
  initializeVerticalMotors();
  initializeHorizontalMotors("old");

  // Initializes wire (protocol to run)
  Wire.begin(); 

  // If pressure sensor does not initialize, throw error
  while(!pressureSensor.init())
  {
      nh.logerror("Pressure sensor cannot initialize.");
  }
}

void loop() 
{
  pressureSensor.read();

  depth.data = pressureSensor.depth()/(3.3);

  pubToPressureSensor.publish(&depth);
  
  nh.spinOnce();
}
