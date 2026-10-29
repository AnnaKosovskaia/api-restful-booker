def test_delete_booking(booking_id, booking_client, auth_headers):
    response = booking_client.delete_booking(
        booking_id, auth_headers
    )
    print(booking_id)
    assert response.status_code == 201

    response_after = booking_client.get_booking(booking_id)
    assert response_after.status_code == 404