from opentelemetry import trace
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.django import DjangoInstrumentor
from opentelemetry.instrumentation.sqlite3 import SQLite3Instrumentor

import os

# Configure the tracer provider
trace.set_tracer_provider(
    TracerProvider(
        resource=Resource.create({SERVICE_NAME: "observability"})
    )
)

# Set up OTLP exporter (HTTP)
otlp_exporter = OTLPSpanExporter(endpoint=os.environ.get("OTLP_TRACE_ENDPOINT", "http://otel:4318/v1/traces"))

# Add processor
trace.get_tracer_provider().add_span_processor(
    BatchSpanProcessor(otlp_exporter)
)

# Instrument Django
DjangoInstrumentor().instrument()
SQLite3Instrumentor().instrument()