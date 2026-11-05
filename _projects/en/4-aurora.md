---
title: "AURORA: the arm that copies you"
excerpt: "A robot arm for rehabilitation research that is to learn to move like a person by watching one."
order: 4
year: 2026
builds_on: [2025-limb]
subjects: [Biology, Physics, Programming, Technology]
facts:
  - label: "Robot"
    value: "LIMB, a 3D-printed robot arm with a hand, developed at MDU"
  - label: "Builds on"
    value: "Several earlier student projects"
  - label: "Goal"
    value: "Record a person's arm movement and let the robot repeat it"
updates:
  - date: 2026-09-29
    text: "Two motion sensors and a camera follow a person's arm in real time and control a simulated robot arm. The next step is to add muscle signals (EMG)."
    url: "https://www.linkedin.com/feed/update/urn:li:activity:7510705551060930560/"
  - date: 2026-09-11
    text: "The team presented how AURORA will combine mechanics, sensors, simulation and control, and how the arm's ability to copy movements will be evaluated."
    url: "https://www.linkedin.com/feed/update/urn:li:activity:7504130680554012672/"
---

## The problem

Robots that are to work close to people, for example in rehabilitation or as prostheses, must move smoothly, safely and predictably. The LIMB arm already exists but has problems: the shoulder ends up crooked, the motors are too weak in some positions and the angle sensors drift after a while. The team will first make the arm reliable and then teach it to copy people.

## How it works

- **Sense** The person demonstrating the movement wears sensors. EMG sensors read the small electrical signals in the forearm muscles and notice when you want to close your hand. Motion sensors (the same type as in your phone) and a camera follow the arm's movement.
- **Plan** The computer combines the data from all sensors into a picture of the movement and turns it into a smooth path for the robot arm. The movement is tested in a simulation first.
- **Act** The robot arm makes the same movement. It has an emergency stop and returns to its start position if the power goes.
{: .sta}

**Did you know?** People move their arms in a surprisingly smooth way: the speed rises and falls evenly without jerks. Researchers have described this mathematically, and the team uses it to measure how human the robot's movement looks. The motors also need to be quiet, because in the future the arm may be controlled with brain signals, and noise then disturbs the measurements.
{: .callout}

## Words to know

- **EMG:** measuring the electrical activity of the muscles with sensors on the skin.
- **Sensor fusion:** combining several sensors so that they cover for each other's weaknesses.
- **Learning from demonstration:** the robot learns by watching a person do something instead of being programmed step by step.

**Think about:** Your phone knows roughly how you are holding it. How do you think it knows, and why is a single sensor not enough to follow a whole arm?
{: .ask}
