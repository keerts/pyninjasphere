#created by: Wilko
#Project team: TechMasters

import json
from pyninjasphere.logic.thing import Thing


class Codec:
    'Decodes and encodes objects'

    def __init__(self):
        pass


    def decode_things(self, string):
        print("[SERVICES][CODEC] decode things")

        json_obj = json.loads(string)
        things = [Thing(**thing_info) for thing_info in json_obj]

        return things

