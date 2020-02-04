compile ::
	python setup.py sdist bdist_wheel
	
push :: 
	python -m twine upload dist/*