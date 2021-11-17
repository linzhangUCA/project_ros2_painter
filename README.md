# Project - ROS2 Managed Robot
This is the final project in Robotics 1 class. In this project, we will control
the simulated turtle to write **UCA** on the simulation canvas. In the mean 
time, your Hexa robot will be driven by the same command that drives the 
simulated turtle. All the tasks will be managed by ROS2.

## Workflow
1. Launch `turtlesim_node`.
2. Start a Hexa robot driving node.
3. Start a letter drawing node. 
4. The letter drawing node will govern the simulated turtle to automatically 
paint letters: **UCA** in the simulation. The Hexa robot will be driven to at 
the same time.
5. In case of no encoders are available, the simulated robot is expected to 
be controlled back to the original position using P(ID) control. See 
following picture for an example.  
![turtlesim_example](https://github.com/linzhangUCA/project_ros2_painter/blob/main/turtlesim_example.png)

## Requirements 
Following materials are required to complete this project.
1. (35%) Python code for Hexa robot driving node. By starting this node, your 
robot is expected to monitor a velocity command topic, which contains the 
`geometry_msgs/Twist` message. The robot should be able to correctly respond 
to nonzero velocity commands, and manuever thereafter. **In the case of absent
of encoder reading devices, you can discretize robot actions and fix motor 
speed.** 
> Find the example staring code in the `hexar_driver` package. 

2. (35%) Python code for drawing the **UCA** letters in the turtlesim. 
You'll need to compute correct velocity commands according to the status of
the turtle. The pen can be mounted or disarmed by calling a service. So, you 
may find [*Writing a simple service and client tutorial*](https://docs.ros.org/en/galactic/Tutorials/Writing-A-Simple-Py-Service-And-Client.html)
helpful. 
> Find the example staring code in the `turtle_painter` package.

3. (20%) Complete the project report and upload the demo video. You'll need 
to edit this `README.md` file and complete the sections of **Summary, 
Material List, Software List, and Usage**

4. (10%) PID control implementation
  - If encoders are available, modify the code in your `hexar_driver` 
package. The motor speed will be controlled by a PID controller given the 
reference motor/wheel speed. 
> Hint: convert the `cmd_vel` into the 
referenced motor speeds. Input of your PID controller is the error between
the referenced motor speeds and the actual motor speeds read by the encoders.
  - If encoders are **NOT** available, modify the code in your 
`turtle_painter` package. Drive the turtle back to the original position 
using PID control. 
> Hint: You may want the turtle to only move forward 
(forward left and forward right). Two sets of PID controllers may required.
One for controlling the linear velocity. Input of it could be the displacement
between the turtle's present position and original position; output could be 
the linear velocity that is going to be published as a `cmd_vel` topic.
Another PID controller is for tuning the angular velocity. Input of it could 
be the angular error beteen the orientation of the turtle and the line 
connecting turtle's present position and its original position.

## Get Started
Open up a terminal on your Ubuntu laptop and run following commands to use 
the template. 
> Substitute `ros_ws` with your own ROS2 workspace name.
```bash
cd ~/ros_ws/src/
git clone https://github.com/linzhangUCA/project_ros2_painter.git
cd ..
colcon build --symlink-install
```

## Summary
> Write below to complete this report. You may want to read the [Markdown guide](https://guides.github.com/features/mastering-markdown/) to better format this report.

### Material List
> Please list hardware (better with links) used in this project below.  

### Software List
> Please list and briefly describe the Python libraries and any software used to realize the robot.

### Usage
> Briefly describe how to use this robot. 



