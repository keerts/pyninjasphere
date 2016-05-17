#created by: Wilko
#Project team: TechMasters

class LastState:
    """The last state of a channel"""

    def __init__(self,  **kwargs):
        """
        Initializes a LastState object by looping through the keywords in kwargs and setting them as attributes.
        :param kwargs: Dictionary
        """
        for keyword in ["timestamp", "payload"]:
                setattr(self, keyword, kwargs[keyword])
