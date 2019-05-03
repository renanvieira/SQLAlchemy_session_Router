run-tests:
	coverage run  --branch --source $(shell pwd) --omit=tests/*,setup.py -m unittest discover --start-directory tests/
	coverage-badge -f -o coverage.svg
