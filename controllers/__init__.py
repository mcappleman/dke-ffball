"""Base Controller Module"""

class BaseController(object):
    """Base Controller to be extended by every other controller"""

    __abstract__ = True

    def __init__(self, *args):
        pass
