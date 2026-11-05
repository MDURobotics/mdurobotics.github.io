---
ref: accessibility
title: "Tillgänglighetsredogörelse"
label: "Tillgänglighet"
permalink: /sv/tillganglighet/
lang: "sv"
---

Mälardalens universitet står bakom den här webbplatsen. Vi vill att så många
som möjligt ska kunna använda den. Här beskriver vi hur webbplatsen uppfyller
lagen (2018:1937) om tillgänglighet till digital offentlig service, vilka
tillgänglighetsproblem vi känner till och hur du kan rapportera brister så att
vi kan åtgärda dem.

## Hur tillgänglig är webbplatsen?

Vi vet att delar av webbplatsen inte är helt tillgängliga. Se avsnittet om
innehåll som inte är tillgängligt nedan.

## Vad kan du göra om du inte kan använda delar av webbplatsen?

Om du behöver innehåll från webbplatsen i ett annat format kan du kontakta oss.
{% if site.accessibility_contact != "" %}Mejla
[{{ site.accessibility_contact }}](mailto:{{ site.accessibility_contact }}).{% endif %}

## Rapportera brister i webbplatsens tillgänglighet

Vi strävar hela tiden efter att förbättra webbplatsens tillgänglighet. Om du
upptäcker problem som inte beskrivs på den här sidan, eller om du anser att vi
inte uppfyller lagens krav, får du gärna meddela oss så att vi vet att problemet
finns.{% if site.accessibility_contact != "" %} Mejla
[{{ site.accessibility_contact }}](mailto:{{ site.accessibility_contact }}).{% endif %}

## Tillsyn

Myndigheten för digital förvaltning (Digg) ansvarar för tillsynen över lagen
om tillgänglighet till digital offentlig service. Om du inte är nöjd med hur
vi hanterar dina synpunkter kan du
[kontakta Digg och påtala det](https://www.digg.se/tdosanmalan).

## Teknisk information om webbplatsens tillgänglighet

Webbplatsen är delvis förenlig med lagen om tillgänglighet till digital
offentlig service, på grund av de brister som beskrivs nedan. Vi bedömer
webbplatsen mot WCAG 2.2 på nivå AA, som omfattar kraven i WCAG 2.1 AA och
den europeiska standarden EN 301 549.

## Innehåll som inte är tillgängligt

### Bristande förenlighet med lagkraven

- **Videor.** Filmerna om AutoBike och AutoSail visas via YouTube. Vi har ännu
  inte kontrollerat att de har korrekta undertexter eller ett textalternativ
  som beskriver innehållet (WCAG 1.2.1, 1.2.2 och 1.2.5). Vi arbetar med att
  åtgärda detta.
- **Publikationslistan.** Listan hämtas automatiskt från DiVA. Titlar på ett annat
  språk än sidans är inte märkta med rätt språk, så en skärmläsare kan uttala
  dem fel (WCAG 3.1.2).

## Hur vi testat webbplatsen

Vi har gjort en självskattning (intern testning) av webbplatsen, med både
automatiska verktyg (axe-core) och manuell granskning av färgkontraster,
tangentbordsnavigering, språkmärkning, rubrikstruktur och visning på smala
skärmar.

Senaste bedömningen gjordes den 3 november 2026.

Redogörelsen uppdaterades senast den 3 november 2026.
