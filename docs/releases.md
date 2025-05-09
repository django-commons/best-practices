# Releasing packages

This section describes how to release Python packages using the Best Practices
methodology

Note: the Best Practices repo uses setuptools as it's build tool. Any tool will work,
but you will need to change your ``pyproject.toml`` and ``<package>/version.py`` file.

## Releases

Software releases are automated through the GitHub Action at
``.github/workflows/release.yml``. It uses PyPI's [Trusted Publisher](https://docs.pypi.org/trusted-publishers/)
integration with GitHub.

PyPI packages are published when a new tag is pushed to origin that
doesn't have `.dev` contained within it.

It's strongly recommended that you limit who can trigger a PyPI release
of your package. The ``release.yml`` supports this via the ``pypi`` environment.
You can limit who can approve the workflow by configuring the environment
(``pypi`` in this case) to have [required reviewers](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-deployments/managing-environments-for-deployment#required-reviewers).

## Testing Releases

The packaging and release process can be tested by utilizing the ``test_release.yml``
GitHub action workflow.

This requires you to allow your package's version to be configured by an environment
variable. An example of this can be seen in ``src/django_commons_best_practices/__init__.py``.
You will also need to change your ``pyproject.toml`` to allow
[dynamic versioning](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/#static-vs-dynamic-metadata).

To test the release process fully, the package must be built with a unique version.
The default versioning schema only supports a `.dev` suffix that is an obviously test
tag. You need to allow a suffix to be specified from an environment variable, then use
that environment variable in ``test_release.yml`` for the ``DEV_VERSION_ENV_KEY`` env
variable.

### Running tests

The default version of ``test_release.yml`` will run the tests once per month, on the second
day of the month.

It also supports running the tests on an adhoc basis via the ``workflow_dispatch`` GitHub
action event type. It will require you to specify an ``iteration`` value. This value must
be unique for each test run on a given day.