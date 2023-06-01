#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float64

global pub1, pub2, received_data

def callback(data):
    #rospy.loginfo('I heard %f', data.data)
    received_data = data.data

    if(received_data == 1.0):
        print("Drive")
        pub1.publish(10.0)
        pub2.publish(-10.0)
    elif(received_data == 2.0):
        print("Reverse")
        pub1.publish(-10.0)
        pub2.publish(10.0)

    elif(received_data == 3.0):
        print("Turn left")
        pub1.publish(-5.0)
        pub2.publish(-5.0)

    elif(received_data == 4.0):
        print("Turn right")
        pub1.publish(5.0)
        pub2.publish(5.0)
    else:
        print("Stop")
        pub1.publish(0.0)
        pub2.publish(0.0)

    

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber('button_state', Float64, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    pub1 = rospy.Publisher('/my_diffbot/leftWheel_velocity_controller/command', Float64, queue_size=10)
    pub2 = rospy.Publisher('/my_diffbot/rightWheel_velocity_controller/command', Float64, queue_size=10)
    listener()
