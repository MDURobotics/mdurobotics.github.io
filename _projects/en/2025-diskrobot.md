---
title: "The dishwashing robot that finds mugs"
excerpt: "A two-armed robot learned to find, grasp and move mugs with the help of a 3D camera and AI."
order: 1
year: 2025
subjects: [Programming, Mathematics, Technology]
facts:
  - label: "Robot"
    value: "ABB YuMi, a two-armed robot made to work close to people"
  - label: "Home"
    value: "The MARC project at MDU, which explores how robots can help in production"
  - label: "Result"
    value: "The robot found and picked up the mug in 76% of the attempts"
---

## The problem

Robots in factories do the same thing over and over, with parts that always lie in exactly the same place. At home it is the opposite: a mug can be anywhere, facing any direction. The team wanted to take a first step towards robots that help with everyday chores, and chose a task everyone recognises: loading the dishwasher.

## How it works

- **Sense** A 3D camera (OAK-D Pro) sees both what the mug looks like and how far away it is.
- **Plan** The AI model YOLO, which the team trained themselves on pictures of mugs, finds the mug and decides how it is turned. A Python program converts the camera's coordinates into the robot's.
- **Act** The robot arm moves in, grasps the mug and lifts it.
{: .sta}

## How did it go?

The robot managed to find and pick up the mug in 76% of the attempts. Getting it all the way into a real dishwasher basket became the next year's task.

## Words to know

- **YOLO:** "You Only Look Once", an AI model that finds objects in an image all at once instead of searching piece by piece.
- **Stereo camera:** a camera with two lenses, like your two eyes, so that it can work out distance.
- **Coordinate system:** a way of stating where something is with numbers. The camera and the robot each have their own, and they must be translated into each other.

**Think about:** 76% sounds pretty good. But how often would you want a robot to drop your favourite mug?
{: .ask}
