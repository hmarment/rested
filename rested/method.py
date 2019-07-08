from .http import HttpClient


class Method:
    def __init__(
        self,
        name=None,
        http_method=None,
        resource=None,
        accepted_params=None,
        authenticate=True,
    ):

        # super(Method, self).__init__(
        #     session=resource._integration._session,
        #     default_headers=resource._integration._default_headers
        # )
        self.name = name
        self.http_method = http_method
        self.accepted_params = accepted_params
        self._resource = resource
        self._authenticate = authenticate

    def __call__(self, url_params=None, headers=None, _json=None):

        url = self._build_url(*url_params if url_params else list())
        headers = self._resource._integration._set_headers(headers)
        return self._resource._integration._request(
            http_method=self.http_method,
            url=url,
            headers=headers,
            json=_json,
            authenticate=self._authenticate,
        )

    def _build_url(self, *parts):
        return self._resource._build_url(self.name, *parts)
