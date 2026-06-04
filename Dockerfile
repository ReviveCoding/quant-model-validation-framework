FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTEST_DISABLE_PLUGIN_AUTOLOAD=1

WORKDIR /app
COPY requirements.txt ./
RUN python -m pip install --no-cache-dir --upgrade pip \
    && python -m pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["sh", "-c", "python scripts/run_pipeline.py && python -m pytest -q"]
