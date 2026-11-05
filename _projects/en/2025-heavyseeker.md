---
title: "HeavySeeker: the robot that finds its way in the forest"
excerpt: "Software and sensors that let a robot vehicle drive itself between points in the forest, even when the GPS is poor."
order: 4
year: 2025
subjects: [Programming, Mathematics, Technology]
facts:
  - label: "Robot"
    value: "Clearpath Husky, an off-the-shelf robot vehicle that the team rebuilt with new sensors"
  - label: "Home"
    value: "SLaRC, MDU's research centre for ground-based robotics"
  - label: "Result"
    value: "The robot drove itself between selected points in a forest environment and could be remote-controlled with video"
---

## The problem

In the forest it is hard for a robot to know where it is. The trees block the GPS signal, the ground is uneven and things can move. The team was to give the robot vehicle senses and software so that it can drive itself between points chosen by a person, and be controlled remotely when it is out of sight.

## How it works

- **Sense** A LiDAR scans the surroundings with lasers and a depth camera sees obstacles. An extra-precise GPS (RTK) gives the position, and sensors on the wheels measure how far the vehicle has driven.
- **Plan** A Kalman filter combines all the sensors into a best guess of where the robot is, even when the GPS is poor. The navigation software Nav2 draws a map of obstacles and works out a path around them.
- **Act** The robot drives to the next point. A person can take over at any time and steer using video from the robot.
{: .sta}

## How did it go?

The robot was tested both in simulation and out in a forest environment. It could be remote-controlled and drive itself between points, even though the GPS signal was sometimes weak. The software is built in parts that can be tested separately, so that others can build on it.

## Words to know

- **LiDAR:** a sensor that measures distance with laser pulses, a bit like radar but with light.
- **Kalman filter:** a mathematical method that combines uncertain measurements into a better guess.
- **Waypoint:** a point that the robot is to reach on its way.

**Think about:** If the GPS says one thing and the wheels say another, which should the robot trust?
{: .ask}
