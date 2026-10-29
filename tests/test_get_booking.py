from jsonschema import validate
from schemas.booking_schema import BOOKING_SCHEMA

def test_get_booking(booking_id, booking_client):
    response = booking_client.get_booking(booking_id)
    assert response.status_code == 200
    data = response.json()
    print(data)

    validate(
        instance=data,
        schema=BOOKING_SCHEMA
    )
