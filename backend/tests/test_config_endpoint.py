import json
import os
from os.path import isfile, join

import pytest

from app.config_reader import reload_readers_with_namespace

API_PATH= "/config/"
CONFIG_DIR= "config"

def get_all_configs():
    all_configs = [join(CONFIG_DIR,f) for f in os.listdir(CONFIG_DIR) if isfile(join(CONFIG_DIR, f))]

    config_content: list[tuple[str, str]] = []
    for config_path in all_configs:
        with open(config_path, "r") as file:
            config_content.append((config_path, file.read()))

    return config_content

def reset_config_files(all_configs: list[tuple[str, str]]):
    for config_path, content in all_configs:
        with open(config_path, "w") as file:
            file.write(content)
        reload_readers_with_namespace(config_path.split("/")[1].split(".")[0])

@pytest.fixture(autouse=True)
def around_tests():
    conf_before_test = get_all_configs()
    yield
    reset_config_files(conf_before_test)

# set
def test_should_throw_bad_request_on_wrong_body(client):
    response = client.put(API_PATH, json={"WRONG_FIELD": "WRONG_VALUE"})
    assert response.status_code == 400

def test_should_modify_test_config(client):
    mail_conf_path = f"{CONFIG_DIR}/mail_validation.json"

    response = client.put(API_PATH, json={"namespace": "mail_validation", "content": {"file": "was_modified"}})

    assert response.status_code == 200
    assert response.json["code"] == "OK"
    with open(mail_conf_path) as file:
        assert file.read() == json.dumps({"file": "was_modified"}, indent=4)

def test_should_get_namespace_not_exists(client):
    response = client.put(API_PATH, json={"namespace": "non_existent_file", "content": {"not": "relevant"}})
    assert response.status_code == 404
    assert response.json["error"] == "NAMESPACE_NOT_FOUND"

# get
def test_should_get_config_in_namespace(client):
    metrics_conf: str
    with open(f"{CONFIG_DIR}/metrics.json") as file:
        metrics_conf = json.loads(file.read())

    response = client.get(API_PATH + "?namespace=metrics")

    assert response.status_code == 200
    assert response.json == metrics_conf

def test_should_get_config_not_found(client):
    response = client.get(API_PATH + "?namespace=non_existent_namespace")
    assert response.status_code == 404
    assert response.json["error"] == "NAMESPACE_NOT_FOUND"