class BadRequest400(Exception):
    """
    HTTP 400 Error
    """

    pass


class Unauthorized401(Exception):
    """
    HTTP 401 Error
    """

    pass


class Forbidden403(Exception):
    """
    HTTP 403 Error
    """

    pass


class NotFound404(Exception):
    """
    HTTP 404 Error
    """

    pass


class MethodNotAllowed405(Exception):
    """
    HTTP 405 Error
    """

    pass


class NotAcceptable406(Exception):
    """
    HTTP 406 Error
    """

    pass


class PreconditionFailed412(Exception):
    """
    HTTP 412 Error
    """

    pass


class UnsupportedMediaType415(Exception):
    """
    HTTP 415 Error
    """

    pass


class TooManyRequests429(Exception):
    """
    HTTP 429 Error
    """

    pass


class InternalServerError500(Exception):
    """
    HTTP 500 Error
    """

    pass


class NotImplemented501(Exception):
    """
    HTTP 501 Error
    """

    pass


class BadGateway502(Exception):
    """
    HTTP 502 Error
    """

    pass


class ServiceUnavailable503(Exception):
    """
    HTTP 503 Error
    """

    pass


class GatewayTimeout504(Exception):
    """
    HTTP 504 Error
    """

    pass


HTTP_ERRORS = {
    400: BadRequest400,
    401: Unauthorized401,
    403: Forbidden403,
    404: NotFound404,
    405: MethodNotAllowed405,
    406: NotAcceptable406,
    412: PreconditionFailed412,
    415: UnsupportedMediaType415,
    429: TooManyRequests429,
    500: InternalServerError500,
    501: NotImplemented501,
    502: BadGateway502,
    503: ServiceUnavailable503,
    504: GatewayTimeout504,
}
