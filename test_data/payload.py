def get_auth_payload():
    json_payload = {"action": "signIn",
                    "data":
                        {"accountType": "TRELLO",
                         "trelloToken": "c56d6251fcdd4ff7470660fbcc678e312a1d6c5de5450374cba2fdc622e2787b"
                         }
                    }
    return json_payload


payload = get_auth_payload()
