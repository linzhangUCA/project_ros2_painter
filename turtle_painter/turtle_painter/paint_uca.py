"""
Make the simulated turtle draw 'UCA' using this code
"""
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class TurtlePainter(Node):
    """
    Program the simulated turtle class. The turtle is expected to listen its
    status (e.g. pose, pen states, etc.) `turtlesim_node` and publish
    appropriate control signal to draw three letters: 'UCA' on the canvas.
    """

    def __init__(self):
        super().__init__('turtle_painter')


def main(args=None):
    """
    Write code to make your own main function.
    """
    print('Hi from turtle_painter.')


if __name__ == '__main__':
    main()
