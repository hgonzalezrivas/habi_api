#!/usr/bin/env bash

set -ue

echo "Deploying Server"
gunicorn app:app --config deployment.py