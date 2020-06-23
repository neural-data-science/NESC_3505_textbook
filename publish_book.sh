#!/bin/zsh
jupyter-book clean .
jupyter-book build .
ghp-import -n -p -f ./_build/html
git add *
git commit -m'Built book'
git push origin master
