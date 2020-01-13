from tusk.utils.version import get_version

VERSION = (0, 0, 1, "alpha", 0)

__version__ = get_version(VERSION)


def setup(set_prefix=True):
    """
    Configure the settings (this happens as a side effect of accessing the
    first setting), configure logging and populate the app registry.
    Set the thread-local urlresolvers script prefix if `set_prefix` is True.
    """
    from tusk.apps import apps
    from tusk.conf import settings
    from tusk.utils.log import configure_logging

    configure_logging(settings.LOGGING_CONFIG, settings.LOGGING)
    apps.populate(settings.INSTALLED_APPS)
