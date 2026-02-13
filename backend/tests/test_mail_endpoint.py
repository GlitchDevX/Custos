path = "/mail/"

def test_should_throw_bad_request_on_wrong_body(client):
    response = client.post(path, json={"mal": "test"})
    assert response.status_code == 400

def test_should_return_ok_status_code(client):
    response = client.post(path, json={"mail": "187gurkenglas@gmail.com"})
    assert response.status_code == 200
    assert response.json["code"] == "OK"

def test_should_get_invalid_format(client):
    response = client.post(path, json={"mail": "invalid-mail-format"})
    assert response.status_code == 200
    assert response.json["code"] == "FORMAT_INVALID"

def test_should_get_disposable_mail(client):
    response = client.post(path, json={"mail": "test@muellmail.com"})
    assert response.status_code == 200
    assert response.json["code"] == "DISPOSABLE"

def test_should_get_no_mailserver(client):
    response = client.post(path, json={"mail": "test@one.one.one.one"}) # 1.1.1.1 has no MX-Records set
    assert response.status_code == 200
    assert response.json["code"] == "NO_SERVER"
