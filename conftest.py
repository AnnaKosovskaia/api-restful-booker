import os
import pytest
import requests

from api.booking_client import BookingClient
from api.auth_client import AuthClient

from dotenv import load_dotenv

from data.booking_data import build_booking_payload

load_dotenv()


@pytest.fixture(scope="session")
def base_url():
    return os.getenv("BASE_URL")

@pytest.fixture(scope="session")
def credentials():
    return {
        "username": os.getenv("API_USERNAME"),
        "password": os.getenv("API_PASSWORD"),
    }

@pytest.fixture(scope="session")
def token(base_url, credentials):
    session = requests.Session()
    response = AuthClient(base_url, session).login(credentials)
    assert response.status_code == 200
    data = response.json()
    return data["token"]

@pytest.fixture(scope="session")
def auth_client(base_url):
    session = requests.Session()
    yield AuthClient(base_url, session)
    session.close()

@pytest.fixture(scope="session")
def auth_headers(token):
    return {
        # "Authorization": f"Bearer {token}"
        "Cookie": f"token={token}"
    }

@pytest.fixture
def booking_ids(booking_ids_response):
    assert booking_ids_response.status_code == 200
    data = booking_ids_response.json()
    assert len(data) > 0
    return data

@pytest.fixture
def booking_ids_response(booking_client):
    return booking_client.get_booking_ids()

@pytest.fixture
def booking_id(booking_client, auth_headers):
    # Setup
    payload = build_booking_payload()
    response = booking_client.create_booking(payload)
    assert response.status_code == 200
    booking_id = response.json()["bookingid"]

    # Passing the ID to the test
    yield booking_id

    # TEARDOWN
    response = booking_client.get_booking(booking_id)
    if response.status_code == 200:
        delete_response = booking_client.delete_booking(
            booking_id,
            auth_headers
        )
        assert delete_response.status_code == 201
    elif response.status_code != 404:
        pytest.fail(
            f"Unexpected status during cleanup: {response.status_code}"
        )

@pytest.fixture(scope="session")
def booking_client(base_url):
    session = requests.Session()
    yield BookingClient(base_url, session)
    session.close()