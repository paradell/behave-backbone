VENV_PATH  := .behave_venv

create_virtualenv:
	virtualenv $(VENV_PATH)

activate_virtualenv:
	source $(VENV_PATH)/bin/activate

install_requirements:
	pip install -r requirements.txt

test:
	behave testSuite
