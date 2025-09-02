FROM python:3.13-slim

RUN pip install --no-cache-dir uv

COPY pyproject.toml uv.lock ./
RUN uv sync

COPY . .

EXPOSE 5000

ENTRYPOINT ["uv", "run", "main.py", "--config=prd"]
