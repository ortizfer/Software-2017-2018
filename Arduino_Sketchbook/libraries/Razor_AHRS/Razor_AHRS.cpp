/*
 * RAZOR_AHRS.c
 *
 *  This code works to communicate the Sparkfun Razor AHRS[1] to the MSP430F5529 micro-controller[2].
 *  Contains the implementation to the API defined in the RAZOR_AHRS.h header.
 *  Code is based on the firnmware found at [3]
 *
 * Depends on Serial1_JMP.h
 *
 * Wiring diagram:
 * P3.3 -> TX@Razor
 * P3.4 -> RX@Razor
 *
 * USB -> PC COM PORT
 *
 *
 *  Created on: Feb 11, 2017
 *      Author: Jose A. Montes Perez
 *
 *  References:
 *  [1] https://www.sparkfun.com/products/retired/10736 - Sparkfun Razor IMU
 *  [2] http://www.ti.com/product/MSP430F5529 - MSP430F5529
 *  [3] https://github.com/Razor-AHRS/razor-9dof-ahrs
 *
 */


#include "Razor_AHRS.h"
#include <Arduino.h>

char outputMode;
char refreshMode;
float temp1, temp2, temp3;

//Variables that store the values for a particular
//angle
float yaw,pitch,roll;
//Variables were the values for the particular
//sensor are sotred
float acc_x,acc_y,acc_z;
float mag_x,mag_y,mag_z;
float gyr_x,gyr_y,gyr_z;


char inBuffer2[9];
char inBuffer[60];

float razorGetYaw(){
    return yaw;
}

float razorGetPitch(){
    return pitch;
}

float razorGetRoll(){
    return roll;
}


void razorSingleOutputSetup(){
    Serial1.begin(IMU_BAUD_RATE);
    delay(10);
    Serial1.print("#o0");
    refreshMode = 0;
}

void razorContinuousOutputSetup(){
    Serial1.begin(IMU_BAUD_RATE);
    Serial1.print("#o1");
    refreshMode = 1;
}

void razorOuptutAngles(){
    Serial1.print("#ob");
    outputMode = 1;
}

void razorOutputAccelerometer(){
    Serial1.print("#osca");
    outputMode = 2;
}


void razorOutputMagnetometer(){
    Serial1.print("#oscm");
    outputMode = 3;
}

void razorOutputGyroscope(){
    Serial1.print("#oscg");
    outputMode = 4;
}



void razorOuptutAnglesText(){
    Serial1.print("#ot");
    outputMode = 5;
}

void razorRefreshValuesBinary(){
    
    switch(outputMode){
    case 1:
        Serial1.print("#f");
        Serial1.readBytes(inBuffer, 12);
        temp1 = *(float *)(inBuffer);
        temp2 = *(float *)(inBuffer + 4);
        temp3 = *(float *)(inBuffer + 8);
        while ((temp1 > 180) || (temp1 < 0.0001 && temp1 > -0.0001)){
            Serial1.print("#o0#ob");
            delay(1);
            Serial1.print("#f");
            Serial1.readBytes(inBuffer, 12);
            Serial1.print("#f");
            Serial1.readBytes(inBuffer, 12);
            temp1 = *(float *)(inBuffer);
            temp2 = *(float *)(inBuffer + 4);
            temp3 = *(float *)(inBuffer + 8);
        }
        yaw = temp1;
        pitch = temp2;
        roll = temp3;
        break;
    case 2: 
        Serial1.print("#f");
        Serial1.readBytes(inBuffer, 12);
        acc_x = *(float *) (inBuffer);
        acc_y = *(float *) (inBuffer + 4);
        acc_z = *(float *) (inBuffer + 8);
        break;
    case 3:
        Serial1.print("#f");
        Serial1.readBytes(inBuffer, 12);
        mag_x = *(float *) (inBuffer + 12);
        mag_y = *(float *) (inBuffer + 16);
        mag_z = *(float *) (inBuffer + 20);
        break;
    case 4:
        Serial1.print("#f");
        Serial1.readBytes(inBuffer, 12);
        gyr_x = *(float *) (inBuffer + 24);
        gyr_y = *(float *) (inBuffer + 28);
        gyr_z = *(float *) (inBuffer + 32);
        break;
    default: break;
    }
}

void razorRefreshValuesAnglesText(){

    if(outputMode == 5){
        Serial1.print("#o0");
        delay(10);
        Serial1.print("#f");
        Serial1.readBytes(inBuffer2, 9);

        int i;
        for (i = 0; i < 8; i++){
            if(inBuffer2[i] == ','){
                inBuffer2[i] = '\n';
                break;
            }
        }
        yaw = atof(inBuffer2);

    }else if(outputMode == 3){
        Serial1.print("#f");
        Serial1.readBytesUntil('\n', inBuffer, IMU_BUFFER);
        Serial1.println(inBuffer);
    }
}



