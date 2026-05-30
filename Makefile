.PHONY: install build clean serve

install:
	python -m pip install -r requirements.txt

build:
	python scripts/build_docs.py --clean

clean:
	python -c "import shutil, pathlib; shutil.rmtree(pathlib.Path('build'), ignore_errors=True)"

serve:
	python -m http.server 8000 --directory build/html
