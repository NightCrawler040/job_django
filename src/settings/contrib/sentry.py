import os
import sentry_sdk

from sentry_sdk.integrations.django import DjangoIntegration


USE_SENTRY = os.getenv("USE_SENTRY", default=False)
if USE_SENTRY:  # pragma: no cover
    sentry_kwargs = {
        "dsn": os.getenv("SENTRY_DSN"),
        # "environment": os.getenv("SENTRY_ENVIRONMENT"),
        "integrations": [DjangoIntegration()],
    }
    sentry_sdk.init(**sentry_kwargs)  # pylint: disable=abstract-class-instantiated
