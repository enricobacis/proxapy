.PHONY: all install run

VENV = venv
FLASK_APP = proxy.py

all run: install
	env FLASK_APP=$(FLASK_APP) $(VENV)/bin/flask run

$(VENV):
	virtualenv $(VENV)

install: $(VENV) requirements.txt
	$(VENV)/bin/pip install -r requirements.txt

clean:
	rm -rf $(VENV) __pycache__ *.pyo *.pyc
