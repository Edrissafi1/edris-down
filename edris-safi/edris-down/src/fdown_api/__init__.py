from fdown_api.main import Fdown

from importlib import metadata

try:
    __version__ = metadata.version("fdown-api")

except metadata.PackageNotFoundError:
    __version__ = "1.0.0"

__repo__ = "https://t.me/edrissafi20"
__info__ = "Unofficial Python wrapper for fdown.net"

__all__ = ["Fdown"]
