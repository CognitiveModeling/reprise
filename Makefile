default: test
documentation:
		cd doc; $(MAKE) clean; $(MAKE) html
test:
		pytest doc/source/*.rst tests/*.py
checkstyle:
		pylint --rcfile=setup.cfg -j 2 reprise tests
.PHONY: default documentation test checkstyle
