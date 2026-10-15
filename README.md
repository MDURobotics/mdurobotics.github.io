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
| Menu | `_data/navigation.yml` |
| People (About page, publication matching) | `_data/people.yml` |
| Student projects (Swedish) | `_projects/*.md`, list page `_pages/student-projects.html` |
| Events | `_events/YYYY-MM-name.md`, list page `_pages/events.md` |
| Research | `_pages/research.md` |
| Layouts / includes | `_layouts/`, `_includes/` (`loop.html`, `video.html`, `event-list.html`, `project-card.html`) |
| Styles (colour tokens, dark mode) | `assets/css/site.css` |

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
