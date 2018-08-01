# -*- coding: utf-8 -*-


def load_valid_tokens() -> dict:
    """
    The auth. tokens are stored in a json file as keys with values as security levels.
    :return: dict[token_str] = access_level_int
    """
    import json

    with open('tokens.json') as file:
        valid_tokens = json.load(file)

    return valid_tokens


# Function to fetch and parse arguments from request and return them in a dict
def get_and_parse_args_from_request(arg_specs: dict) -> dict:
    """
    Takes specification dict for the args and verifies if the arguments exists, are of correct type, and extra checks.
    If no args were given, abort.
    :param arg_specs: dict with value names as keys and for every value the following keys: format, importance
    :return: dict with arg_name as key and value if correct and given
    """
    from flask import request
    from werkzeug.exceptions import abort

    values = dict()
    for arg_name, arg in arg_specs.items():

        # Get value of every argument formatted as given type
        val = request.args.get(arg_name, type=arg['type'])

        if arg['importance'] == 'required' and val is None:
            abort(400, description=f'Parameter "{arg_name}" required but not found')

        if val is not None:     # Do not check or add None values
            # Check integrity of argument, will abort if not fulfilled
            verify_argument(arg_name, val)

            values[arg_name] = val

    # If no args were given, abort
    if len(values) == 0:
        abort(400, description='No parameters were given, see the docs.')

    return values


def verify_argument(arg_name: str, val: str):
    from werkzeug.exceptions import abort
    import re

    # define regex
    REGEX_PHONE_NUMBER = re.compile(r'(\+\d{2})\d{9}')  # plus sign, 2 digits then 9 digits
    REGEX_PERSONNUMMER = re.compile(r'\d{8}-\d{4}')     # 8 digits, one dash, 4 digits
    REGEX_ZIP = re.compile(r'\d{4,6}')  # Norwegian and Danish post numbers are of len 4, Swedish of len 5

    if arg_name == 'C_PERSONNR' and re.match(REGEX_PERSONNUMMER, val) is None:
        abort(400, description=f'Parameter "{arg_name}" not valid, should be YYYYMMDD-XXXX')

    elif arg_name == 'C_PHONE' and re.match(REGEX_PHONE_NUMBER, val.strip(' ')) is None:
        abort(400, description=f'Parameter "{arg_name}" not valid, should be +XXYYYYYYYYY')

    elif arg_name in ['C_GIVENNAME', 'C_LASTNAME', 'C_REGISTERED_ADDRESS', 'C_CITY', 'C_KOMMUN', 'C_LAN', 'C_COUNTRY',
                      'ENROL_HOTEL', 'ENROL_CHANNEL'] and len(val) > 1 is False:
        abort(400, description=f'Parameter "{arg_name}" not valid, length should be > 1')

    elif arg_name == 'C_EMAIL' and '@' not in val and ' ' in val:
        abort(400, description=f'Parameter "{arg_name}" not valid, should contain @, and not spaces')

    elif arg_name == 'C_ZIP' and re.match(REGEX_ZIP, val.strip(' ')) is None:
        abort(400, description=f'Parameter "{arg_name}" not valid, should only contain numbers and be of length 4-6')

    elif arg_name in ['MEMBER', 'B2B_INFO'] and val not in [0, 1, '0', '1']:
        abort(400, description=f'Parameter "{arg_name}" not valid, should be 0 or 1')


def authenticate_token() -> str:
    """
    Fetches the token from the argument request url.
    Checks it towards the local tokens and returns access level for that token
    :return: int, access level
    """
    from werkzeug.exceptions import abort

    arg_specs = {
        'token':
            {
                'type': str,
                'importance': 'required'
            }
    }

    args = get_and_parse_args_from_request(arg_specs)
    token = args['token']

    valid_tokens = load_valid_tokens()

    if token not in valid_tokens:
        abort(401, description='The token you entered was not valid')
    else:
        return valid_tokens[token]


def get_search_column(requester):

    if requester == 'book_visit':
        search_column = 'C_PHONE'
    else:
        search_column = 'C_PERSONNR'

    return search_column


# Function to generate tokens
def generate_random_token(token_length=None) -> str:
    """
    Returns a randomly initated URL friendly string of length 'token_length'
    :param token_length: int, default TOKEN_LENGTH=20
    :return: str, token
    """
    from secrets import token_urlsafe
    from api import TOKEN_LENGTH

    if token_length is None:
        token_length = TOKEN_LENGTH

    return token_urlsafe(token_length)
