def test_ping(booking_client):
    response = booking_client.ping()
    assert response.status_code == 201

    print("METHOD:", response.request.method)
    print("URL:", response.request.url)
    print("STATUS:", response.status_code)
    print("BODY:", response.text)