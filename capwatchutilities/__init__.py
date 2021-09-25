import warnings

from .__version__ import __version__

warnings.simplefilter('always', DeprecationWarning)


def hello(target="World"):
    print("Hello {}!".format(target))