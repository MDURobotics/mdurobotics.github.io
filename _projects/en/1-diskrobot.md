---
title: "A robot that loads the dishwasher"
excerpt: "A two-armed robot is to put a cup in the dishwasher basket in under ten seconds."
order: 1
year: 2026
builds_on: [2025-diskrobot]
subjects: [Programming, Mathematics, Technology, Physics]
facts:
  - label: "Robot"
    value: "ABB YuMi, a two-armed robot made to work close to people"
  - label: "Builds on"
    value: "Last year's team, which succeeded in 76% of the attempts"
  - label: "Goal"
    value: "Cup in the basket in under 10 s, plus a home-made three-fingered robot hand"
team: "GREG"
updates:
  - date: 2026-11-02
    text: "YuMi picked up all the cups from the table in one go. The 3D camera finds the cups, a second camera sees what the basket looks like, and the robot tries again if a grasp fails."
    url: "https://www.linkedin.com/feed/update/urn:li:activity:7522929000432902144/"
  - date: 2026-10-21
    text: "The gripper moves! Servo motors pull the cables so that the fingers bend and the wrist turns."
    url: "https://www.linkedin.com/feed/update/urn:li:activity:7518622810273951744/"
  - date: 2026-10-08
    text: "From the moment the robot picks up the cup until it is in place now takes 7 seconds, under the 10-second goal. Network delay and the camera that finds free spots in the basket are not included yet."
    url: "https://www.linkedin.com/feed/update/urn:li:activity:7514045897086009344/"
  - date: 2026-10-06
    text: "The first prototype of the 3D-printed gripper with three cable-driven fingers is assembled."
    url: "https://www.linkedin.com/feed/update/urn:li:activity:7513149847277895680/"
---

## The problem

Loading the dishwasher is easy for you but hard for a robot. Cups face different directions, have different shapes, and some spots in the basket are already taken. Last year's team got the robot to lift paper cups and put them on a table. This year they are going into a real dishwasher basket, and it has to be faster.

## How it works

- **Sense** A 3D camera on the robot finds the cup. A second camera looks down into the basket and sees which spots are free, a bit like the systems that show free parking spaces.
- **Plan** The AI model YOLO recognises the cup. The program converts the camera image into coordinates the robot understands.
- **Act** The arm grasps the cup and puts it in a free spot in the basket.
{: .sta}

**Did you know?** The team is also building a 3D-printed robot hand with three fingers pulled by cables, much like the tendons in your hand. To notice if the cup is starting to slip, they use, among other things, the same type of sensor as in a computer mouse. If the sensor feels the cup moving, the hand grips harder.
{: .callout}

## Words to know

- **Collaborative robot:** a robot built to work close to people without a fence around it.
- **Calibration:** making the camera's and the robot's coordinate systems agree.
- **Tendon-driven gripper:** a robot hand where the fingers are pulled by cables instead of having a motor in every joint.

**Think about:** Why is it harder for a robot to load dishes than to weld a car together, even though welding seems more advanced?
{: .ask}
