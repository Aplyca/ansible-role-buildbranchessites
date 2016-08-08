#!/bin/bash
# test BuildBranchesSites provisiones with ansible

echo "Starting VM and provision with role"
vagrant destroy -f &&
vagrant up
