class LastState:
    """ The last state of a channel. """

    def __init__(self,  **kwargs):
        """
        Initializes a LastState object by looping through the keywords in
        kwargs and setting them as attributes.
        :param kwargs: Dictionary with timestamp and payload.
        """
        for keyword in ["timestamp", "payload"]:
            setattr(self, keyword, kwargs[keyword])
