from background_task import background
from django.utils import timezone
from .models import Entry
import logging

logger = logging.getLogger("OTEL")
logging.basicConfig(level=logging.INFO)

@background(schedule=10)
def clean_expired_records():
    deleted_count, _ = Entry.objects.filter(expire__lt=timezone.now()).delete()
    logger.info(f"[Cleanup] Deleted {deleted_count} expired records.")


clean_expired_records(repeat=10)