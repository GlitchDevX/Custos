def test_should_throw_bad_request_on_wrong_body(client):
    response = client.post("/validate-mail/", json={"mal": "test"})
    assert response.status_code == 400

def test_should_return_ok_status_code(client):
    response = client.post("/validate-mail/", json={"mail": "test@gmail.com"})
    assert response.status_code == 200
    assert response.json["code"] == "OK"

def test_should_get_invalid_format(client):
    response = client.post("/validate-mail/", json={"mail": "invalid-mail-format"})
    assert response.status_code == 400
    assert response.json["code"] == "FORMAT_INVALID"

def test_should_get_disposable_mail(client):
    response = client.post("/validate-mail/", json={"mail": "test@muellmail.com"})
    assert response.status_code == 400
    assert response.json["code"] == "DISPOSABLE"

def test_should_get_no_mailserver(client):
    response = client.post("/validate-mail/", json={"mail": "test@1.1.1.1"}) # 1.1.1.1 has no MX-Records set
    assert response.status_code == 400
    assert response.json["code"] == "NO_MAILSERVER"
