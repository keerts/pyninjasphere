# created by: chico_000
# Project team: TechMasters


from jsonmodels.models import Base
from .channel import Channel


class Device(Base):
    """Device, contains info about a device and it's channels"""

    def __init__(self, **kwargs):
        """
        Initializes a Device object by looping through the keywords in kwargs and setting them as attributes.
        :param kwargs: Dictionary
        """
        for keyword in ["id", "naturalId", "name", "thingId", "channels", "signatures"]:
            if keyword == "channels" and kwargs[keyword] is not None:
                kwargs[keyword] = [Channel(**channel_info) for channel_info in kwargs[keyword]]
            setattr(self, keyword, kwargs[keyword])
