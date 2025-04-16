import contextlib

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class InstagramConfig(AppConfig):
    name = "downloaderinstagram.instagram"
    verbose_name = _("Instagram")

    def ready(self):
        with contextlib.suppress(ImportError):
            import downloaderinstagram.instagram.signals  # noqa: F401
