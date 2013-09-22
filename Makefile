test:
	nosetests tests

coverage:
	nosetests --with-coverage --cover-html --cover-package=matchbox

pep8:
	pep8 matchbox tests

clean:
	rm .coverage
	rm -r cover