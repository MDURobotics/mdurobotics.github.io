# Arbetsanteckningar

Status och att-göra-lista, så vi kan fortsätta där vi slutade.
Senast uppdaterad 2026-10-15. Se `README.md` för hur sajten är uppbyggd.

## Status

- Tillfällig förhandsvisning (sedan 2026-11-03): repot `johanhjorth/mdurobotics`
  → https://johanhjorth.github.io/mdurobotics/, byggs av `.github/workflows/pages.yml`.
  Pusha via SSH (gh-token saknar `workflow`-scope). Organisationen `mdurobotics` finns inte än.
- Publikationssidan har 130 poster från DiVA, handledda avhandlingar och
  `_data/publications_extra.yml`.

## Publicera (när organisationen finns)

1. Skapa organisationen `mdurobotics` på github.com (Settings → Organizations → New).
2. `gh repo create mdurobotics/mdurobotics.github.io --public --source . --push`
3. Repo → Settings → Pages: deploy from branch `main`, root.
4. Settings → Actions → General → Workflow permissions: "Read and write".
5. Kör "Update publications" manuellt under Actions en gång. Kontrollera att
   Pages byggs om efter Actions-commiten. Om inte: lägg till ett deploy-steg
   eller en PAT.

## Två språk (2026-11-05)

Hela sajten finns på engelska (standard) och svenska (`/sv/`), med en EN | SV-knapp
i menyraden. Se README.md, avsnittet "Two languages". Att granska:

- [ ] Engelska översättningar av projekt och evenemang (gjorda med Claude, behöver läsas
      av någon i gruppen).
- [ ] Engelska namn på evenemang: "Meet an engineer (Stör en ingenjör)", "Foundation year
      EXPO", "Study hall", "Industry advisory board". Rävarnas Revange och Högvarv är oöversatta.
- Gamla adresser har bytt språk: `/student-projects/x/` och `/events/x/` är nu engelska,
  de svenska ligger under `/sv/`. `/tillganglighet/` heter nu `/sv/tillganglighet/`.

## Text och innehåll som saknas (TODO i filerna)

- [ ] `index.html`: en eller två meningar om labbets mission
- [ ] `index.html`: gruppbild `assets/images/team.jpg` (bortkommenterad tills den finns)
- [ ] `_pages/about.md`: intro, historik, kontakt, lediga tjänster
- [ ] `_pages/research.md`: intro samt beskrivningar av AutoBike och AutoSail
- [ ] `_events/2027-01-slutdemonstration.md`: riktigt datum, tid, lokal och program
- [ ] Jonas Larsson har inget DiVA-id med publikationer

## Publikationer – öppna frågor

- [ ] **STRIDE (2026)**: kolla publikationstyp. Står som "Conference paper",
      men "Drones and Unmanned Systems" kan vara bok eller tidskrift.
- [ ] **BSN 2026-artiklarna**: författarna har bara initialer (O. Ågren, E. Åstrand).
- [ ] **Fråga Mikael** om myon- och μSR-fysikartiklarna (1995–2001, 17 st i
      hans Scholar-profil) är hans. De är inte med nu.
- [ ] **Fråga Mikael** om han handledde de här avhandlingarna. Scholar har
      dem, men DiVA anger Ylva Bäcklund eller ingen handledare:
      García Castaño 2006 (diva2:120542), Folke 2005 (diva2:121032),
      Ljungblad lic 2016 (diva2:881123), Lönnblad lic 2005 (diva2:120836).
      Om ja: be biblioteket lägga till honom som handledare i DiVA.
- [ ] **Be biblioteket rätta DiVA**:
  - diva2:120832 *Remote system for patient monitoring using Bluetooth*
    saknar Mikael som författare.
  - diva2:1669805 *Autonomous UAS-based agriculture applications* är inte
    kopplad till Carl.
  - diva2:713609 (Petrović): handledarens för- och efternamn är omkastade.
- [ ] Registrera 2026-artiklarna i DiVA. Skriptet säger sedan vilka poster
      som kan tas bort ur `publications_extra.yml`.
- Medvetet uteslutet: DiVA-manuskript (5 st), status "Submitted"
  (*Decentralised Multi-Robot Path Planning…*), studentuppsatser, KTH:s
  proteinartiklar (annan person), samt "Research Planning Assignment 3",
  "Induction Machine Speed Control" och "Student report-autobike 2018".
- Google Scholar har inget API och får inte skrapas. Kontrollera luckor
  manuellt med `scripts/compare_scholar.py` (senaste listan finns i
  `notes/scholar-2026-10.txt`). OpenAlex utvärderades men blandar ihop
  personer med samma namn, så det används inte.

## Designfrågor

- [ ] Ska rubrikerna i Sense/Plan/Act-rutorna också vara orange (som i hero)?

## Idéer för senare

- Forskningsprojekt som egen samling under `/projects/`
- Import av BibTeX-export från Scholar
- Roll för Johan: står som "Lecturer" (adjunkt). Ändra i `_data/people.yml` vid behov.

## Videor från studentgrupperna (väntar, beslut 2026-11-03)

- Bädda **inte** in LinkedIn direkt: sätter cookies utan samtycke (GDPR) och saknar undertexter (WCAG 1.2.2).
- Plan: be grupperna om originalfiler → MDU Play (play.mdu.se) eller YouTube via `youtube-nocookie` (`_includes/video.html`).
  Alternativ: "klicka för att ladda"-ruta för LinkedIn-inlägg.
- Tal i videon kräver undertexter. Utan tal räcker en textbeskrivning.

## Tillgänglighet (lag 2018:1937, WCAG 2.2 AA)

- Redogörelse på `/tillganglighet/`. Uppdatera datum och brister vid ändringar.
- `accessibility_contact` i `_config.yml` måste fyllas i innan sajten blir officiell.
- Testa: axe-core via puppeteer mot localhost (alla sidor, ljust + mörkt), reflow 320 px, tangentbord.
- MDU-orange `#ff4800` bara till dekoration/stor text; `--signal-strong` bakom liten vit text, `--signal-on-dark` på grönt.

