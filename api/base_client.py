class BaseClient():
    def __init__(self, base_url, session):
        self.base_url = base_url
        self.session = session

    def get(self, endpoint):
        return self.session.get(
            f"{self.base_url}{endpoint}"
        )

    def post(self, endpoint, payload):
        return self.session.post(
            f"{self.base_url}{endpoint}",
            json=payload
        )

    def put(self, endpoint, payload, headers):
        return self.session.put(
            f"{self.base_url}{endpoint}",
            json=payload,
            headers=headers
        )

    def delete(self, endpoint, headers):
        return self.session.delete(
            f"{self.base_url}{endpoint}",
            headers=headers
        )
