from api.base_client import BaseClient
from api.endpoints import AUTH


class AuthClient(BaseClient):
    def login(self, credentials):
        return self.post(AUTH, credentials)