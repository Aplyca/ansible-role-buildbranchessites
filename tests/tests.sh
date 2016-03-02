#!/bin/bash
# test MatiaDB provisiones with ansible

cd $(dirname "$0") && cd ..

echo "Install dependencies"
ansible-galaxy install -r dependencies.yml

echo "Checking syntax"

ansible-playbook -i inventories/local playbook.yml --connection=local --syntax-check

echo "Running role"
ansible-playbook -i inventories/local playbook.yml --connection=local

echo "Checking idempotence"
ansible-playbook -i inventories/local playbook.yml --connection=local | grep -q 'changed=0.*failed=0' && (echo 'Idempotence test: pass' && exit 0) || (echo 'Idempotence test: fail' && exit 1)

echo "Running tests"
ansible-playbook -i inventories/local tests/playbook.yml --connection=local
