---
title: "The robot that copes when the network goes down"
excerpt: "What should an AI-controlled robot do when the internet disappears in the middle of the job?"
order: 2
year: 2026
subjects: [Programming, Technology]
facts:
  - label: "Robot"
    value: "ABB YuMi picking up dishes"
  - label: "Partner"
    value: "Westermo and Arcticus Systems, companies in industrial networks and embedded systems"
  - label: "Goal"
    value: "Switch to backup mode within 5 s and stop safely within 10 s"
team: "H.E.R.B."
updates:
  - date: 2026-10-27
    text: "The camera finds the cup and the robot moves there on its own. The motion is still a bit jerky, so the next step is to make it smoother."
    url: "https://www.linkedin.com/feed/update/urn:li:activity:7520770687280787458/"
  - date: 2026-10-23
    text: "The team won the HackFactory hackathon at MITC. The challenge from Alfa Laval was to turn old 2D drawings into 3D models with AI that runs locally, without the cloud."
    url: "https://www.linkedin.com/feed/update/urn:li:activity:7519343971609874432/"
  - date: 2026-10-01
    text: "The team presents the project, done together with Westermo: a robot that keeps picking up cups even when the network goes down."
    url: "https://www.linkedin.com/feed/update/urn:li:activity:7511404282605174784/"
---

## The problem

Large AI models often run on powerful servers somewhere in the cloud. That works well until the network acts up. A robot that suddenly gets old or wrong instructions can do something dangerous. So the team is building a system that gradually steps down to simpler solutions instead of crashing.

## Four modes

| Mode | What runs |
|---|---|
| **Normal** | Large AI model in the cloud. At least 85% accuracy. |
| **Backup 1** | Smaller model on a Raspberry Pi next to the robot. |
| **Backup 2** | A minimal model on an industrial network computer. |
| **Safe stop** | The arm returns to its rest position. |

## How it works

- **Sense** A camera looks down on the dishes from above. At the same time, the system constantly checks whether the AI services are responding.
- **Plan** The best available AI model works out where the cup is and how it is turned. If no model responds, the robot is not allowed to guess.
- **Act** The robot picks up the dishes, more slowly if it is running in backup mode, or stops safely.
{: .sta}

**It is also about security.** Researchers have shown that industrial robots sometimes accept motion commands over the network without checking them. So the team is doing a threat analysis: what could an attacker do, and how do you stop it? One protection is that the robot checks that the coordinates it receives are reasonable before it moves.
{: .callout}

## Words to know

- **Edge AI:** AI that runs on a small computer close to the machine instead of in the cloud.
- **Fail-safe:** when something goes wrong, the system ends up in a harmless state.
- **Threat model:** a systematic list of how a system can be attacked.

**Think about:** What other things in your everyday life should work even without the internet? What does a map app do when you lose coverage, for example?
{: .ask}
