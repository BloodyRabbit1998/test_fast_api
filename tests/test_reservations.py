import datetime

def test_reservation_conflict(client):
    now = datetime.now().isoformat()
    response = client.post("/reservations/", json={
        "customer_name": "Пётр",
        "table_id": 1,
        "reservation_time": now,  # пересекается с предыдущей бронью
        "duration_minutes": 30
    })
    assert response.status_code == 400
    assert "conflict" in response.json()["detail"].lower()