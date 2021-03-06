import json


def json_into_dictionary(json_str):
    """
    (str) -> (dict)
    This function makes a dictionary from json string.
    """
    parsed = json.loads(json_str)
    return parsed


def find_name(parsed):
    """
    (dict) -> (str)
    This function finds a name in a dictionary generated by
    Twitter API response.
    """
    return parsed['name']


def find_location(parsed):
    """
    (dict) -> (str)
    This function finds a location in a dictionary generated
    by Twitter API response.
    """
    return parsed['location']


def find_nickname(parsed):
    """
    (dict) -> (str)
    This function finds a name in a dictionary generated by
    Twitter API response.
    """
    return parsed['screen_name']


def find_descriprion(parsed):
    """
    (dict) -> (str)
    This function finds a description in a dictionary
    generated by Twitter API response.
    """
    return parsed['description']


def find_time_zone(parsed):
    """
    (dict) -> (str)
    This function finds a description in a dictionary
    generated by Twitter API response.
    """
    return parsed['time_zone']


def find_photo(parsed):
    """
    (dict) -> (str)
    This function finds a link on a profile photo by parsed
    Twitter API response.
    """
    return parsed['profile_image_url']


def find_data(parsed, data_type='personal'):
    """
    (str, dict) -> (dict)
    This function parses parsed json file finding different data dictionaries
    """
    if data_type == 'personal':
        return {'name': find_name(parsed)}
    elif data_type == 'geo':
        return {'location': find_location(parsed)}
    elif data_type == 'n+f':
        return {'nick': find_nickname(parsed), 'full name': find_name(parsed)}
    elif data_type == 'map':
        return {'name': find_name(parsed), 'location': find_location(parsed), 'photo_link': find_photo(parsed),
                'description': find_descriprion(parsed), 'time_zone': find_time_zone(parsed)}
