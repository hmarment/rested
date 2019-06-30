from rested.auth.auth import BasicAuth, User

TEST_USERNAME = 'test@user.com'
TEST_PASSWORD = 'password'

def test_auth_basic(test_integration):

    user = User(TEST_USERNAME, TEST_PASSWORD)
    auth = BasicAuth(user)
    
    auth(test_integration)

    assert 'Authorization' in test_integration._default_headers and test_integration._default_headers.get('Authorization') ==  'Basic: dGVzdEB1c2VyLmNvbTpwYXNzd29yZA=='