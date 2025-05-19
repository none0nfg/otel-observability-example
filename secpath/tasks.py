from background_task import background
from django.utils import timezone
from .models import Entry
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

@background(schedule=10)
def clean_expired_records():
    deleted_count, _ = Entry.objects.filter(expire__lt=timezone.now()).delete()
    logger.info(f"[Cleanup] Deleted {deleted_count} expired records.")
