#!/bin/bash

set -e
errors=0

# Run unit tests
python pdb_add_chain/pdb_add_chain_test.py || {
    echo "'python python/pdb_add_chain/pdb_add_chain_test.py' failed"
    let errors+=1
}

# Check program style
pylint -E pdb_add_chain/*.py || {
    echo 'pylint -E pdb_add_chain/*.py failed'
    let errors+=1
}

[ "$errors" -gt 0 ] && {
    echo "There were $errors errors found"
    exit 1
}

echo "Ok : Python specific tests"
