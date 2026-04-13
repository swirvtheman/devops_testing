#!/usr/bin/env bash
# AI älskar verkligen sina emojis, så vi kör på det! 🚀

set -e  # Avbryt vid fel — precis som en CI-pipeline

echo "=============================="
echo "  TESTPIPELINE"
echo "=============================="

echo ""
echo "📋 Steg 1: Linting med flake8..."
flake8 src/ tests/ --max-line-length=120
echo "✅ Linting OK"

echo ""
echo "🔍 Steg 2: Typkontroll med mypy..."
mypy src/ --ignore-missing-imports
echo "✅ Typkontroll OK"

echo ""
echo "🧪 Steg 3: Enhetstester med coverage..."
pytest tests/ -v --cov=src --cov-report=term-missing --cov-fail-under=80
echo "✅ Tester OK"

echo ""
echo "🔒 Steg 4: Säkerhetsanalys med bandit..."
bandit -r src/ -ll
echo "✅ Säkerhetsanalys OK"

echo ""
echo "=============================="
echo "  ✅ PIPELINE LYCKADES!"
echo "=============================="

