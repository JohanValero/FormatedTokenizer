all:
	python3 ./src/lexer.py

test:
	python3 ./test/test_lexer.py

venv:
	python3 -m venv env

activate_env:
	source ./env/Scripts/activate