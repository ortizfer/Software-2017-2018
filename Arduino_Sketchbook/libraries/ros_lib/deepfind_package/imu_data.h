#ifndef _ROS_deepfind_package_imu_data_h
#define _ROS_deepfind_package_imu_data_h

#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"
#include "std_msgs/Header.h"

namespace deepfind_package
{

  class imu_data : public ros::Msg
  {
    public:
      typedef std_msgs::Header _header_type;
      _header_type header;
      typedef float _yaw_type;
      _yaw_type yaw;
      typedef float _pitch_type;
      _pitch_type pitch;
      typedef float _roll_type;
      _roll_type roll;
      typedef float _acc_x_type;
      _acc_x_type acc_x;
      typedef float _acc_y_type;
      _acc_y_type acc_y;
      typedef float _acc_z_type;
      _acc_z_type acc_z;
      typedef float _gyr_x_type;
      _gyr_x_type gyr_x;
      typedef float _gyr_y_type;
      _gyr_y_type gyr_y;
      typedef float _gyr_z_type;
      _gyr_z_type gyr_z;
      typedef float _mag_x_type;
      _mag_x_type mag_x;
      typedef float _mag_y_type;
      _mag_y_type mag_y;
      typedef float _mag_z_type;
      _mag_z_type mag_z;

    imu_data():
      header(),
      yaw(0),
      pitch(0),
      roll(0),
      acc_x(0),
      acc_y(0),
      acc_z(0),
      gyr_x(0),
      gyr_y(0),
      gyr_z(0),
      mag_x(0),
      mag_y(0),
      mag_z(0)
    {
    }

    virtual int serialize(unsigned char *outbuffer) const
    {
      int offset = 0;
      offset += this->header.serialize(outbuffer + offset);
      offset += serializeAvrFloat64(outbuffer + offset, this->yaw);
      offset += serializeAvrFloat64(outbuffer + offset, this->pitch);
      offset += serializeAvrFloat64(outbuffer + offset, this->roll);
      offset += serializeAvrFloat64(outbuffer + offset, this->acc_x);
      offset += serializeAvrFloat64(outbuffer + offset, this->acc_y);
      offset += serializeAvrFloat64(outbuffer + offset, this->acc_z);
      offset += serializeAvrFloat64(outbuffer + offset, this->gyr_x);
      offset += serializeAvrFloat64(outbuffer + offset, this->gyr_y);
      offset += serializeAvrFloat64(outbuffer + offset, this->gyr_z);
      offset += serializeAvrFloat64(outbuffer + offset, this->mag_x);
      offset += serializeAvrFloat64(outbuffer + offset, this->mag_y);
      offset += serializeAvrFloat64(outbuffer + offset, this->mag_z);
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer)
    {
      int offset = 0;
      offset += this->header.deserialize(inbuffer + offset);
      offset += deserializeAvrFloat64(inbuffer + offset, &(this->yaw));
      offset += deserializeAvrFloat64(inbuffer + offset, &(this->pitch));
      offset += deserializeAvrFloat64(inbuffer + offset, &(this->roll));
      offset += deserializeAvrFloat64(inbuffer + offset, &(this->acc_x));
      offset += deserializeAvrFloat64(inbuffer + offset, &(this->acc_y));
      offset += deserializeAvrFloat64(inbuffer + offset, &(this->acc_z));
      offset += deserializeAvrFloat64(inbuffer + offset, &(this->gyr_x));
      offset += deserializeAvrFloat64(inbuffer + offset, &(this->gyr_y));
      offset += deserializeAvrFloat64(inbuffer + offset, &(this->gyr_z));
      offset += deserializeAvrFloat64(inbuffer + offset, &(this->mag_x));
      offset += deserializeAvrFloat64(inbuffer + offset, &(this->mag_y));
      offset += deserializeAvrFloat64(inbuffer + offset, &(this->mag_z));
     return offset;
    }

    const char * getType(){ return "deepfind_package/imu_data"; };
    const char * getMD5(){ return "5781ee5294affb6dd3e062f6edb954b1"; };

  };

}
#endif