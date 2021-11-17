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
be controlled back to the original position using P(ID) control.

## Requirements 
Following materials are required to complete this project.
1. (30%) Python code for Hexa robot driving node. By starting this node, your 
robot is expected to monitor a velocity command topic, which contains the 
`geometry_msgs/Twist` message. The robot should be able to correctly respond 
to nonzero velocity commands, and manuever thereafter. **In the case of absent
of encoder reading devices, you can discretize robot actions and fix motor 
speed.** > Find the example staring code in the `hexar_driver` package. 

2. (30%) Python code for drawing the **UCA** letters in the turtlesim computes correct commands and drives the 
turtle to draw letters: **UCA**. 

## Usage

## Summary
> Write below to complete this report. You may want to read the [Markdown guide](https://guides.github.com/features/mastering-markdown/) to better format this report.

### Material List
> Please list hardware (better with links) used in this project below.  

### Software List
> Please list and briefly describe the Python libraries and any software used to realize the robot.

### Usage
> Briefly describe how to use this robot. Imagine you are teaching a person how to use your robot.



