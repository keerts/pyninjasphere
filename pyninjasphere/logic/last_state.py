#created by: Wilko
#Project team: TechMasters

class lastState:
    'Laststate of a channel'

    def __init__(self,  **kwargs):
        for keyword in ["timestamp", "payload"]:
                setattr(self, keyword, kwargs[keyword])