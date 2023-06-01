#!/bin/sh
FILE=".env"
if test -f "$FILE"; then
  echo "Found an environment file"
  source "$FILE"
fi
python3 src/civicsgpt/main.py "$@"
