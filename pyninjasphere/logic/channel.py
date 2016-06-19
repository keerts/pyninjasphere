from jsonmodels.models import Base
from pyninjasphere.logic.last_state import LastState


class Channel(Base):
    """
    Channel of a device, contains info about the channel
    and supported methods/events.
    """

    def __init__(self,  **kwargs):
        """
        Initializes a channel object by looping through
        the keywords in kwargs and setting them as attributes.
        :param kwargs: Dictionary containing a channel.
        """
        for keyword in ["topic", "schema", "supportedMethods",
                        "supportedEvents", "id", "protocol",
                        "deviceId", "lastState"]:
            if keyword == "lastState" and kwargs[keyword] is not None:
                kwargs[keyword] = LastState(**kwargs[keyword])
            setattr(self, keyword, kwargs[keyword])
