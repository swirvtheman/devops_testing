FROM python:3.14-slim

RUN pip install --no-cache-dir \
    pytest \
    pytest-cov \
    pytest-mock \
    pytest-bdd \
    hypothesis \
    mutmut \
    tox \
    flake8 \
    mypy \
    bandit \
    responses \
    faker \
    selenium \
    behave \
    locust \
    safety

WORKDIR /app
CMD ["bash"]
