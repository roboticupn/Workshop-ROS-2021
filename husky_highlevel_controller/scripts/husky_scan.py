#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan

def laser_callback(msg):
   
    rospy.info(rospy.get_caller_id() + 'value : %s', msg.range_min)

def main():
    rospy.init_node('husky_scan', anonymous=True)
    topic = rospy.get_param('/laser_scan/topic')
    queue_size = rospy.get_param('/laser_scan/queue_size') 
    if !topic:
	ROS_ERROR("Couldn't find topic parameter!")
    if !queue_size:
	ROS_ERROR("Couldn't find queue_size parameter!")

    rospy.Subscriber(topic,queue_size,laser_callback)
    rospy.spin()

if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass
