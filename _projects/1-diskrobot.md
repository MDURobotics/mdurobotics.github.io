---
title: "Robot som plockar in i diskmaskinen"
excerpt: "En tvåarmad robot ska ställa in en kopp i diskmaskinskorgen på under tio sekunder."
order: 1
year: 2026
builds_on: [2025-diskrobot]
subjects: [Programmering, Matematik, Teknik, Fysik]
facts:
  - label: "Robot"
    value: "ABB YuMi, en tvåarmad robot gjord för att jobba nära människor"
  - label: "Bygger på"
    value: "Förra årets grupp, som lyckades i 76 % av försöken"
  - label: "Mål"
    value: "Kopp i korgen på under 10 s, plus en egen robothand med tre fingrar"
team: "GREG"
updates:
  - date: 2026-11-02
    text: "YuMi plockade upp alla koppar från bordet i ett svep. 3D-kameran hittar kopparna, en andra kamera ser hur det ser ut i korgen, och roboten försöker igen om ett grepp misslyckas."
    url: "https://www.linkedin.com/feed/update/urn:li:activity:7522929000432902144/"
  - date: 2026-10-21
    text: "Griparen rör sig! Servomotorer drar i vajrarna så att fingrarna böjs och handleden vrider sig."
    url: "https://www.linkedin.com/feed/update/urn:li:activity:7518622810273951744/"
  - date: 2026-10-08
    text: "Från att roboten tar koppen tills den står på plats tar det nu 7 sekunder, under målet på 10. Nätverksfördröjningen och kameran som ser lediga platser i korgen är inte med än."
    url: "https://www.linkedin.com/feed/update/urn:li:activity:7514045897086009344/"
  - date: 2026-10-06
    text: "Den första prototypen av den 3D-printade griparen med tre vajerstyrda fingrar är monterad."
    url: "https://www.linkedin.com/feed/update/urn:li:activity:7513149847277895680/"
---

## Problemet

Att ställa in disk är lätt för dig men svårt för en robot. Koppar står åt olika håll, har olika form och korgen har platser som redan är upptagna. Förra årets grupp fick roboten att lyfta pappersmuggar och ställa dem på ett bord. I år ska de hamna i en riktig diskkorg, och det ska gå snabbare.

## Så funkar den

- **Känna** En 3D-kamera på roboten hittar koppen. En andra kamera tittar ner i korgen och ser vilka platser som är lediga, ungefär som system som visar lediga parkeringsplatser.
- **Planera** AI-modellen YOLO känner igen koppen. Programmet räknar om kamerans bild till koordinater som roboten förstår.
- **Agera** Armen greppar koppen och ställer den på en ledig plats i korgen.
{: .sta}

**Visste du?** Gruppen bygger också en 3D-printad robothand med tre fingrar som dras av vajrar, ungefär som senorna i din hand. För att märka om koppen håller på att glida använder de bland annat samma typ av sensor som sitter i en datormus. Känner sensorn att koppen rör sig, greppar handen hårdare.
{: .callout}

## Ord att kunna

- **Kollaborativ robot:** en robot byggd för att arbeta nära människor utan staket runt sig.
- **Kalibrering:** att få kamerans och robotens koordinatsystem att stämma överens.
- **Senstyrd gripare:** en robothand där fingrarna dras av vajrar istället för att ha en motor i varje led.

**Fundera på:** Varför är det svårare för en robot att plocka disk än att svetsa ihop en bil, fast svetsning verkar mer avancerat?
{: .ask}