#!/bin/bash
echo "Starting ETL as $(date)"
cd ~/currency_etl
source venv/bin/activate
python test.py
echo "ETL finished"
