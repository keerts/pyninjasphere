#created by: chico_000
#Project team: TechMasters


from jsonmodels.models import Base
from .last_state import lastState


class Channel(Base):
    'Channel of a device, contains info about the channel and supported methods/events'

    def __init__(self,  **kwargs):
        for keyword in ["topic", "schema", "supportedMethods", "supportedEvents", "id", "protocol",
                        "deviceId", "lastState"]:
            if keyword == "lastState":
                if kwargs[keyword] is not None:
                    setattr(self, keyword, lastState(**kwargs[keyword]))
            else:
                setattr(self, keyword, kwargs[keyword])


