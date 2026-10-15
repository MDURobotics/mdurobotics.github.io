#!/bin/sh
# Local preview at http://localhost:4000 (Jekyll in Docker, no local Ruby needed)
cd "$(dirname "$0")"
exec docker run --rm --name mdurobotics-preview \
  --user "$(id -u):$(id -g)" -e HOME=/tmp \
  -p 4000:4000 -p 35729:35729 \
  -v "$PWD":/srv/site -w /srv/site \
  -e BUNDLE_PATH=/srv/site/vendor/bundle \
  ruby:3.3 sh -c "bundle install --quiet && bundle exec jekyll serve --host 0.0.0.0 --livereload --force_polling"
