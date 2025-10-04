# Custos
Custos is a User Content Moderation System which aims to prevent spam and helps to moderate users.

Custos has a Web UI and API Backend. The Web UI to manage the application, configure the endpoints and experiment.
And the API where user content can be validated and checked in real time either using effective rulesets or the detoxify neuronal network.

The tech stack is `Python` with `Flask` for the backend and `Nuxt` using the `Nuxt UI` component library for the frontend.

## Installation
You can run Custos purely using docker compose.

For this simply put this text into a file named `docker-compose.yml`.
```yml
services:
  custos:
    image: glitchdevx/custos:latest
    restart: always
    ports:
      - "127.0.0.1:3060:3060"
  custos-ui:
    image: glitchdevx/custos-ui:latest
    restart: always
    depends_on:
      - custos
    ports:
      - "127.0.0.1:3070:80"
```

> [!TIP]
> If you want to run Custos headless simply remove the custos-ui part of the file.

Then to start it run `docker compose up -d`.

And to stop it `docker compose down`.

### Configuration
You can configure Custos mainly in two ways, either by directly editing the config files located 
inside the ``custos-config/`` dir, or by using the API per HTTP call or the Web-UI.


### Metrics
Custos has a Prometheus exporter, meaning you can scrape the metrics from custos using Prometheus and them use them in a grafana dashboard.

To let Prometheus scrape Custos you can add this simple config to `/etc/prometheus/prometheus.yml`
```yml
scrape_configs:
  - job_name: 'custos'
    static_configs:
      - targets: ['localhost:3060']  # assuming your Custos instance is running on port 3060
```

This data could then be used in a Grafana dashboard, you can use [this dashboard](./frontend/app/assets/data/metric-configs/grafana-dashboard.json) as a base.

## Local Development
To develop locally, see the individual readmes in the [frontend](frontend/README.md#local-setup) and [backend](frontend/README.md#local-setup).


---
<br>
<div align="center">
    <img src="frontend/public/favicon.png" width=200>
    <br>
    <strong>Flag, Manage, Protect with Custos</strong>
</div>
