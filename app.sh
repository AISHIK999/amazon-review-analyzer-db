#!/usr/bin/env bash
cd ~/PycharmProjects/pythonProject || exit
. venv/bin/activate
python3 fetch_reviews.py
python3 clean_reviews.py
python3 sentiment_analyzer.py
python3 append_to_database.py