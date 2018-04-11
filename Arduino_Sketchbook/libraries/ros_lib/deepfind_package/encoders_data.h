#ifndef _ROS_deepfind_package_encoders_data_h
#define _ROS_deepfind_package_encoders_data_h

#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"

namespace deepfind_package
{

  class encoders_data : public ros::Msg
  {
    public:
      typedef const char* _help_type;
      _help_type help;

    encoders_data():
      help("")
    {
    }

    virtual int serialize(unsigned char *outbuffer) const
    {
      int offset = 0;
      uint32_t length_help = strlen(this->help);
      varToArr(outbuffer + offset, length_help);
      offset += 4;
      memcpy(outbuffer + offset, this->help, length_help);
      offset += length_help;
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer)
    {
      int offset = 0;
      uint32_t length_help;
      arrToVar(length_help, (inbuffer + offset));
      offset += 4;
      for(unsigned int k= offset; k< offset+length_help; ++k){
          inbuffer[k-1]=inbuffer[k];
      }
      inbuffer[offset+length_help-1]=0;
      this->help = (char *)(inbuffer + offset-1);
      offset += length_help;
     return offset;
    }

    const char * getType(){ return "deepfind_package/encoders_data"; };
    const char * getMD5(){ return "6ded41f8a691465b353a1de637830f92"; };

  };

}
#endif