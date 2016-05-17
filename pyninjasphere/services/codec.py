#created by: Wilko
#Project team: TechMasters

import json
from pyninjasphere.logic.thing import Thing


class Codec:
    """Decodes and encodes objects"""

    def __init__(self):
        pass

    @staticmethod
    def decode_things(string):
        """
        Decodes a json object to things
        :param string: encoded things
        :return: decoded things
        """
        print("[SERVICES][CODEC] decode things")
        json_obj = json.loads(string)
        things = [Thing(**thing_info) for thing_info in json_obj['data']]
        return things

