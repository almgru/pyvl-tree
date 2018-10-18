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
	#twine publish ./dist/pyvltree-$(version).tar.gz ./dist/pyvltree-$(version)-py3-none-any.whl

.PHONY: plot
plot: metrics
	. ./venv/bin/activate ;\
			./scripts/plot.py ./run-times/latest.txt -o ./plots/ ;\
			mv ./plots/plot-linear.png ./plots/lin-$$(date +'%F_%T').png ;\
			mv ./plots/plot-log.png ./plots/log-$$(date +'%F_%T').png ;\
			mv ./run-times/latest.txt ./run-times/$$(\date +'%F_%T').txt

.PHONY: metrics
metrics:
	@echo "Generating runtime metrics. This may take a while.."
	. ./venv/bin/activate ;\
			./scripts/gather-run-time-metrics.sh --iterations 1000 \
												 --n-pow-start 0 \
												 --n-pow-end 16 \
			> ./run-times/latest.txt

.PHONY: test
test: $(target)
	. ./venv/bin/activate ;\
			python setup.py test ;\
			coverage report -m

$(target): venv $(sources)
	. ./venv/bin/activate ;\
			python setup.py sdist bdist_wheel ;\
			pip install $(target)

venv:
	python3 -m venv venv
	. ./venv/bin/activate ;\
			pip install --upgrade pip setuptools wheel ;\
			pip install --requirement ./requirements-dev.txt
