# Makefile

SHELL := /usr/bin/env bash
venv_dev := ./venv_dev/
venv_prod := ./venv_prod/
dev_requirements := ./requirements/dev.txt
sources := $(wildcard pyvltree/*.py)
version := $(shell grep --perl-regex --only-matching \
			 "(?<=version=\')\d+\.\d+\.\d+(\-.+)?(?=\')" ./setup.py)
target := dist/PYVLTree-$(version).tar.gz

.PHONY: all
all: $(target)

.PHONY: clean
clean:
	rm -rf $(venv_dev) $(venv_prod)
	rm -rf ./pyvltree/__pycache__/
	rm -rf ./pyvltree/test/__pycache__/
	rm -rf ./dist/

.PHONY: test
test: $(target)
	source ./venv_dev/bin/activate;\
	python -m unittest

$(target): $(sources) $(venv_dev)
	source ./venv_dev/bin/activate;\
	python setup.py sdist;\
	pip install dist/PYVLTree-*.tar.gz

$(venv_dev): $(dev_requirements)
	rm -rf $(venv_dev)
	test -d vevn_dev || python3 -m venv $(venv_dev)
	source ./venv_dev/bin/activate;\
	pip install --upgrade pip setuptools;\
	pip install --requirement $(dev_requirements)
