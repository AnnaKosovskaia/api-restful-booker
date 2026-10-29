def test_get_booking_ids(booking_ids_response):
    assert booking_ids_response.status_code == 200

    data = booking_ids_response.json()
    assert isinstance(data, list)
    assert len(data) > 0

    for booking in data:
        assert "bookingid" in booking
        assert isinstance(booking["bookingid"], int)

