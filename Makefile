init:
	pip install -r requirements.txt
clean:
	rm ./html/*.html
test:
	coverage run --source=. -m py.test tests
coverage:
	coverage report
