#created by: chico_000
#Project team: TechMasters


from jsonmodels.models import Base
from .device import Device


class Thing(Base):
    'Class for smart Things, used to identify things'

    def __init__(self, **kwargs):
        for keyword in ["id", "type", "name", "device", "deviceId", "location", "promoted"]:
            if keyword == "device":
                setattr(self, keyword, Device(**kwargs[keyword]))
            if keyword == "location":
                self.location = kwargs.get(keyword)
            else:
                setattr(self, keyword, kwargs[keyword])

