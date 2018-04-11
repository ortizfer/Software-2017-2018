#ifndef _ROS_deepfind_package_sensor_data_h
#define _ROS_deepfind_package_sensor_data_h

#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"
#include "deepfind_package/imu_data.h"
#include "sensor_msgs/LaserScan.h"
#include "deepfind_package/encoders_data.h"

namespace deepfind_package
{

  class sensor_data : public ros::Msg
  {
    public:
      typedef deepfind_package::imu_data _imu_type;
      _imu_type imu;
      typedef sensor_msgs::LaserScan _lidar_type;
      _lidar_type lidar;
      typedef deepfind_package::encoders_data _encoder_type;
      _encoder_type encoder;

    sensor_data():
      imu(),
      lidar(),
      encoder()
    {
    }

    virtual int serialize(unsigned char *outbuffer) const
    {
      int offset = 0;
      offset += this->imu.serialize(outbuffer + offset);
      offset += this->lidar.serialize(outbuffer + offset);
      offset += this->encoder.serialize(outbuffer + offset);
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer)
    {
      int offset = 0;
      offset += this->imu.deserialize(inbuffer + offset);
      offset += this->lidar.deserialize(inbuffer + offset);
      offset += this->encoder.deserialize(inbuffer + offset);
     return offset;
    }

    const char * getType(){ return "deepfind_package/sensor_data"; };
    const char * getMD5(){ return "607c2e43fa35473ad64e71758a520fd3"; };

  };

}
#endif