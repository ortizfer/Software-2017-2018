#ifndef _ROS_rumarino_package_HorizontalMotors_h
#define _ROS_rumarino_package_HorizontalMotors_h

#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"

namespace rumarino_package
{

  class HorizontalMotors : public ros::Msg
  {
    public:
      typedef int32_t _leftMotor_type;
      _leftMotor_type leftMotor;
      typedef int32_t _rightMotor_type;
      _rightMotor_type rightMotor;

    HorizontalMotors():
      leftMotor(0),
      rightMotor(0)
    {
    }

    virtual int serialize(unsigned char *outbuffer) const
    {
      int offset = 0;
      union {
        int32_t real;
        uint32_t base;
      } u_leftMotor;
      u_leftMotor.real = this->leftMotor;
      *(outbuffer + offset + 0) = (u_leftMotor.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_leftMotor.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_leftMotor.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_leftMotor.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->leftMotor);
      union {
        int32_t real;
        uint32_t base;
      } u_rightMotor;
      u_rightMotor.real = this->rightMotor;
      *(outbuffer + offset + 0) = (u_rightMotor.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_rightMotor.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_rightMotor.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_rightMotor.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->rightMotor);
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer)
    {
      int offset = 0;
      union {
        int32_t real;
        uint32_t base;
      } u_leftMotor;
      u_leftMotor.base = 0;
      u_leftMotor.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_leftMotor.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_leftMotor.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_leftMotor.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->leftMotor = u_leftMotor.real;
      offset += sizeof(this->leftMotor);
      union {
        int32_t real;
        uint32_t base;
      } u_rightMotor;
      u_rightMotor.base = 0;
      u_rightMotor.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_rightMotor.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_rightMotor.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_rightMotor.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->rightMotor = u_rightMotor.real;
      offset += sizeof(this->rightMotor);
     return offset;
    }

    const char * getType(){ return "rumarino_package/HorizontalMotors"; };
    const char * getMD5(){ return "40c59515e060d941dde4c816f719e5bb"; };

  };

}
#endif