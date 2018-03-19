#!/bin/bash

if [ "$1" = "--skip-build" ]; then
    echo "skipping build..."
else
    echo "building image, to skip run with --skip-build"
    docker build -t test-image .
fi

# see https://explainshell.com/explain?cmd=set+-euxo%20pipefail
set -euxo pipefail

docker run --rm -it test-image --version
docker run --rm -it --entrypoint '' \
    -v `pwd`:/test -w /test  \
    test-image bash -c 'pip install tox && tox'

# move container coverage paths to local, see .coveragerc [paths] and this comment:
# https://github.com/pytest-dev/pytest-cov/issues/146#issuecomment-272971136
echo "combining container coverage..."
mv .coverage .coverage.tmp
coverage combine --append

echo "tests finished..."
