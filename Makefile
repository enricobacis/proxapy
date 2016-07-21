.PHONY: all debug install run

VENV        = venv
FLASK_DEBUG = 0
FLASK_APP   = proxy.py
HOST        = 0.0.0.0
PORT        = 5000

all run: install
	env FLASK_DEBUG=$(FLASK_DEBUG) FLASK_APP=$(FLASK_APP) \
		$(VENV)/bin/flask run --host $(HOST) --port $(PORT)

debug: FLASK_DEBUG=1
debug: run

$(VENV):
	virtualenv $(VENV)

install: $(VENV) requirements.txt
	$(VENV)/bin/pip install -r requirements.txt

clean:
	rm -rf $(VENV) __pycache__ *.pyo *.pyc
