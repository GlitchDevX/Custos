# Custos Backend
The custos backend is a python based API using Flask.

It is connected to the ``MySQL`` database which is recommended to start via docker composse.
To only start the db execute
```bash
# execute in project root
docker compose up db -d
```

## Local Setup
You need to have ``uv`` installed to work in the backend part of this project.

Then to start the backend locally.
```bash
# install dependencies (once)
uv sync

# start backend
uv run main.py
```