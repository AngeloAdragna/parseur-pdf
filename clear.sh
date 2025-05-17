#!/bin/bash

# Ask the user for confirmation
read -p "Êtes-vous sûr de vouloir supprimer tous les fichiers .txt et .xml dans le répertoire courant ? (y/n) : " confirm

# Treat Enter (empty input) or 'y'/'Y' as confirmation
if [ -z "$confirm" ] || [ "$confirm" = "y" ] || [ "$confirm" = "Y" ]; then
    # Remove all local .txt files in the current directory
    rm -f ./CORPUS_TRAIN/*.txt ./CORPUS_TRAIN/*.xml
    rm -f ./CORPUS_TXT/*.txt ./CORPUS_TXT/*.xml
    rm -f ./CORPUS_XML/*.txt ./CORPUS_XML/*.xml
    rm -f ./CORPUS_TEST/*.txt ./CORPUS_TEST/*.xml
    rm -f ./CORPUS_TEST_TXT/*.txt ./CORPUS_TEST_TXT/*.xml
    rm -f ./CORPUS_TEST_XML/*.txt ./CORPUS_TEST_XML/*.xml
    echo "Tous les fichiers .txt et .xml ont été supprimés."
else
    echo "Opération annulée."
fi