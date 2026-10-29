import json
from jsonschema import validate
from schemas.booking_schema import BOOKING_SCHEMA
from data.booking_data import build_booking_payload

def test_update_booking(booking_id, booking_client, auth_headers):
    payload = build_booking_payload()
    response = booking_client.update_booking(
        booking_id, payload, auth_headers
    )
    assert response.status_code == 200
    data = response.json()
    print(json.dumps(data, indent=4))

    response_after = booking_client.get_booking_ids()
    assert response_after.status_code == 200
    ids_after = response_after.json()
    assert len(ids_after) > 1

    response_updated = booking_client.get_booking(booking_id)
    assert response_updated.status_code == 200
    assert response_updated.json() == payload

    validate(
        instance=data,
        schema=BOOKING_SCHEMA
    )