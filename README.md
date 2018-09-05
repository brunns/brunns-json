# brunns-json

Extended JSON encoding and decoding for Python

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Build Status](https://travis-ci.org/brunns/brunns-json.svg?branch=master&logo=travis)](https://travis-ci.org/brunns/brunns-json)
[![PyPi Version](https://img.shields.io/pypi/v/brunns-json.svg?logo=pypi)](https://pypi.org/project/brunns-json/#history)
[![Python Versions](https://img.shields.io/pypi/pyversions/brunns-json.svg?logo=python)](https://pypi.org/project/brunns-json/)
[![Licence](https://img.shields.io/github/license/brunns/brunns-json.svg)](https://github.com/brunns/brunns-json/blob/master/LICENSE)
[![GitHub all releases](https://img.shields.io/github/downloads/brunns/brunns-json/total.svg?logo=github)](https://github.com/brunns/brunns-json/releases/)
[![GitHub forks](https://img.shields.io/github/forks/brunns/brunns-json.svg?label=Fork&logo=github)](https://github.com/brunns/brunns-json/network/members)
[![GitHub stars](https://img.shields.io/github/stars/brunns/brunns-json.svg?label=Star&logo=github)](https://github.com/brunns/brunns-json/stargazers/)
[![GitHub watchers](https://img.shields.io/github/watchers/brunns/brunns-json.svg?label=Watch&logo=github)](https://github.com/brunns/brunns-json/watchers/)
[![GitHub contributors](https://img.shields.io/github/contributors/brunns/brunns-json.svg?logo=github)](https://github.com/brunns/brunns-json/graphs/contributors/)
[![GitHub issues](https://img.shields.io/github/issues/brunns/brunns-json.svg?logo=github)](https://github.com/brunns/brunns-json/issues/)
[![GitHub issues-closed](https://img.shields.io/github/issues-closed/brunns/brunns-json.svg?logo=github)](https://github.com/brunns/brunns-json/issues?q=is%3Aissue+is%3Aclosed)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/brunns/brunns-json.svg?logo=github)](https://github.com/brunns/brunns-json/pulls)
[![GitHub pull-requests closed](https://img.shields.io/github/issues-pr-closed/brunns/brunns-json.svg?logo=github)](https://github.com/brunns/brunns-json/pulls?utf8=%E2%9C%93&q=is%3Apr+is%3Aclosed)

## Setup

Install with pip:

    pip install brunns-json

(As usual, use of a [venv](https://docs.python.org/3/library/venv.html) or [virtualenv](https://virtualenv.pypa.io) is recommended.)

## Developing

Requires [tox](https://tox.readthedocs.io). Run `make precommit` tells you if you're OK to commit. For more options, run:

    make help

## Releasing

Requires [hub](https://hub.github.com/), [setuptools](https://setuptools.readthedocs.io) and [twine](https://twine.readthedocs.io). To release `n.n.n`:

    version="n.n.n"
    git commit -am"Release $version" && git push # If not already all pushed, which it should be.
    hub release create $version -m"Release $version"
    python setup.py sdist
    twine upload dist/`ls -t dist/ | head -n1`
