def get_auth_payload():
    json_payload = {"action": "signIn",
                    "data":
                        {"accountType": "TRELLO",
                         "trelloToken": "//"
                         }
                    }
    return json_payload


payload = get_auth_payload()
