# NESC 3505 Textbook – Neural Data Science

Live site: https://neuraldatascience.io/

This repository contains the source for the Neural Data Science textbook. The site is built with Jupyter Book (via MyST) and deployed automatically to GitHub Pages.

## How publishing works

- Pushing to the `master` branch triggers a GitHub Actions workflow that:
  - Installs the MyST CLI and Python dependencies
  - Builds the HTML site
  - Deploys it to GitHub Pages

You don’t need to publish locally or commit build artifacts. The CI runner builds from source and uploads the site directly.

## Local development

Option A: Quick static build

1. Build the site
	- `myst build --html`
2. Open the result
	- `_build/html/index.html`

Option B: Dev server (live preview)

1. If you hit npm EACCES errors on macOS, fix npm cache permissions:
	- `sudo chown -R "$USER:$(id -gn)" ~/.npm`
	- `npm cache verify`
2. Start the dev server
	- `jupyter book start`

## Project configuration

- Site structure and config are defined in `myst.yml`
- Additional legacy settings may still exist in `_config.yml`; these are ignored by MyST once `myst.yml` is present
- The GitHub Actions workflow lives at `.github/workflows/deploy.yml`

## Troubleshooting

- If the Actions run fails at “Upload artifact”, check that the build step created `_build/html`.
- If the MyST CLI isn’t found locally, install it globally with `npm install -g mystmd` (Node.js ≥ 18 required).
- To preview just a single change locally, re-run `myst build --html` and refresh your browser on `_build/html/index.html`.

