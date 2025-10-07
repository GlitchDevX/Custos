#!/bin/bash

# this script is required, because when docker mounts the config volume it won't sync the files that are already present.

if [ -d "default_config" ]; then
  echo "Initializing docker config volume"
  mv default_config/* config/
  rm -rf default_config
fi

uv run main.py --config prd
