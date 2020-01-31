#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

def move():
    #Starts a new node
    PI = 3.14159265389
    rospy.init_node('robot',anonymous=True)
    velocity_publisher =rospy.Publisher('turtle1/cmd_vel',Twist,queue_size=10)
    vel_msg = Twist()
    #Receiving the user's input
    print("Lets move your robot")
    distance = input("Type your distance:")
    #Checking if the movement is forward or backwards
    #Since we are moving just in x-axis
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    t0 = rospy.Time.now().to_sec()
    current_distance = 0
    count = 0
    while (1):
        #Setting the current time for distance calculus
        vel_msg.linear.x = 0.2
        vel_msg.angular.z = 0
        velocity_publisher.publish(vel_msg)
        t1 = rospy.Time.now().to_sec()
        current_distance=(t1-t0)*vel_msg.linear.x
        #Loop to move the turtle in an specified distance
        count = count + 1
        if current_distance > distance :
            t2 = rospy.Time.now().to_sec()
        while (current_distance > distance):
            vel_msg.linear.x = 0
            vel_msg.angular.z = 0.2
            #Publish the velocity
            velocity_publisher.publish(vel_msg)
            #Takes actual time to velocity calculus
            t3 = rospy.Time.now().to_sec()
            current_angular = (t3-t2)* 0.2
            if current_angular > PI/2:
                current_distance = 0
                t0 = rospy.Time.now().to_sec()
        #After the loop,stops the robot
        #vel_msg.linear.x = 0
        #Force the robot to stop
        #velocity_publisher.publish(vel_msg)
if __name__ == '__main__':
    try:
        #Testing our function
        move()
    except rospy.ROSInterruptException: pass
