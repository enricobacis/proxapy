.PHONY: all install run

VENV       = venv
APP_MODULE = proxy:app
CONFIG     = config.py

all run: install
	$(VENV)/bin/gunicorn -c $(CONFIG) $(APP_MODULE)

$(VENV):
	virtualenv $(VENV)

install: $(VENV) requirements.txt
	$(VENV)/bin/pip install -r requirements.txt

clean:
	rm -rf $(VENV) __pycache__ *.pyo *.pyc
