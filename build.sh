#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r requirements.txt

# Convert static asset files
python manage.py collectstatic --no-input

# Apply any outstanding database migrations
python manage.py migrate

# Simplify test or demo deployments by automatically ensuring a superuser always exists
# (In real production: It’s generally better to remove this line and create a superuser manually)
python manage.py createsuperuser --no-input     