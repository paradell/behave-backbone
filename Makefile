VENV_PATH  := .venv

all: clean_virtualenv create_virtualenv activate_virtualenv install_requirements

clean_virtualenv:
	rm -rf $(VENV_PATH)

create_virtualenv:
	virtualenv $(VENV_PATH)

activate_virtualenv:
	@echo "run manually: 'source $(VENV_PATH)/bin/activate'"
	@echo "And then run 'make install_requirements'"
	exit 1

install_requirements:
	$(VENV_PATH)/bin/python3 -m pip install -r requirements.txt

test_pro:
	behave testSuite  --tags=~@skip --junit --define env=PRO

test_deprecated:
	behave testSuite  --tags=~@skip --junit --define env=DEPRECATED