path = "/content/"

def test_should_throw_bad_request_on_wrong_body(client):
    response = client.post(path, json={"invalid": "body"})
    assert response.status_code == 400

def test_should_detect_nothing(client):
    response = client.post(path, json={"content": "Some acceptable content"})
    assert response.status_code == 200
    assert response.json["flags"] == []
    assert response.json["censored_content"] == "Some acceptable content"

def test_should_detect_blocked_word(client):
    response = client.post(path, json={"content": "Fuck you"})
    assert response.status_code == 200
    assert response.json["flags"] == ["blocked_word"]
    assert response.json["censored_content"] == "**** you"

def test_should_detect_url(client):
    response = client.post(path, json={"content": "Visit sapphire-games.com"})
    assert response.status_code == 200
    assert response.json["flags"] == ["contains_url"]
    assert response.json["censored_content"] == "Visit ******************"

def test_should_detect_both(client):
    response = client.post(path, json={"content": "Fuck! Visit sapphire-games.com"})
    assert response.status_code == 200
    assert response.json["flags"].sort() == ["blocked_word", "contains_url"].sort()
    assert response.json["censored_content"] == "****! Visit ******************"
