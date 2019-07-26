# rested

> Rested helps you set up and configure client(s) for third-party RESTful HTTP APIs, by writing simple configuration files.

[![Python 3.7][python-url]][python-url]
[![Build Status][travis-image]][travis-url]


## Installation

OS X & Linux:

```sh
poetry install rested
```


## Usage example

TBD

<!-- _For more examples and usage, please refer to the [Wiki][wiki]._ -->

### Config File

Each config file corresponds to one _integration_ or third-party API. Integrations contain one or many _resources_. Resources support CRUD operations by default, with the ability to add additonal methods.

```toml
[configuration]

name = "myapi"
base-url = "https://jsonplaceholder.typicode.com"

    [configuration.auth]
    # integration level authentication settings

    type = "JWT"
    login-resource = 'auth' # resource containing login method
    login-method = 'signin'  # method to login

[resources]

    [resources.auth.login]
    
    endpoint = "auth/login"
    method = "POST"
    arguments = ["username", "password", "rememberMe"]
    authenticate = false

    [resources.posts]

    [resources.todos.list]

    endpoint = "list"
    method = "GET"

    [resources.comments]

    [resources.albums]
    
    [resources.photos]

    [resources.users]

```

## Development setup

Describe how to install all development dependencies and how to run an automated test-suite of some kind. Potentially do this for multiple platforms.

```sh
poetry install rested
```

## Meta

Henry Marment – henrymarment@gmail.com

Distributed under the MIT license. See ``LICENSE`` for more information.

[https://github.com/hmarment/rested](https://github.com/hmarment/)

## Contributing

1. Fork it (<https://github.com/hmarment/rested/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

<!-- Markdown link & img dfn's -->
[python-image]: https://img.shields.io/badge/python-3.7-blue.svg
[python-url]: https://www.python.org/downloads/release/python-372/
<!-- [travis-image]: https://img.shields.io/travis/dbader/node-datadog-metrics/master.svg?style=flat-square -->
[travis-url]: https://travis-ci.com/hmarment/rested
[wiki]: https://github.com/yourname/yourproject/wiki