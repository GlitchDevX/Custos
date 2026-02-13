FROM python:3.13-slim

RUN pip install --no-cache-dir uv

COPY pyproject.toml uv.lock ./
RUN uv sync

COPY . .
RUN mv config/ default_config/

EXPOSE 3060

ENTRYPOINT ["./start_production.sh"]
