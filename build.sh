#!usr/bin/env bash

# Alert exit
set -e

# Install dependencies
pip install -r requirements.txt

# Static Files Collection (As Needed)
# If DISABLE_COLLECTSTATIC is set to 0 in your render.yaml,
# Render will handle this automatically.
# If you need full control or have specific requirements,
# you can uncomment the following line:
# python manage.py collectstatic --noinput

# Run db migrations
python manage.py migrate