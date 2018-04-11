#ifndef _ROS_deepfind_package_motor_command_h
#define _ROS_deepfind_package_motor_command_h

#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"

namespace deepfind_package
{

  class motor_command : public ros::Msg
  {
    public:
      typedef int32_t _leftMotorPower_type;
      _leftMotorPower_type leftMotorPower;
      typedef int32_t _rightMotorPower_type;
      _rightMotorPower_type rightMotorPower;
      typedef int32_t _leftMotorDirection_type;
      _leftMotorDirection_type leftMotorDirection;
      typedef int32_t _rightMotorDirection_type;
      _rightMotorDirection_type rightMotorDirection;

    motor_command():
      leftMotorPower(0),
      rightMotorPower(0),
      leftMotorDirection(0),
      rightMotorDirection(0)
    {
    }

    virtual int serialize(unsigned char *outbuffer) const
    {
      int offset = 0;
      union {
        int32_t real;
        uint32_t base;
      } u_leftMotorPower;
      u_leftMotorPower.real = this->leftMotorPower;
      *(outbuffer + offset + 0) = (u_leftMotorPower.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_leftMotorPower.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_leftMotorPower.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_leftMotorPower.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->leftMotorPower);
      union {
        int32_t real;
        uint32_t base;
      } u_rightMotorPower;
      u_rightMotorPower.real = this->rightMotorPower;
      *(outbuffer + offset + 0) = (u_rightMotorPower.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_rightMotorPower.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_rightMotorPower.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_rightMotorPower.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->rightMotorPower);
      union {
        int32_t real;
        uint32_t base;
      } u_leftMotorDirection;
      u_leftMotorDirection.real = this->leftMotorDirection;
      *(outbuffer + offset + 0) = (u_leftMotorDirection.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_leftMotorDirection.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_leftMotorDirection.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_leftMotorDirection.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->leftMotorDirection);
      union {
        int32_t real;
        uint32_t base;
      } u_rightMotorDirection;
      u_rightMotorDirection.real = this->rightMotorDirection;
      *(outbuffer + offset + 0) = (u_rightMotorDirection.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_rightMotorDirection.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_rightMotorDirection.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_rightMotorDirection.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->rightMotorDirection);
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer)
    {
      int offset = 0;
      union {
        int32_t real;
        uint32_t base;
      } u_leftMotorPower;
      u_leftMotorPower.base = 0;
      u_leftMotorPower.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_leftMotorPower.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_leftMotorPower.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_leftMotorPower.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->leftMotorPower = u_leftMotorPower.real;
      offset += sizeof(this->leftMotorPower);
      union {
        int32_t real;
        uint32_t base;
      } u_rightMotorPower;
      u_rightMotorPower.base = 0;
      u_rightMotorPower.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_rightMotorPower.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_rightMotorPower.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_rightMotorPower.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->rightMotorPower = u_rightMotorPower.real;
      offset += sizeof(this->rightMotorPower);
      union {
        int32_t real;
        uint32_t base;
      } u_leftMotorDirection;
      u_leftMotorDirection.base = 0;
      u_leftMotorDirection.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_leftMotorDirection.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_leftMotorDirection.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_leftMotorDirection.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->leftMotorDirection = u_leftMotorDirection.real;
      offset += sizeof(this->leftMotorDirection);
      union {
        int32_t real;
        uint32_t base;
      } u_rightMotorDirection;
      u_rightMotorDirection.base = 0;
      u_rightMotorDirection.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_rightMotorDirection.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_rightMotorDirection.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_rightMotorDirection.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->rightMotorDirection = u_rightMotorDirection.real;
      offset += sizeof(this->rightMotorDirection);
     return offset;
    }

    const char * getType(){ return "deepfind_package/motor_command"; };
    const char * getMD5(){ return "382ef61c60c451a76309a7978532675c"; };

  };

}
#endif