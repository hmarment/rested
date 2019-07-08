import os
import getpass
import datetime
import configparser

from tomlkit import parse
from dataclasses import dataclass

CACHE_PATH = os.path.join(os.path.expanduser("~"), ".rested")
CREDENTIALS_FILE = ".credentials"
CREDENTIALS_CACHE = os.path.join(CACHE_PATH, CREDENTIALS_FILE)


def _load_cache(credentials_file_path=CREDENTIALS_CACHE):

    credentials = configparser.ConfigParser()
    credentials.read(credentials_file_path)

    return credentials


class InvalidError(Exception):
    pass


@dataclass
class User:

    username: str
    password: str

    def serialise(self, username_key="username", password_key="password", **kwargs):
        """Generate a dictionary ('JSON') representation."""

        serialised = {username_key: self.username, password_key: self.password}

        for key, val in kwargs.keys():
            serialised[key] = val

        return serialised

    @classmethod
    def from_cache(cls, profile_name):

        credentials = _load_cache()

        if profile_name in credentials:
            profile = credentials[profile_name]
            try:
                u = User(username=profile["username"], password=profile["password"])
            except KeyError:
                raise KeyError(
                    f"Username / Password not defined from profile={profile_name}"
                )
            else:
                return u


@dataclass
class Token:

    _as_string: str
    _valid_for_in_seconds: int = 120
    _created = datetime.datetime = datetime.datetime.utcnow()
    _expires: datetime.datetime = _created + datetime.timedelta(
        seconds=_valid_for_in_seconds
    )

    @property
    def value(self):

        return self._as_string

    @classmethod
    def from_cache(cls, cache):
        pass

    @classmethod
    def deserialise(cls, _json, _json_token_key="token"):
        """Deserialise from an API reponse. _json is a python dictionary representation of an API JSON response."""
        kwargs = dict(_as_string=_json.get(_json_token_key))
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
            raise InvalidError("Token has expired")
        return self._expires <= datetime.datetime.utcnow() + datetime.timedelta(
            seconds=threshold_in_seconds
        )
