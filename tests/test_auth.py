def test_user_registration(client):
    response = client.post("/users/", json={"email": "test@example.com", "password": "secret"})
    assert response.status_code == 200
    assert response.json()["email"] == "test@example.com"
