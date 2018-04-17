#ifndef _ROS_rumarino_package_ForwardsCommand_h
#define _ROS_rumarino_package_ForwardsCommand_h

#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"

namespace rumarino_package
{

  class ForwardsCommand : public ros::Msg
  {
    public:
      typedef int32_t _forwardsIntensity_type;
      _forwardsIntensity_type forwardsIntensity;
      typedef bool _movingForwards_type;
      _movingForwards_type movingForwards;

    ForwardsCommand():
      forwardsIntensity(0),
      movingForwards(0)
    {
    }

    virtual int serialize(unsigned char *outbuffer) const
    {
      int offset = 0;
      union {
        int32_t real;
        uint32_t base;
      } u_forwardsIntensity;
      u_forwardsIntensity.real = this->forwardsIntensity;
      *(outbuffer + offset + 0) = (u_forwardsIntensity.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_forwardsIntensity.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_forwardsIntensity.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_forwardsIntensity.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->forwardsIntensity);
      union {
        bool real;
        uint8_t base;
      } u_movingForwards;
      u_movingForwards.real = this->movingForwards;
      *(outbuffer + offset + 0) = (u_movingForwards.base >> (8 * 0)) & 0xFF;
      offset += sizeof(this->movingForwards);
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer)
    {
      int offset = 0;
      union {
        int32_t real;
        uint32_t base;
      } u_forwardsIntensity;
      u_forwardsIntensity.base = 0;
      u_forwardsIntensity.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_forwardsIntensity.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_forwardsIntensity.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_forwardsIntensity.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->forwardsIntensity = u_forwardsIntensity.real;
      offset += sizeof(this->forwardsIntensity);
      union {
        bool real;
        uint8_t base;
      } u_movingForwards;
      u_movingForwards.base = 0;
      u_movingForwards.base |= ((uint8_t) (*(inbuffer + offset + 0))) << (8 * 0);
      this->movingForwards = u_movingForwards.real;
      offset += sizeof(this->movingForwards);
     return offset;
    }

    const char * getType(){ return "rumarino_package/ForwardsCommand"; };
    const char * getMD5(){ return "7cc50976fb171be96f2abafc072f2cd0"; };

  };

}
#endif