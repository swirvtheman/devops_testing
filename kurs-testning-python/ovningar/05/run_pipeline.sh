#!/usr/bin/env bash

set -e 

echo "Running flake8..."
flake8 calculator.py calculator_test.py --max-line-length=120
echo "flake8 OK"

echo "Running pytest..." 
pytest --cov=calculator --cov-branch --cov-report=term-missing --cov-fail-under=80 calculator_test.py
echo "pytest OK"

echo "Pipeline completed successfully!"