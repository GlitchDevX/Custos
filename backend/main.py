import argparse
from app.app import FlaskApplication
from app.config.flask_config import FlaskDevConfig, FlaskTstConfig, FlaskPrdConfig

flask_configs = {
    "dev": FlaskDevConfig,
    "tst": FlaskTstConfig,
    "prd": FlaskPrdConfig
}

def run(config):
    FlaskApplication(config)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run the Flask application.')
    parser.add_argument('--config', type=str, choices=['dev', 'tst', 'prd'],
                        default='dev', help='Choose the configuration to use')

    args = parser.parse_args()

    run(flask_configs.get(args.config))