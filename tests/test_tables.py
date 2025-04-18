def test_create_table(client):
    response = client.post("/tables/", json={
        "name": "Table 1",
        "seats": 4,
        "location": "зал у окна"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Table 1"
    assert data["seats"] == 4
    assert data["location"] == "зал у окна"
def test_get_tables(client):
    response = client.get("/tables/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert any(t["name"] == "Table 1" for t in data)