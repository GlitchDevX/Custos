#!/bin/bash

nohup uv run main.py --config prd &
p_id=$!

SECONDS=0
until curl -s http://localhost:3060/swagger.json > /dev/null
do
  if (( SECONDS > 60 ))
  then
      echo "Timed out at $SECONDS..."
      exit 1
  fi

  echo "API not started. Waiting..."
  sleep 1
done

curl -s http://localhost:3060/swagger.json > swagger.json
echo "Extracted swagger.json"

kill $p_id
