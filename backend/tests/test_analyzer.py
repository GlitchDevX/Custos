path = "/analyze/"

def test_should_throw_bad_request_on_wrong_body(client):
    response = client.post(path, json={"invalid": "body"})
    assert response.status_code == 400

def test_should_detect_no_toxicity(client):
    response = client.post(path, json={"content": "Some acceptable content"})
    assert response.status_code == 200
    assert response.json["labels"] == []

def test_should_detect_toxicity(client):
    response = client.post(path, json={"content": "Fuck you"})
    assert response.status_code == 200
    assert response.json["labels"] == ["toxicity", "obscene"]

def test_should_detect_sexual_explicit(client):
    response = client.post(path, json={"content": "Lick my balls"})
    assert response.status_code == 200
    assert response.json["labels"] == ["toxicity", "obscene", "sexual_explicit"]
