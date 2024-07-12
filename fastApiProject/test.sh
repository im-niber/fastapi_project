#!/usr/bin/env bash
# 맨 윗 줄은 bash로 실행해라 라는 뜻 #!
set -eo pipefail
# 중간에 실패하면 중지하라 라는 의미의 pipefail

COLOR_GREEN=`tput setaf 2;`
COLOR_NC=`tput sgr0;` # No Color

echo "Starting black"
poetry run black .
echo "OK"

echo "Starting isort"
poetry run isort .
echo "OK"

echo "Starting mypy"
poetry run mypy .
echo "OK"

echo "Starting pytest with coverage"
poetry run coverage run -m pytest
poetry run coverage report -m
poetry run coverage html

echo "${COLOR_GREEN}All tests passed successfully!${COLOR_NC}"