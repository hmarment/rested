
from .http import HttpClient

class Method(HttpClient):
    
    def __init__(self, name=None, http_method=None, resource=None, accepted_params=None):

        super(Method, self).__init__(
            session=resource._session,
            default_headers=resource._default_headers
        )
        self.name = name
        self.http_method = http_method
        self.accepted_params = accepted_params
        self._resource = resource

    def __call__(self, url_params=None, headers=None, _json=None):

        url = self._build_url(*url_params if url_params else list())
        headers = self._set_headers(headers)
        return self._request(http_method=self.http_method, url=url, headers=headers, json=_json)

    def _build_url(self, *parts):
        return super()._build_url(
            self._resource._integration.base_url,
            self._resource.name,
            self.name,
            *parts
        )
