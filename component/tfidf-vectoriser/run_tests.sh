#!/usr/bin/env bash
python setup.py nosetests
rtrn_code=$?
coverage erase
exit $rtrn_code