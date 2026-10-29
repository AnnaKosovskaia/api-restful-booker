import json
from jsonschema import validate
from schemas.booking_schema import BOOKING_SCHEMA
from data.booking_data import build_booking_payload

def test_create_booking(booking_client):
    payload = build_booking_payload()
    response = booking_client.create_booking(payload)
    assert response.status_code == 200
    data = response.json()
    print(json.dumps(data, indent=4))

    assert isinstance(data["bookingid"], int)
    validate(
        instance=data["booking"],
        schema=BOOKING_SCHEMA
    )

    assert data["booking"] == payload
