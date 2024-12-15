# Contributing

Everyone is welcome to contribute to `best-practices`. We strictly
enforce our [Code of Conduct](../CODE_OF_CONDUCT.md), so please review it before
contributing.

## Getting started

1. [Fork the repository](https://github.com/django-commons/best-practices/fork)
2. Clone your fork of the repository `git clone git@github.com:[YOUR_USERNAME_HERE]/best-practices.git && cd best-practices`
3. Create a venv and activate it `python -m venv venv && source venv/bin/activate`
4. Create a feature branch for your work `git checkout -b relevant-branch-name-here`
5. Implement your changes, run the tests and make a commit to your branch
6. Push your branch to GitHub `git push origin relevant-branch-name-here`
7. Create a [PR on the upstream repo (this repo)](https://github.com/django-commons/best-practices/pulls)

## Architecture

The best-practices is a collection of utility functions with a
playground theme. The purpose is to serve as an example to inbound repositories.
Because of that the documentation, pre-commit configuration and GitHub actions
are the most important aspects of the project. The code itself is secondary.

## Running the tests

```shell
python3 -m unittest
```

Nothing special here!

## Releasing

The repo is configured to [automatically release to PyPI](https://github.com/django-commons/best-practices/blob/main/.github/workflows/release.yml)
when a new tag is pushed to GitHub. This makes use of [PyPI's trusted publishers](https://docs.pypi.org/trusted-publishers/).

### Manual releases

In the case a manual release is necessary, you'll need to use [Twine](https://github.com/pypa/twine) and [Build](https://github.com/pypa/build).

```shell
# Install packaging dependencies
python3 -m pip install -U twine build
# Build the project
python3 -m build
# Release to test PyPI
python3 -m twine upload --repository testpypi dist/*
# Release to PyPI
python3 -m twine upload dist/*
```
