VENV := ids706

all: setup format lint test

setup:
	rm -rf $(VENV)
	python3 -m venv $(VENV)
	$(VENV)/bin/pip install -r requirements.txt

lint:
	$(VENV)/bin/pylint src/ --ignore-patterns=test_.*?py

format:
	$(VENV)/bin/black src/

test:
	$(VENV)/bin/pytest -v src/
	rm -rf *.png *.pdf

run:
	$(VENV)/bin/python src/main.py

deploy:
	git config --local user.email "41898282+github-actions[bot]@users.noreply.github.com"
	git config --local user.name "github-actions[bot]"
	git add NBA_2021_Report.pdf
	git add ./*.png
	git commit -m "Add report and images"

clean:
	rm -rf $(VENV)