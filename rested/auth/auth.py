from base64 import b64encode

from .credentials import Token, User


class UnauthorizedError(Exception):
    pass


class Auth:
    """Base class for all auth types."""

    def __call__(self, client):
        # r.headers['Authorization'] = _basic_auth_str(self.username, self.password)
        client._authenticated = True


class UserAuth(Auth):
    def __init__(self, user):

        self._user = user
        self.username = user.username
        self.password = user.password


class UserLogin(UserAuth):
    def __init__(
        self, user, login_method, username_key="username", password_key="password"
    ):
        super(UserLogin, self).__init__(user)
        self._login = login_method
        self._username_key = username_key
        self._password_key = password_key

    def __call__(self):
        return self._login(
            _json={self._username_key: self.username, self._password_key: self.password}
        )


class BasicAuth(UserAuth):
    """HTTP Basic Authentication."""

    def __init__(self, user):

        self._user = user
        self.username = user.username
        self.password = user.password

    def __call__(self, client):

        client._authenticated = True
        client._default_headers.update({"Authorization": f"Basic: {self.encode()}"})

    def encode(self):

        return b64encode(f"{self.username}:{self.password}".encode("utf-8")).decode(
            "utf-8"
        )


# class ApiKey(Auth):

#     def __init__(self, apikey):

#         self.apikey = apikey

#     def __call__(self, client):
#         super(ApiKey, self).__call__(client)
#         # client.base_url += '?'


class TokenAuth(Auth):
    def __init__(self, token=None):

        self.token = token

    def _fetch_token(self, client):

        r = client._login()
        self.token = Token.deserialise(r.json())

    def __call__(self, client, header_key="Bearer"):

        if not self.token or self.token.expired():
            self._fetch_token(client)

        if not client._authenticated:
            client._authenticated = True
            client._default_headers.update({header_key: self.token.value})


class JwtAuth(TokenAuth):
    """JSON Web Token Authentication."""

    def __call__(self, client):

        super(JwtAuth, self).__call__(client, header_key="X-AUTH-TOKEN")


def login():

    return client._login()


def logout():
    pass


def hmac():
    pass


def oauth1():
    pass


def oauth2():
    pass


def api_key():
    pass
