#ifndef _ROS_rumarino_package_ControllerSetup_h
#define _ROS_rumarino_package_ControllerSetup_h

#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"

namespace rumarino_package
{

  class ControllerSetup : public ros::Msg
  {
    public:
      typedef bool _controllerRunning_type;
      _controllerRunning_type controllerRunning;
      typedef float _controllerGain_type;
      _controllerGain_type controllerGain;
      typedef float _controllerBias_type;
      _controllerBias_type controllerBias;

    ControllerSetup():
      controllerRunning(0),
      controllerGain(0),
      controllerBias(0)
    {
    }

    virtual int serialize(unsigned char *outbuffer) const
    {
      int offset = 0;
      union {
        bool real;
        uint8_t base;
      } u_controllerRunning;
      u_controllerRunning.real = this->controllerRunning;
      *(outbuffer + offset + 0) = (u_controllerRunning.base >> (8 * 0)) & 0xFF;
      offset += sizeof(this->controllerRunning);
      union {
        float real;
        uint32_t base;
      } u_controllerGain;
      u_controllerGain.real = this->controllerGain;
      *(outbuffer + offset + 0) = (u_controllerGain.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_controllerGain.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_controllerGain.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_controllerGain.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->controllerGain);
      union {
        float real;
        uint32_t base;
      } u_controllerBias;
      u_controllerBias.real = this->controllerBias;
      *(outbuffer + offset + 0) = (u_controllerBias.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_controllerBias.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_controllerBias.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_controllerBias.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->controllerBias);
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer)
    {
      int offset = 0;
      union {
        bool real;
        uint8_t base;
      } u_controllerRunning;
      u_controllerRunning.base = 0;
      u_controllerRunning.base |= ((uint8_t) (*(inbuffer + offset + 0))) << (8 * 0);
      this->controllerRunning = u_controllerRunning.real;
      offset += sizeof(this->controllerRunning);
      union {
        float real;
        uint32_t base;
      } u_controllerGain;
      u_controllerGain.base = 0;
      u_controllerGain.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_controllerGain.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_controllerGain.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_controllerGain.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->controllerGain = u_controllerGain.real;
      offset += sizeof(this->controllerGain);
      union {
        float real;
        uint32_t base;
      } u_controllerBias;
      u_controllerBias.base = 0;
      u_controllerBias.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_controllerBias.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_controllerBias.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_controllerBias.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->controllerBias = u_controllerBias.real;
      offset += sizeof(this->controllerBias);
     return offset;
    }

    const char * getType(){ return "rumarino_package/ControllerSetup"; };
    const char * getMD5(){ return "29be7d2ddc5b278e77a74aad39d6a2ae"; };

  };

}
#endif