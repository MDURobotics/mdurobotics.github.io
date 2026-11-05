# mdurobotics.github.io

Website of the robotics group at Mälardalen University (MDU). Jekyll on
GitHub Pages, custom theme in MDU colours (no remote theme).

## Preview locally

    ./serve.sh        # Jekyll in Docker, http://localhost:4000, live reload

Changes to `_config.yml` need a restart: `docker stop mdurobotics-preview`,
then `./serve.sh` again.

## Where things live

| What | File |
|---|---|
| Menu (one list per language) | `_data/navigation.yml` |
| Interface text (buttons, labels, month names) | `_data/i18n.yml` |
| People (About page, publication matching) | `_data/people.yml` |
| Pages | `_pages/*` (English), `_pages/sv/*` (Swedish) |
| Student projects | `_projects/en/*.md`, `_projects/sv/*.md` |
| Events | `_events/en/YYYY-MM-DD-name.md`, `_events/sv/…` |
| Layouts / includes | `_layouts/`, `_includes/` (`home.html`, `student-projects.html`, `publications.html`, `event-list.html`, `translation.html`, …) |
| Styles (colour tokens, dark mode) | `assets/css/site.css` |

## Two languages

The whole site exists in English (default, `/…`) and Swedish (`/sv/…`).
The EN | SV switch in the top bar goes to the same page in the other language.

- **Projects and events:** write each one twice, with the same file name in
  `en/` and `sv/`. That is how the two are linked. URLs and `lang` come from
  `_config.yml`.
- **Pages:** the English and Swedish file share a `ref:` in the front matter
  and have their own `permalink:` (Swedish under `/sv/`).
- **Interface text:** add new strings to both `en` and `sv` in
  `_data/i18n.yml`.
- If a translation is missing, the switch goes to the other language's
  home page.

MDU colours: green `#00352D`, orange `#FF4800`, sand `#F5E0C8`, cream `#FCF4EB`.

## Publications

`_data/publications.json` is generated, do not edit it by hand:

    python3 scripts/fetch_publications.py

It pulls from MDU's DiVA: everything authored by the DiVA person ids in
`people.yml`, plus PhD/licentiate theses supervised by members. Missing or
mis-linked publications go in `_data/publications_extra.yml`. The GitHub
Action `.github/workflows/publications.yml` re-runs it weekly and commits
the result.

To check a Google Scholar profile for gaps, save its list as `year|title`
lines and run `python3 scripts/compare_scholar.py <file>`.
