init:
	pip install -r requirements.txt
clean:
	rm ./html/*.html
test:
	py.test tests
