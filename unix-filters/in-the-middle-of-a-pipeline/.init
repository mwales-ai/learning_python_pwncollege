#!/bin/bash

SEARCH_TERM="instruction"
BIGFILE="/challenge/DESCRIPTION.md"

LINE_NUM_INST=$(cat $BIGFILE | grep -in $SEARCH_TERM | tail -n 1 | cut -d':' -f 1)
NUM_LINES_TOTAL=$(wc -l $BIGFILE | cut -d' ' -f1)
NUM_LINE_TAIL=$(( $NUM_LINES_TOTAL - $LINE_NUM_INST + 1 ))
tail -n $NUM_LINE_TAIL $BIGFILE > /challenge/README.md

chmod 0644 /challenge/DESCRIPTION.md 

chmod 0600 /challenge/.eval_data/*
chmod 0700 /challenge/.eval_data



