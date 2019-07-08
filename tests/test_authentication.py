from rested.auth.auth import Auth, BasicAuth, JwtAuth, Token, User

from .conftest import MockResponse

TEST_USERNAME = "test@user.com"
TEST_PASSWORD = "password"
TEST_JWT = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"


def test_no_auth(test_integration):

    assert not test_integration._authenticated

    auth = Auth()
    auth(test_integration)

    assert test_integration._authenticated


def test_auth_basic(test_integration):

    assert not test_integration._authenticated

    user = User(TEST_USERNAME, TEST_PASSWORD)
    auth = BasicAuth(user)

    auth(test_integration)

    assert (
        test_integration._authenticated
        and "Authorization" in test_integration._default_headers
        and test_integration._default_headers.get("Authorization")
        == "Basic: dGVzdEB1c2VyLmNvbTpwYXNzd29yZA=="
    )


def test_auth_jwt(mocker, test_integration):

    assert not test_integration._authenticated

    mocker.patch.object(
        test_integration,
        "_login",
        return_value=MockResponse(200, content=dict(token=TEST_JWT)),
    )

    auth = JwtAuth()
    auth(test_integration)

    assert (
        test_integration._authenticated
        and "X-AUTH-TOKEN" in test_integration._default_headers
        and test_integration._default_headers.get("X-AUTH-TOKEN") == TEST_JWT
    )
