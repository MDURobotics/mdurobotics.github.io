---
title: "KARIS: humanoid robot i fabriken"
excerpt: "Kan en människoliknande robot göra ett vanligt fabriksjobb utan att man bygger om fabriken?"
order: 3
year: 2026
subjects: [Programmering, Matematik, Fysik, Teknik]
facts:
  - label: "Robot"
    value: "Unitree G1, en humanoid robot med händer som kan greppa"
  - label: "Partner"
    value: "Volvo"
  - label: "Mål"
    value: "Plocka rätt delar till en monteringsbricka, både på ett tomt och ett stökigt bord"
updates:
  - date: 2026-10-30
    text: "Från att följa föremål till att greppa dem. Händer formade som en människas är svårare att plocka med än man tror."
    url: "https://www.linkedin.com/feed/update/urn:li:activity:7521917906683686913/"
  - date: 2026-10-29
    text: "Objektigenkänning och rörelseplanering fungerar. Att koppla ihop dem med ett pålitligt grepp är den största utmaningen."
    url: "https://www.linkedin.com/feed/update/urn:li:activity:7521516263634923520/"
  - date: 2026-09-14
    text: "Gruppen presenterade KARIS, en humanoid robot för plockning i industrin, och hur den ska testas i både verklig fabriksmiljö och i labbet."
    url: "https://www.linkedin.com/feed/update/urn:li:activity:7505197405500510208/"
---

## Problemet

Fabriker är byggda för människor: hyllor i rätt höjd, verktyg för händer, gångar för fötter. En vanlig industrirobot kräver att man bygger om arbetsplatsen runt den. En humanoid skulle i teorin kunna ta över en människas plats direkt. Jobbet gruppen testar kallas *kitting*, att plocka ihop de delar som behövs för ett monteringssteg och lägga dem på rätt plats i en bricka. Det är lite som att packa en matkasse efter ett recept.

## Så funkar den

- **Känna** Robotens kamera ser bordet. AI känner igen vilka delar som ligger där och om någon del är okänd.
- **Planera** En annan AI-modell räknar ut exakt var varje del ligger och hur den är vriden i alla riktningar. Sedan räknar programmet ut hur varje led i armen ska vinklas för att handen ska hamna rätt, utan att krocka med något.
- **Agera** Handen greppar delen, armen flyttar den och lägger den i rätt fack i brickan. Här kommer fysiken in: handen måste trycka så hårt att friktionen håller kvar delen, men inte så hårt att den skadas. Och när armen accelererar påverkar både delens och armens egen massa hur mycket kraft motorerna behöver.
{: .sta}

**Varför är det svårt?** Förra året klarade ett examensarbete samma uppgift, men långsamt och inte varje gång. I år låter gruppen AI sköta det roboten *ser*, men programmerar själva rörelserna mer exakt. Målet på längre sikt är att roboten ska vara ungefär lika snabb som en människa.
{: .callout}

## Ord att kunna

- **Humanoid:** en robot byggd med människokroppen som förebild.
- **6D-position:** var ett föremål är (x, y, z) och hur det är vridet (tre vinklar).
- **Invers kinematik:** att räkna baklänges från var handen ska vara till hur varje led ska vinklas.
- **Dynamik:** läran om hur krafter påverkar rörelse, till exempel hur mycket motorerna måste orka för att flytta armen snabbt men mjukt.

**Fundera på:** Är det smartare att bygga robotar som liknar människor, eller att bygga om arbetsplatser för robotar? Vad talar för och emot?
{: .ask}