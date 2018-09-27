# Makefile

SHELL := /usr/bin/env bash

.PHONY: all
all: debug

.PHONY: debug
debug: venv_dev
	source ./venv_dev/bin/activate;\
	python setup.py sdist;\
	pip install dist/PYVLTree-*.tar.gz

venv_dev: requirements/dev.txt requirements/common.txt
	test -d vevn_dev || python3 -m venv ./venv_dev/
	source ./venv_dev/bin/activate;\
	pip install --upgrade pip setuptools;\
	pip install --requirement requirements/dev.txt
