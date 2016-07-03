from jsonmodels.models import Base
from .device import Device


class Thing(Base):
    """ Class for smart Things, used to identify things. """

    keywords = ["id", "deviceId", "type", "name", "location", "promoted"]

    def __init__(self, **kwargs):
        """ Initializes a Thing """
        if "device" in kwargs and kwargs["device"] is not None:
            self.device = Device(**kwargs["device"])
        else:
            self.device = None
        for keyword in self.keywords:
            setattr(self, keyword, kwargs.get(keyword, ""))
