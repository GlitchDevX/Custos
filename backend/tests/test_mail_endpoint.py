def test_should_throw_bad_request_on_wrong_body(client):
    response = client.post("/validate-mail/", json={"mal": "test"})
    assert response.status_code == 400