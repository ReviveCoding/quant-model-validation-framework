.PHONY: install run test validate clean dashboard

install:
	python -m pip install --upgrade pip
	python -m pip install -r requirements.txt

run:
	PYTHONDONTWRITEBYTECODE=1 python scripts/run_pipeline.py

test:
	PYTHONDONTWRITEBYTECODE=1 PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 python -m pytest -q

validate: run test

clean:
	rm -rf outputs reports data/processed .pytest_cache
	find . -type d -name "__pycache__" -prune -exec rm -rf {} +

dashboard:
	python -m pip install -r requirements-dashboard.txt
	streamlit run src/dashboard/streamlit_app.py
