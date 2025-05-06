#!/bin/bash

# Ask the user for confirmation
read -p "Are you sure you want to remove all .txt and .xml files in the current directory? (y/n): " confirm

# Treat Enter (empty input) or 'y'/'Y' as confirmation
if [ -z "$confirm" ] || [ "$confirm" = "y" ] || [ "$confirm" = "Y" ]; then
    # Remove all local .txt files in the current directory
    rm -f ./CORPUS_TRAIN/*.txt ./CORPUS_TRAIN/*.xml
    rm -f ./CORPUS_TXT/*.txt ./CORPUS_TXT/*.xml
    rm -f ./CORPUS_XML/*.xml ./CORPUS_XML/*.txt
    echo "All .txt and .xml files have been removed."
else
    echo "Operation canceled."
fi