---
title: "Roboten som klarar att nätet går ner"
excerpt: "Vad ska en AI-styrd robot göra när internet försvinner mitt i jobbet?"
order: 2
year: 2026
subjects: [Programmering, Teknik]
facts:
  - label: "Robot"
    value: "ABB YuMi som plockar disk"
  - label: "Partner"
    value: "Westermo och Arcticus Systems, företag inom industriella nätverk och inbyggda system"
  - label: "Mål"
    value: "Byta till reservläge inom 5 s och stanna säkert inom 10 s"
team: "H.E.R.B."
updates:
  - date: 2026-10-27
    text: "Kameran hittar koppen och roboten rör sig dit på egen hand. Rörelsen är fortfarande lite ryckig, så nästa steg är att göra den mjukare."
    url: "https://www.linkedin.com/feed/update/urn:li:activity:7520770687280787458/"
  - date: 2026-10-23
    text: "Gruppen vann hackathonet HackFactory hos MITC. Utmaningen från Alfa Laval var att göra om gamla 2D-ritningar till 3D-modeller med AI som körs lokalt, utan molnet."
    url: "https://www.linkedin.com/feed/update/urn:li:activity:7519343971609874432/"
  - date: 2026-10-01
    text: "Gruppen berättar om projektet, som görs tillsammans med Westermo: en robot som fortsätter plocka koppar även när nätverket går ner."
    url: "https://www.linkedin.com/feed/update/urn:li:activity:7511404282605174784/"
---

## Problemet

Stora AI-modeller körs ofta på kraftfulla servrar någonstans i molnet. Det fungerar bra tills nätverket krånglar. En robot som plötsligt får gamla eller felaktiga instruktioner kan göra något farligt. Gruppen bygger därför ett system som gradvis växlar ner till enklare lösningar istället för att krascha.

## Fyra lägen

| Läge | Vad som körs |
|---|---|
| **Normal** | Stor AI-modell i molnet. Minst 85 % träffsäkerhet. |
| **Reserv 1** | Mindre modell på en Raspberry Pi bredvid roboten. |
| **Reserv 2** | En minimal modell på en industriell nätverksdator. |
| **Säkert stopp** | Armen åker tillbaka till sitt viloläge. |

## Så funkar den

- **Känna** En kamera tittar ovanifrån på disken. Samtidigt övervakar systemet hela tiden om AI-tjänsterna svarar.
- **Planera** Den bästa AI-modell som är tillgänglig räknar ut var koppen står och hur den är vriden. Svarar ingen modell får roboten inte gissa.
- **Agera** Roboten plockar disken, långsammare om den kör i reservläge, eller stannar säkert.
{: .sta}

**Det handlar också om säkerhet.** Forskare har visat att industrirobotar ibland tar emot rörelsekommandon över nätverket utan att kontrollera dem. Gruppen gör därför en hotanalys: vad kan en angripare göra, och hur stoppar man det? Ett skydd är att roboten kontrollerar att koordinaterna den får är rimliga innan den rör sig.
{: .callout}

## Ord att kunna

- **Edge AI:** AI som körs på en liten dator nära maskinen istället för i molnet.
- **Fail-safe:** när något går fel hamnar systemet i ett ofarligt läge.
- **Hotmodell:** en systematisk lista över hur ett system kan attackeras.

**Fundera på:** Vilka andra saker i din vardag borde fungera även utan internet? Hur gör till exempel en kartapp när du tappar täckning?
{: .ask}