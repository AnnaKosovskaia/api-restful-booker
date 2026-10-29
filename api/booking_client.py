from api.base_client import BaseClient
from api.endpoints import BOOKINGS, booking_by_id, PING



class BookingClient(BaseClient):

    def get_booking_ids(self):
        return self.get(BOOKINGS)

    def get_booking(self, booking_id):
        return self.get(booking_by_id(booking_id))

    def create_booking(self, payload):
        return self.post(BOOKINGS, payload)

    def update_booking(self, booking_id, payload, headers):
        return self.put(booking_by_id(booking_id), payload, headers)

    def delete_booking(self, booking_id, headers):
        return self.delete(booking_by_id(booking_id), headers)

    def ping(self):
        return self.get(PING)


