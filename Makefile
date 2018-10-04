# Makefile

SHELL := /usr/bin/env bash
venv := ./venv
dev_requirements := ./requirements/dev.txt
sources := $(wildcard pyvltree/*.py)
version := $(shell grep --perl-regex --only-matching \
			 "(?<=version=\')\d+\.\d+\.\d+(\-.+)?(?=\')" ./setup.py)
target := dist/PYVLTree-$(version).tar.gz

.PHONY: all
all: $(target)

.PHONY: clean
clean:
	rm -rf $(venv)
	rm -rf ./pyvltree/__pycache__/
	rm -rf ./pyvltree/test/__pycache__/
	rm -rf ./dist/
	rm -rf ./PYVLTree.egg-info/

.PHONY: test
test: $(target)
	source $(venv)/bin/activate;\
	coverage run -m unittest;\
	coverage report -m

$(target): $(sources) $(venv)
	source $(venv)/bin/activate;\
	python setup.py sdist;\
	pip install $(target)

$(venv): $(dev_requirements) setup.py
	rm -rf $(venv)
	python3 -m venv $(venv)
	source $(venv)/bin/activate;\
	pip install --upgrade pip setuptools;\
	pip install --requirement $(dev_requirements)
