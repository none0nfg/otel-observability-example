#!/bin/sh

# Set the Django project root
DJANGO_ROOT="/django/observability"

# Activate the virtual environment (if needed)
# source /path/to/venv/bin/activate

# Navigate to the project directory
cd "$DJANGO_ROOT" || exit 1

# Make and apply migrations
echo "Making migrations..."
python manage.py makemigrations

echo "Applying migrations..."
python manage.py migrate

sleep 10 && echo "[Cleanup] Starting cleaner" && python manage.py process_tasks &

# Run additional command passed to the script
if [ "$#" -gt 0 ]; then
    echo "Running: $@"
    exec "$@"
fi