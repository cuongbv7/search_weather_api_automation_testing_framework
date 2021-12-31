import json
import sys

from requests.status_codes import codes
from exceptions import UnknownStatusError

PY3 = sys.version_info > (3,)

def is_json(data):
    try:
        json.loads(data)
    except (TypeError, ValueError):
        return False
    return True


def parse_named_status(status_code):
    """
    Converts named status from human readable to integer
    """
    code = status_code.lower().replace(' ', '_')
    code = codes.get(code)
    if not code:
        raise UnknownStatusError(status_code)
    return code


def json_pretty_print(content):
    """
    Pretty print a JSON object
    ``content``  JSON object to pretty print
    """
    temp = json.loads(content)
    return json.dumps(
        temp,
        sort_keys=True,
        indent=4,
        separators=(
            ',',
            ': '))


def is_string_type(data):
    if PY3 and isinstance(data, str):
        return True
    elif not PY3 and isinstance(data, unicode): # noqa
        return True
    return False

