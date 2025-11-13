import logging, requests
from .config import settings

log = logging.getLogger("robust.monitor")

def alert_slack(message: str):
    if not settings.SLACK_WEBHOOK:
        log.debug("Slack webhook not configured.")
        return
    try:
        requests.post(settings.SLACK_WEBHOOK, json={"text": message}, timeout=3)
    except Exception:
        log.exception("Failed to send slack alert")

def alert_critical(exc: Exception, context: dict | None = None):
    msg = f"Critical error: {exc} | ctx: {context}"
    log.critical(msg)
    alert_slack(msg)
    # opcional: enviar email, webhook etc.
