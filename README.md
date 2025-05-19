# Observability with OTEL

Simple django application with traces,metrics,logs for examples.

## Use

Just clone repository, and run `docker compose up -d` (Maybe few times in a row)


All interesting services will be exposed to your localhost interface:

* http://localhost/secpath/ - Application (Nginx that will proxy request)
* http://localhost:3000/    - Grafana (To check logs, metrics, and some traces) <b>admin:admin</b>
* http://localhost:16686/   - Jaeger (Pretty nice visualization of traces)
