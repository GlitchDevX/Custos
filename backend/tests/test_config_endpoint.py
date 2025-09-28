import json
import time
import pytest


API_PATH= "/config/"
CONFIG_PATH= "config/test.json"
base_content = {
    "field1": "before saving",
    "field2": "blabla"
}

def reset_file():
    with open(CONFIG_PATH, "w") as file:
        file.write(json.dumps(base_content))

@pytest.fixture(autouse=True)
def around_tests():
    reset_file()
    yield
    reset_file()

# set
def test_should_throw_bad_request_on_wrong_body(client):
    response = client.put(API_PATH, json={"WRONG_FIELD": "WRONG_VALUE"})
    assert response.status_code == 400

def test_should_modify_test_config(client):
    with open(CONFIG_PATH) as file:
        assert file.read() == json.dumps(base_content)
    response = client.put(API_PATH, json={"namespace": "test", "content": {"file": "was_modified"}})
    assert response.status_code == 200
    assert response.json["code"] == "OK"
    with open(CONFIG_PATH) as file:
        assert file.read() == json.dumps({"file": "was_modified"}, indent=4)

def test_should_get_namespace_not_exists(client):
    response = client.put(API_PATH, json={"namespace": "non_existent_file", "content": {"not": "relevant"}})
    assert response.status_code == 404
    assert response.json["code"] == "NAMESPACE_NOT_FOUND"
    with open(CONFIG_PATH) as file:
        assert file.read() == json.dumps(base_content)

# get
def test_should_get_config_in_namespace(client):
    response = client.get(API_PATH + "?namespace=test")
    assert response.status_code == 200
    assert response.json == base_content

def test_should_get_config_not_found(client):
    response = client.get(API_PATH + "?namespace=non_existent_namespace")
    assert response.status_code == 404
    assert response.json == {}