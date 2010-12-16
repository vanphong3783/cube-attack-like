#!/bin/bash

nohup python attack.py > /dev/null 2 >& 1 &
tail -f log.txt

