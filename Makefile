init:
	pip3 install -r requirements.txt
clean:
	rm ./html/*.html
test:
	rm ./test_html/*.html; coverage run --source=. -m py.test tests
coverage:
	coverage report
