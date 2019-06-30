import getpass
import datetime

from dataclasses import dataclass


class InvalidError(Exception):
    pass


@dataclass
class User:

    username: str
    password: str

    def serialise(self):
        pass

    

@dataclass
class Token:

    _as_string: str
    _valid_for_in_seconds: int = 120
    _created = datetime.datetime = datetime.datetime.utcnow()
    _expires: datetime.datetime = _created + datetime.timedelta(seconds=_valid_for_in_seconds)
    
    @property
    def value(self):

        return self._as_string

    @classmethod
    def from_cache(cls, cache):
        pass

    @classmethod
    def deserialise(cls, _json, _json_token_key='token'):
        """Deserialise from an API reponse. _json is a python dictionary representation of an API JSON response."""
        kwargs = dict(
            _as_string=_json.get(_json_token_key)
        )
        return cls(**kwargs)

    def serialise(self):
        pass

    def to_cache(self, cache):
        pass

    def expired(self):
        """
        Check if Token has expired

        :returns: Boolean
        """

        return datetime.datetime.utcnow() > self._expires
    
    def about_to_expire(self, threshold_in_seconds=3600):
        """
        Check if Token will expire within a given number of hours

        :threshold: Number of hours to expiry
        :returns: Boolean
        """
        if self.expired():
            raise InvalidError('Token has expired')
        return self._expires <= datetime.datetime.utcnow() + datetime.timedelta(
            seconds=threshold_in_seconds
        )
    