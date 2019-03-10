__author__ = "Suyash Soni"
__email__ = "suyash.soni248@gmail.com"

import re
from util.constants import CMD_REGEX_PATTERNS

def _parse_cmd_(pattern, pattern_groups, data=None):
    """
    Parses a command(e.g. park, leave, status etc.) and returns the information(e.g. color, slot etc.) obtained by parsing.

    :param pattern: regex for the underlying command.
    :param pattern_groups: regex pattern groups for the underlying command.
    :param data: command to be parsed.
    :return: Parsed information.
    """
    match_obj = re.match(pattern, data)
    if match_obj:
        return {attr: match_obj.group(attr) for attr in pattern_groups}
    return None

def parse(data):
    """
    Parses **data** against all the commands' regex pattern.

    :param data: command to be parsed.
    :return: Tuple of command key(@see util.constants.Command) and dict representing parsed command's info.
     Returns `(None, None)` if data/cmd is invalid.
    """
    cmd_key = None
    parsed_cmd = None
    for _cmd_key, pattern_info in CMD_REGEX_PATTERNS.items():
        _parsed_cmd = _parse_cmd_(pattern_info.pattern, pattern_info.groups, data=data)
        if _parsed_cmd:
            cmd_key = _cmd_key
            parsed_cmd = _parsed_cmd
            break
    return cmd_key, parsed_cmd