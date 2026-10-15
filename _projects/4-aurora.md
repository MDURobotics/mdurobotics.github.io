---
title: "AURORA: armen som härmar dig"
excerpt: "En robotarm för rehabiliteringsforskning som ska lära sig röra sig som en människa genom att titta på en."
order: 4
subjects: [Biologi, Fysik, Programmering, Teknik]
facts:
  - label: "Robot"
    value: "LIMB, en 3D-printad robotarm med hand, utvecklad på MDU"
  - label: "Bygger på"
    value: "Flera tidigare studentprojekt"
  - label: "Mål"
    value: "Spela in en människas armrörelse och låta roboten göra om den"
---

## Problemet

Robotar som ska jobba nära människor, till exempel inom rehabilitering eller som proteser, måste röra sig mjukt, säkert och förutsägbart. LIMB-armen finns redan men har problem: axeln blir sned, motorerna är för svaga i vissa lägen och vinkelsensorerna visar fel efter en stund. Gruppen ska först göra armen pålitlig och sedan lära den att härma människor.

## Så funkar den

- **Känna** Människan som visar rörelsen bär sensorer. EMG-sensorer läser de små elektriska signalerna i underarmens muskler och märker när du vill knyta handen. Rörelsesensorer (samma typ som i din mobil) och en kamera följer armens rörelse.
- **Planera** Datorn slår ihop alla sensorers data till en bild av rörelsen och gör om den till en mjuk bana för robotarmen. Rörelsen testas först i en simulering.
- **Agera** Robotarmen gör samma rörelse. Den har nödstopp och åker hem till startläget om strömmen går.
{: .sta}

**Visste du?** Människor rör armen på ett förvånansvärt mjukt sätt: hastigheten ökar och minskar jämnt utan ryck. Forskare har beskrivit det matematiskt, och gruppen använder det för att mäta hur mänsklig robotens rörelse ser ut. Motorerna ska dessutom vara tysta, eftersom armen i framtiden kan styras med hjärnsignaler och då stör ljud mätningarna.
{: .callout}

## Ord att kunna

- **EMG:** mätning av musklernas elektriska aktivitet via sensorer på huden.
- **Sensorfusion:** att kombinera flera sensorer så att de täcker upp för varandras svagheter.
- **Inlärning genom demonstration:** roboten lär sig genom att se en människa göra något istället för att programmeras steg för steg.

**Fundera på:** Din mobil vet ungefär hur du håller den. Hur tror du att den vet det, och varför räcker inte en enda sensor för att följa en hel arm?
{: .ask}