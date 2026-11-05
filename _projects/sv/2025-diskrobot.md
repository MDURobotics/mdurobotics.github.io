---
title: "Diskroboten som hittar muggar"
excerpt: "En tvåarmad robot lärde sig hitta, greppa och flytta muggar med hjälp av en 3D-kamera och AI."
order: 1
year: 2025
subjects: [Programmering, Matematik, Teknik]
facts:
  - label: "Robot"
    value: "ABB YuMi, en tvåarmad robot gjord för att jobba nära människor"
  - label: "Hemvist"
    value: "MARC-projektet på MDU, som undersöker hur robotar kan hjälpa till i produktionen"
  - label: "Resultat"
    value: "Roboten hittade och plockade upp muggen i 76 % av försöken"
---

## Problemet

Robotar i fabriker gör samma sak om och om igen, med delar som alltid ligger på exakt samma ställe. Hemma är det tvärtom: en mugg kan stå var som helst och åt vilket håll som helst. Gruppen ville ta ett första steg mot robotar som hjälper till med vardagssysslor, och valde en uppgift alla känner igen: att ställa in disk i diskmaskinen.

## Så funkar den

- **Känna** En 3D-kamera (OAK-D Pro) ser både hur muggen ser ut och hur långt bort den står.
- **Planera** AI-modellen YOLO, som gruppen själva tränade på bilder av muggar, hittar muggen och avgör hur den är vriden. Ett Python-program räknar om kamerans koordinater till robotens.
- **Agera** Robotarmen åker fram, greppar muggen och lyfter den.
{: .sta}

## Hur gick det?

Roboten klarade att hitta och plocka upp muggen i 76 % av försöken. Att få den hela vägen in i en riktig diskkorg blev nästa års uppgift.

## Ord att kunna

- **YOLO:** "You Only Look Once", en AI-modell som hittar föremål i en bild på en gång i stället för att leta bit för bit.
- **Stereokamera:** en kamera med två linser, som dina två ögon, så att den kan räkna ut avstånd.
- **Koordinatsystem:** ett sätt att ange var något finns med siffror. Kameran och roboten har var sitt, och de måste översättas till varandra.

**Fundera på:** 76 % låter ganska bra. Men hur ofta skulle du vilja att en robot tappade din favoritmugg?
{: .ask}
