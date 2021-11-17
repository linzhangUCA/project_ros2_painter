"""
A ROS2 version motor driver. The Hexa robot is expected to take in a `Twist`
message and drive the motors using PhaseEnableRobot. In the case of absent 
encoders, define functions like: foward_left(), forward_right(), 
backward_left(), backward_right() to simplify your robot's behavior.

"""
from gpiozero import LED, PhaseEnableRobot
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class HexarDriver(Node):
    """
    Write your code below to complete the simulated turtle class. The turtle is
    expected to listen its status (e.g. pose, pen states, etc.)
    `turtlesim_node` and publish appropriate control signal to draw three
    letters: 'UCA' on the canvas.
    """

    def __init__(self):
        super().__init__('hexar_driver')


def main(args=None):
    print('Hi from hexar_driver.')


if __name__ == '__main__':
    main()
