FROM python:3.11-slim

WORKDIR /app

COPY /backend .

RUN pip install --no-cache-dir uv
RUN uv sync

EXPOSE 5000

ENTRYPOINT ["uv", "run", "main.py", "--config=prd"]
