# Makefile

SHELL := /usr/bin/env bash
sources := $(wildcard pyvltree/*.py)
version := $(shell grep --perl-regex --only-matching \
			 "(?<=version=\')\d+\.\d+\.\d+(\-.+)?(?=\')" ./setup.py)
target := dist/PYVLTree-$(version).tar.gz

.PHONY: all
all: $(target)

.PHONY: test
test: $(target)
	source ./venv_dev/bin/activate;\
	python -m unittest

$(target): $(sources) venv_dev
	source ./venv_dev/bin/activate;\
	python setup.py sdist;\
	pip install dist/PYVLTree-*.tar.gz

venv_dev: requirements/dev.txt requirements/common.txt
	test -d vevn_dev || python3 -m venv ./venv_dev/
	source ./venv_dev/bin/activate;\
	pip install --upgrade pip setuptools;\
	pip install --requirement requirements/dev.txt
