sources := $(wildcard pyvltree/*.py)
version := $(shell grep --perl-regex --only-matching \
			 "(?<=version=\')\d+\.\d+\.\d+(\-.+)?(?=\')" ./setup.py)
target := dist/pyvltree-$(version).tar.gz

.PHONY: all
all: $(target)

.PHONY: clean
clean:
	rm -rf ./pyvltree/__pycache__/
	rm -rf ./pyvltree/test/__pycache__/
	rm -rf ./dist/
	rm -rf ./PYVLTree.egg-info/

.PHONY: publish
publish: $(target)
	pipenv run twine publish ./dist/pyvltree-$(version).tar.gz ./dist/pyvltree-$(version)-py3-none-any.whl

.PHONY: test
test: $(target)
	pipenv run python setup.py test
	pipenv run coverage report -m

$(target): $(sources)
	pipenv update --dev
	pipenv run python setup.py sdist bdist_wheel
	pipenv run pip install $(target)
