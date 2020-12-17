#!/usr/bin/env bash
# -*- coding: utf-8 -*-

# Wrapper to run npm command to invoke tools for compiling assets
# Requires being run from yarn or with purgecss, sass (dart) being globally installed
# under LGPL v3.0 @ Cobalt <cobalt.rocks> (see LICENSE)

echo "Descending into theme/static/"
cd theme/static/

npm run production-compile

echo "Done. Ascending back"
cd ../..
