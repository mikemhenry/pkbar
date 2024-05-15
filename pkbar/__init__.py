from .pkbar import Pbar, Kbar
from importlib.metadata import version


class DistributionNotFound(Exception):
    pass


try:
    __version__ = version(__name__)
except DistributionNotFound:
    # package is not installed
    pass

__all__ = ["Pbar", "Kbar"]
