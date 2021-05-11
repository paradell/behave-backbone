# Ophen Test Assignment

This is a test assignment for Ophen Automation Test vacancy

## Goals of this assignment
Create automated tests for the GitHub API.

## How to set up the environment
Before setting up the environment, make sure your machine has installed:
* Python3
* Pip
* Virtualenv

Everything is scripted in the Makefile to ease the process.

1. Set up the virtual environment
```make create_virtualenv```
or run manually
```python3 -m venv .venv```

2. Install requirements
```make install_requirements```

3. Activate the virtualenv (this is not possible to do by running make commands)
```source .venv/bin/activate```

## Run the tests
This automated tests run using behave, and it can be used to run it against the production environment of Github API or the deprecated one.
```make test_pro```
```make test_deprecated```

This will run all the tests without the "skip" tag and store the oputput JUnit results in a XML file that can be used to present properly the results.
