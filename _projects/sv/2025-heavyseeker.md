---
title: "HeavySeeker: roboten som hittar i skogen"
excerpt: "Programvara och sensorer som låter en robotbil köra själv mellan punkter i skogen, även när GPS:en är dålig."
order: 4
year: 2025
subjects: [Programmering, Matematik, Teknik]
facts:
  - label: "Robot"
    value: "Clearpath Husky, en färdig robotbil som gruppen byggde om med nya sensorer"
  - label: "Hemvist"
    value: "SLaRC, MDU:s forskningscenter för markbaserad robotik"
  - label: "Resultat"
    value: "Roboten körde själv mellan utvalda punkter i skogsmiljö och kunde fjärrstyras med video"
---

## Problemet

I skogen är det svårt för en robot att veta var den är. Träden skymmer GPS-signalen, marken är ojämn och saker kan röra sig. Gruppen skulle ge robotbilen sinnen och programvara så att den kan köra själv mellan punkter som en människa har valt, och kunna styras på distans när den är utom synhåll.

## Så funkar den

- **Känna** En LiDAR skannar omgivningen med laser och en djupkamera ser hinder. En extra noggrann GPS (RTK) anger position, och givare på hjulen mäter hur långt bilen har kört.
- **Planera** Ett Kalmanfilter väger ihop alla sensorer till en gissning om var roboten är, även när GPS:en är dålig. Navigationsprogrammet Nav2 ritar upp en karta över hinder och räknar ut en väg runt dem.
- **Agera** Roboten kör till nästa punkt. En människa kan när som helst ta över och styra med hjälp av video från roboten.
{: .sta}

## Hur gick det?

Roboten testades både i simulering och ute i skogsmiljö. Den kunde fjärrstyras och köra själv mellan punkter, trots att GPS-signalen ibland var svag. Programvaran är byggd i delar som kan testas var för sig, så att andra kan bygga vidare på den.

## Ord att kunna

- **LiDAR:** en sensor som mäter avstånd med laserpulser, ungefär som radar fast med ljus.
- **Kalmanfilter:** en matematisk metod som väger ihop osäkra mätningar till en bättre gissning.
- **Waypoint:** en punkt som roboten ska ta sig till på vägen.

**Fundera på:** Om GPS:en säger en sak och hjulen säger en annan, vem ska roboten lita på?
{: .ask}
