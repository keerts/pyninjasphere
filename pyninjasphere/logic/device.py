#created by: chico_000
#Project team: TechMasters


from jsonmodels.models import Base
from .channel import Channel

class Device(Base):
    'Device, contains info about a device and it\'s channels'

    def __init__(self, **kwargs):
        for keyword in ["id", "naturalId", "name", "thingId", "channels", "signatures"]:
            if keyword == "channels":
                setattr(self, keyword, [Channel(**channel_info) for channel_info in kwargs[keyword]])
            else:
                setattr(self, keyword, kwargs[keyword])

