def get_auth_payload():
    json_payload = {"action": "signIn",
                    "data":
                        {"accountType": "TRELLO",
                         "trelloToken": "d3c54a73afc4ce1c48c95cf9959f1b842d700f3afb1f744e31068f7b2b9a4231"
                         }
                    }
    return json_payload


payload = get_auth_payload()
