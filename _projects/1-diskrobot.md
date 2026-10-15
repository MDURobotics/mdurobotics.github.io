---
title: "Robot som plockar in i diskmaskinen"
excerpt: "En tvåarmad robot ska ställa in en kopp i diskmaskinskorgen på under tio sekunder."
order: 1
subjects: [Programmering, Matematik, Teknik, Fysik]
facts:
  - label: "Robot"
    value: "ABB YuMi, en tvåarmad robot gjord för att jobba nära människor"
  - label: "Bygger på"
    value: "Förra årets grupp, som lyckades i 76 % av försöken"
  - label: "Mål"
    value: "Kopp i korgen på under 10 s, plus en egen robothand med tre fingrar"
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