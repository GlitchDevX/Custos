import argparse
import atexit

from app.app import FlaskApplication
from app.config.flask_config import FlaskDevConfig, FlaskTstConfig, FlaskPrdConfig
from app.config.app_config import DevConfig, PrdConfig, TstConfig
from app.config import app_config
from app.utils.scheduler_wrapper import scheduler

flask_configs = {
    "dev": FlaskDevConfig,
    "tst": FlaskTstConfig,
    "prd": FlaskPrdConfig
}
app_configs = {
    "dev": DevConfig,
    "tst": TstConfig,
    "prd": PrdConfig,
}

atexit.register(lambda: scheduler.shutdown())

def run(config):
    FlaskApplication(config)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run the Flask application.')
    parser.add_argument('--config', type=str, choices=['dev', 'tst', 'prd'],
                        default='dev', help='Choose the configuration to use')

    args = parser.parse_args()

    app_config.config = app_configs.get(args.config)

    run(flask_configs.get(args.config))