#include <Arduino.h>
#include <ros.h>
#include <geometry_msgs/Twist.h>
#include <std_msgs/Int32.h>
#include <std_msgs/Float32.h>
#include <std_msgs/Int32MultiArray.h>
#include <Motors.h>
#include <Wire.h>
#include <MS5837.h>

//int leftMotor = 0; 
//int rightMotor = 0;
std_msgs::Float32 depth;
//MS5837 pressureSensor;

// Callback function for left motors

/*void setLeftMotors(const std_msgs::Int32&  motorIntensity)
{
   leftMotor = motorIntensity.data;
   setHorizontalMotorSpeed(motorIntensity.data, rightMotor);
}

// Callback function for right motors
void setRightMotors(const std_msgs::Int32& motorIntensity)
{ 
    rightMotor = motorIntensity.data;
    setHorizontalMotorSpeed(leftMotor, motorIntensity.data);
}

*/

// Callback function for simultaneous usage of vertical motors
void setVerticalMotors(const std_msgs::Int32& motorIntensity)
{
    setVerticalMotorSpeed(motorIntensity.data);
}

// Callback function for simultaneous usage of horizontal motors
void setHorizontalMotors(const std_msgs::Int32MultiArray& message)
{
    setHorizontalMotorSpeed(message.data[0], message.data[1]);
}


ros::NodeHandle nh;

// Creates all the ROS subscriber objects
ros::Subscriber<std_msgs::Int32MultiArray> subHorizontalMotors("horizontal_motors", setHorizontalMotors);
ros::Subscriber<std_msgs::Int32> subVerticalMotors("vertical_motors", setVerticalMotors);
//ros::Subscriber<std_msgs::Int32> subLeftMotors("left_motor", setLeftMotors);
//ros::Subscriber<std_msgs::Int32> subRightMotors("right_motor", setRightMotors);

// Create the pressure sensor publisher 
//ros::Publisher pubToPressureSensor("pressure_sensor", &depth);


void setup() {
  // Initializes the node and prepares for publishing and subscribing.
  nh.initNode();
 // nh.advertise(pubToPressureSensor);
  nh.subscribe(subVerticalMotors);
  nh.subscribe(subHorizontalMotors);
  //nh.subscribe(subLeftMotors);
 // nh.subscribe(subRightMotors);

  // Initializes all the motors
  initializeVerticalMotors();
  initializeHorizontalMotors("old");

/*
  // Initializes wire (protocol to run)
  Wire.begin(); 

  // If pressure sensor does not initialize, throw error
  while(!pressureSensor.init())
  {
      nh.logerror("Pressure sensor cannot initialize.");
  }

*/
}

void loop() 
{
  /* pressureSensor.read();

  depth.data = pressureSensor.depth()/(3.3);

  pubToPressureSensor.publish(&depth); */
  
  nh.spinOnce();
}
