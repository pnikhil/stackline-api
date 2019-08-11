from api_error import BadRequest

def check_autocomplete_request(content):
    if "prefix" not in content or "type" not in content:
        raise BadRequest('Bad Request: type and prefix, both are required', 40001, {'ext': 1})
    if not content["prefix"]:
        raise BadRequest('Bad Request: Prefix cannot be empty', 40001, {'ext': 1})
    if not content["type"]:
        raise BadRequest('Bad Request: Type cannot be empty', 40001, {'ext': 1})
    return True


def check_search_request(content):
    if not content["conditions"]:
        raise BadRequest('Bad Request: Conditions cannot be empty', 40001, {'ext': 1})
    if not content["pagination"]:
        raise BadRequest('Bad Request: Pagination cannot be empty', 40001, {'ext': 1})

    if type(content["conditions"]) != list and type(content["conditions"]) != dict: #For single or multiple condition objects
        raise BadRequest('Bad Request: Conditions not in proper format', 40001, {'ext': 1})

    if "from" not in content["pagination"] or "size" not in content["pagination"]:
        raise BadRequest('Bad Request: Pagination not in proper format', 40001, {'ext': 1})

    if type(content["conditions"]) == list:
        for condition in content["conditions"]:
            if "type" not in condition or  condition["type"] == "":
                raise BadRequest('Type not specified for all conditions', 40001, {'ext': 1})

            if "values" not in condition or condition["values"] == "":
                raise BadRequest('Values not specified for all conditions', 40001, {'ext': 1})

    if type(content["conditions"]) == dict:
        if "type" not in content["conditions"] or content["conditions"]["type"] == "":
            raise BadRequest('Type not specified for conditions', 40001, {'ext': 1})

        if "values" not in content["conditions"] or content["conditions"]["values"] == "":
            raise BadRequest('Values not specified for conditions', 40001, {'ext': 1})

    return True

def check_keyword_request(content):
    if "keywords" not in content or len(content) != 1:
        raise BadRequest('Invalid input', 40001, {'ext': 1})

    if type(content["keywords"]) != list:
        raise BadRequest('Expecting a list for keywords', 40001, {'ext': 1})
    return True
