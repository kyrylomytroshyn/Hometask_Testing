#!/bin/bash -x

echo "Running tests"
pytest

echo "Running mypy"
mypy --config-file mypy.cfg .

echo "Running pylint"
pylint --rcfile=.pylintrc --load-plugins pylint_django --disable no-self-use apps/
