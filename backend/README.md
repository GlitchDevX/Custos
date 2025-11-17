# Custos Backend
The custos backend is a python based API using Flask.

## Local Setup
You need to have ``uv`` installed to work in the backend part of this project.

Then to start the backend locally.
```bash
# install dependencies (once)
uv sync

# start backend
uv run main.py
```

## Update Documentation
To update the swagger config and see the changes in the ui start the frontend with this command.
```bash
pn run dev:docs
```
