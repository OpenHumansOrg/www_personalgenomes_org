#!/bin/bash
set -e # exit with nonzero exit code if anything fails

# Installing via gem file to use Netlify's Cache
gem install jekyll

# jekyll build
mv _redirects _site
