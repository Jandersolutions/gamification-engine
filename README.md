# gamification-engine
[![Build Status](https://travis-ci.org/ActiDoo/gamification-engine.svg?branch=master)](https://travis-ci.org/ActiDoo/gamification-engine)
[![Requirements Status](https://requires.io/github/ActiDoo/gamification-engine/requirements.svg?branch=master)](https://requires.io/github/ActiDoo/gamification-engine/requirements/?branch=master)
[![Heroku](https://heroku-badge.herokuapp.com/?app=gamification-engine&root=admin)](https://gamification-engine.herokuapp.com)
[![Documentation Status](https://img.shields.io/badge/docs-latest-brightgreen.svg?style=flat)](https://readthedocs.org/projects/gamification-engine/?badge=latest)
[![Latest Version](https://badge.fury.io/py/gamification-engine.svg)](https://pypi.python.org/pypi/gamification-engine/)
[![Downloads](https://img.shields.io/pypi/dm/gamification-engine.svg)](https://pypi.python.org/pypi/gamification-engine/)
[![License](http://img.shields.io/:license-mit-green.svg)](https://pypi.python.org/pypi/gamification-engine/)


The Gamification-Engine (gengine) is an open source software (MIT) for integrating any kinds of gamification features into your product.

The engine is **not meant to be a platform** including any kinds of predefined graphics, layouts or statistics.
It is framework for developing your own solution, implemented as a **service** to which your application server can talk over a REST api. 

(commercial support available at https://www.gamification-software.com)

**Latest recommended version: v0.1.31** (not yet called "stable" though)

## Features

- multi level achievements
- multi goal achievements
- progress and single goals 
- leader boards / ladder
- achievements can be reached directly or by evaluating leaderboards daily, weekly, monthly or yearly
- time zone independent (correct daily, weekly.. evaluations among time zones)
- social-awareness (e.g. reach the highest score among your friends)
- geo-awareness (e.g. reach the highest score among all users in your city)
- rules can be defined in python using given variables (e.g. the current level)
- custom definable achievement properties and rewards
- custom definable languages and translations
- dependencies between achievements (prerequisites & postconditions)
- high performance / scalable
- administration ui

## REST Interface

Simple REST-interface to communicate with arbitrary systems

see http://gamification-engine.readthedocs.org/en/latest/rest/index.html

## Demo Installation

A demo installation is available at https://gamification-engine.herokuapp.com/

## Usage

1. A ready-to-use buildpack for Heroku and dokku is available at https://github.com/ActiDoo/gamification-engine-dokku Follow the instructions there.
2. The current stable version is available as phyton package at https://pypi.python.org/pypi/gamification-engine
3. Checkout the source code and configure the PostgreSQL database in `development.ini`. Then run `python setup.py develop` to configure the application and `pserve development.ini` to start it. The front end is available at http://localhost:6543

## Roadmap

Do you want to contribute? We badly need tests!
Also a nicer admin UI would be great or maybe some cool features :-) 

For a full list see:

http://gamification-engine.readthedocs.org/en/latest/roadmap.html

## Licenses of dependencies

Pyramid: BSD-derived (http://www.repoze.org/LICENSE.txt)

pyramid_chameleon: BSD-derived (http://www.repoze.org/LICENSE.txt)

pyramid_debugtoolbar: BSD

SQLAlchemy: MIT

zope.sqlalchemy: Zope Public License (ZPL) Version 2.1

waitress: Zope Public License (ZPL) Version 2.1

pytz: MIT

dogpile.cache: BSD

pyramid_dogpile_cache: MIT

flask: BSD

flask-admin: BSD

psycopg2: LGPL / ZPL

pymemcache: Apache License 2.0

mock: BSD

alembic: MIT
