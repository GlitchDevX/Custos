FROM python:3.13-slim

COPY . .

RUN pip install --no-cache-dir uv
RUN uv sync

EXPOSE 5000

ENTRYPOINT ["uv", "run", "main.py", "--config=prd"]
