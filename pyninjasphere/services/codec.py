import json
import logging
from pyninjasphere.logic.thing import Thing

_LOGGER = logging.getLogger(__name__)


class Codec:
    """ Decodes and encodes objects. """

    def __init__(self):
        pass

    @staticmethod
    def decode_things(encoded_things):
        """
        Decodes a json object to things.
        :param encoded_things: Encoded things.
        :return: Decoded things or an empty list if no things were found.
        """
        _LOGGER.debug("[SERVICES][CODEC] decode things")
        things = []
        try:
            json_obj = json.loads(encoded_things)
            things = [Thing(**thing_info) for thing_info in json_obj['data']]
        except UnicodeError as err:
            _LOGGER.error("A Unicode-related encoding or decoding error "
                          "occurred somewhere between " + err.start + " and " +
                          err.end + ". " + err.reason + " This error occured "
                          "while decoding " + err.object + " with " +
                          err.encoding + ".")
        except TypeError:
            _LOGGER.error("The json string is incorrect.")
        return things
