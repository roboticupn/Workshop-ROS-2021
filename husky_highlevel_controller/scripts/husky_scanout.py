#! /usr/bin/env python
import rospy
from std_msgs.msg import String

def main():
    pub = rospy.Publisher('scan_out', String, queue_size=10)
    rospy.init_node('husky_scanout', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        _str = "value : %s" % rospy.get_time()
        rospy.loginfo(_str)
        pub.publish(_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
