.PHONY: all install run

VENV       = venv
APP_PATH   = proxapy
APP_MODULE = proxapy.proxapy:app
CONFIG     = config/gunicorn

all run: install
	$(VENV)/bin/gunicorn -c $(CONFIG) --pythonpath $(APP_PATH) $(APP_MODULE)

$(VENV):
	virtualenv $(VENV)

install: $(VENV) requirements.txt
	$(VENV)/bin/pip install -r requirements.txt

clean:
	rm -rf $(VENV) __pycache__ *.pyo *.pyc
