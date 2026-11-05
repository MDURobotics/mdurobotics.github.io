---
title: "KARIS: a humanoid robot in the factory"
excerpt: "Can a human-like robot do an ordinary factory job without rebuilding the factory?"
order: 3
year: 2026
subjects: [Programming, Mathematics, Physics, Technology]
facts:
  - label: "Robot"
    value: "Unitree G1, a humanoid robot with hands that can grasp"
  - label: "Partner"
    value: "Volvo"
  - label: "Goal"
    value: "Pick the right parts for an assembly tray, on both a clear and a cluttered table"
updates:
  - date: 2026-10-30
    text: "From following objects to grasping them. Hands shaped like a human's are harder to pick with than you might think."
    url: "https://www.linkedin.com/feed/update/urn:li:activity:7521917906683686913/"
  - date: 2026-10-29
    text: "Object recognition and motion planning work. Connecting them to a reliable grasp is the biggest challenge."
    url: "https://www.linkedin.com/feed/update/urn:li:activity:7521516263634923520/"
  - date: 2026-09-14
    text: "The team presented KARIS, a humanoid robot for industrial picking, and how it will be tested both in a real factory environment and in the lab."
    url: "https://www.linkedin.com/feed/update/urn:li:activity:7505197405500510208/"
---

## The problem

Factories are built for people: shelves at the right height, tools for hands, aisles for feet. An ordinary industrial robot requires the workplace to be rebuilt around it. In theory, a humanoid could take a person's place directly. The job the team is testing is called *kitting*: collecting the parts needed for one assembly step and placing them in the right spot in a tray. It is a bit like packing a grocery bag from a recipe.

## How it works

- **Sense** The robot's camera sees the table. AI recognises which parts are there and whether any part is unknown.
- **Plan** Another AI model works out exactly where each part is and how it is turned in every direction. The program then calculates how each joint in the arm must be angled for the hand to end up in the right place without hitting anything.
- **Act** The hand grasps the part, the arm moves it and places it in the right compartment of the tray. This is where physics comes in: the hand must squeeze hard enough for friction to hold the part, but not so hard that it gets damaged. And when the arm accelerates, the mass of both the part and the arm itself affects how much force the motors need.
{: .sta}

**Why is it hard?** Last year, a degree project managed the same task, but slowly and not every time. This year the team lets AI handle what the robot *sees*, but programs the movements themselves more precisely. The long-term goal is for the robot to be about as fast as a person.
{: .callout}

## Words to know

- **Humanoid:** a robot built with the human body as a model.
- **6D pose:** where an object is (x, y, z) and how it is turned (three angles).
- **Inverse kinematics:** calculating backwards from where the hand should be to how each joint should be angled.
- **Dynamics:** the study of how forces affect motion, for example how much the motors must manage to move the arm quickly but smoothly.

**Think about:** Is it smarter to build robots that look like people, or to rebuild workplaces for robots? What speaks for and against each?
{: .ask}
