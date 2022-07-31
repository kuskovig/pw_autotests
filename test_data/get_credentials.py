import json
import os
import cerberus
from pathlib import Path


def validate_credentials(file):
    schema = {'username': {'type': 'string', 'required': True},
              'password': {'type': 'string', 'required': True}
              }
    v = cerberus.Validator(schema)
    result = v.validate(file)
    if not result:
        raise ValueError("credentials file does not fit the schema:\n"
                         "{\n'username': 'YOUR_USERNAME',\n'password': 'YOUR_PASSWORD'\n}")
    return result


def read_credentials(path=Path().absolute().joinpath("credentials.json")):
    if os.path.isfile(path):
        with open(path) as file:
            jsonfile = json.load(file)
            validate_credentials(jsonfile)
        return jsonfile
    else:
        raise IOError("credentials.json file was not found in current directory")


credentials = read_credentials()
