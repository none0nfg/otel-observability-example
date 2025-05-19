FROM python:3.12.3

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE="observability.settings"

WORKDIR /django/observability/
COPY requirements.txt .
COPY docker/entrypoint.sh /
RUN python3 -m pip install -r requirements.txt

COPY . .

ENTRYPOINT [ "/entrypoint.sh", "gunicorn", "observability.wsgi:application" ]
CMD [ "-w 2", "-b 0.0.0.0:80" ]

EXPOSE 80/tcp