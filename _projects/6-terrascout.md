---
title: "TerraScout: terrängroboten"
excerpt: "En obemannad terrängbil som ska utföra uppdrag på egen hand och ändra rutt när den upptäcker något på vägen."
order: 6
subjects: [Programmering, Matematik, Teknik]
---

| **Robot** | TerraScout, en fyrhjulig terrängrobot byggd av tidigare studenter |
| **Hemvist** | SLaRC, MDU:s forskningscenter för markbaserad robotik |
| **Mål** | Besöka fem punkter i bästa ordning och planera om rutten när den hittar hinder |

## Problemet

Robotar som kör ute i naturen används i jordbruk, gruvor och för övervakning. Utomhus finns inga raka korridorer: marken är ojämn och nya hinder kan dyka upp. TerraScout kan redan köra från en punkt till en annan. I år ska den klara ett helt uppdrag och själv förstå vad den ser.

## Så funkar den

- **Känna:** En LiDAR skannar omgivningen med laser, en djupkamera ser objekt, och en extra noggrann GPS anger position på centimeternivå.
- **Tänka:** AI känner igen objekt och räknar ut var de står. Runt dem ritas en förbjuden zon på kartan. Programmet räknar fram i vilken ordning punkterna ska besökas och gör en ny plan om vägen blockeras.
- **Göra:** Roboten kör rutten, fotograferar det den hittar och sparar allt i en logg. Den har nödstopp och en människa med fjärrkontroll kan alltid ta över.

**Ett klassiskt matteproblem.** Att hitta den kortaste vägen som besöker flera punkter kallas handelsresandeproblemet. Med fem punkter finns 120 möjliga ordningar, så en dator kan testa alla. Med 20 punkter finns över 2 miljarder miljarder ordningar, och då behövs smartare metoder.
{: .notice--warning}

## Ord att kunna

- **UGV:** Unmanned Ground Vehicle, ett obemannat markfordon.
- **LiDAR:** en sensor som mäter avstånd med laserpulser, ungefär som radar fast med ljus.
- **Omplanering:** att räkna fram en ny rutt medan roboten redan kör.

**Fundera på:** Du ska handla på fem ställen i stan. Hur väljer du ordning? Skulle du och en dator välja samma väg?
{: .notice--info}
