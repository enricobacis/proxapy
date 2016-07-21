.PHONY: all debug install run

VENV = venv
FLASK_APP = proxy.py
FLASK_DEBUG = 0

all run: install
	env FLASK_DEBUG=$(FLASK_DEBUG) FLASK_APP=$(FLASK_APP) $(VENV)/bin/flask run

debug: FLASK_DEBUG=1
debug: run

$(VENV):
	virtualenv $(VENV)

install: $(VENV) requirements.txt
	$(VENV)/bin/pip install -r requirements.txt

clean:
	rm -rf $(VENV) __pycache__ *.pyo *.pyc
