---
title: "TerraScout: the off-road robot"
excerpt: "An unmanned off-road vehicle that is to carry out missions on its own and change route when it discovers something on the way."
order: 6
year: 2026
builds_on: [2025-lightseeker, 2025-heavyseeker]
subjects: [Programming, Mathematics, Technology]
facts:
  - label: "Robot"
    value: "TerraScout, a four-wheeled off-road robot built by earlier students"
  - label: "Home"
    value: "SLaRC, MDU's research centre for ground-based robotics"
  - label: "Goal"
    value: "Visit five points in the best order and replan the route when it finds obstacles"
---

## The problem

Robots that drive outdoors are used in farming, mining and surveillance. Outdoors there are no straight corridors: the ground is uneven and new obstacles can appear. TerraScout can already drive from one point to another. This year it has to complete a whole mission and understand what it sees by itself.

## How it works

- **Sense** A LiDAR scans the surroundings with lasers, a depth camera sees objects, and an extra-precise GPS gives the position to the centimetre.
- **Plan** AI recognises objects and works out where they are. A no-go zone is drawn around them on the map. The program works out the order in which to visit the points and makes a new plan if the way is blocked.
- **Act** The robot drives the route, photographs what it finds and saves everything in a log. It has an emergency stop, and a person with a remote control can always take over.
{: .sta}

**A classic maths problem.** Finding the shortest route that visits several points is called the travelling salesman problem. With five points there are 120 possible orders, so a computer can try them all. With 20 points there are more than 2 billion billion orders, and then smarter methods are needed.
{: .callout}

## Words to know

- **UGV:** Unmanned Ground Vehicle.
- **LiDAR:** a sensor that measures distance with laser pulses, a bit like radar but with light.
- **Replanning:** working out a new route while the robot is already driving.

**Think about:** You are going shopping at five places in town. How do you choose the order? Would you and a computer choose the same route?
{: .ask}
