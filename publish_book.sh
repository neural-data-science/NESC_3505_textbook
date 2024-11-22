#!/bin/zsh

export PYDEVD_DISABLE_FILE_VALIDATION=1

jupyter-book clean .

jupyter-book build .

ghp-import -n -p -f ./_build/html --cname='neuraldatascience.io'

git add *
git commit -m'Built book'
git push origin master
