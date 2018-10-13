sources := $(wildcard pyvltree/*.py)
version := $(shell grep --perl-regex --only-matching \
			 "(?<=version=\')\d+\.\d+\.\d+(\-.+)?(?=\')" ./setup.py)
target := dist/PYVLTree-$(version).tar.gz

.PHONY: all
all: $(target)

.PHONY: clean
clean:
	rm -rf ./pyvltree/__pycache__/
	rm -rf ./pyvltree/test/__pycache__/
	rm -rf ./dist/
	rm -rf ./PYVLTree.egg-info/

.PHONY: test
test: $(target)
	pipenv run coverage run -m unittest
	pipenv run coverage report -m

$(target): $(sources)
	pipenv update --outdated
	pipenv run python setup.py sdist
	pipenv run pip install $(target)
