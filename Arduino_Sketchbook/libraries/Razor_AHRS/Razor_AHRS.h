/*
 * RAZOR_AHRS.h
 *
 *  Created on: Feb 11, 2017
 *      Author: RathK
 */

#ifndef RAZOR_AHRS_H_
#define RAZOR_AHRS_H_

#include <Arduino.h>

#define IMU_BAUD_RATE 9600      //Baud Rate for communicating with the sensor
#define IMU_SAMPLE_RATE 60      //Suggested sample rate in milliseconds
#define IMU_BUFFER 60           //Malloc buffer size with slight overshoot


float razorGetYaw();
float razorGetPitch();
float razorGetRoll();

void razorSingleOutputSetup();
void razorContinuousOutputSetup();

void razorOuptutAngles();
void razorOuptutAnglesText();
void razorOutputAccelerometer();
void razorOutputGyroscope();
void razorOutputMagnetometer();

void razorRefreshValuesBinary();
void razorRefreshValuesAnglesText();


#endif /* RAZOR_AHRS_H_ */
