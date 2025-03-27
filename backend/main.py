import argparse
from app import create_app
from app.config import DevelopmentConfig, TestingConfig, ProductionConfig

configs = {
    "dev": DevelopmentConfig,
    "tst": TestingConfig,
    "prd": ProductionConfig
}

def run(config):
    app = create_app(config)
    app.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run the Flask application.')
    parser.add_argument('--config', type=str, choices=['dev', 'tst', 'prd'],
                        default='dev', help='Choose the configuration to use')

    args = parser.parse_args()
    run(configs.get(args.config))