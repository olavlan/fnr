birth_numbers = \
[15081064528,24111088787,"09031188188",21051085563,26021170711] + \
[10077026652,25087014463,19037138013,13057039447,"08117048013"] + \
[26112684181,27054034321,"01025935175","03101157864",13070175228] + \
[13070175221,261126841811,34111088787,29021170711,"Monica Robertson"]

expected_validity = \
[True]*5 + \
[True]*5 + \
[True]*5 + \
[False]*5

expected_gender = \
["male"]*5 + \
["female"]*5 + \
["male", "male", "male", "female", "female"] + \
[-1]*5

expected_age = \
[14, 14, 13, 14, 13] + \
[54, 54, 53, 54, 54] + \
[0, 84, 65, 13, 23] + \
[-1]*5

expected_existence = \
[False]*5 + \
[False]*5 + \
[True]*5 + \
[-1]*5

expected_counts = {
    "female": 7,
    "male": 8,
    "total": 15
}

expected_detailed_counts = {
    "0-17": {
        "male": 6,
        "female": 1
    },
    "18-24": {
        "male": 0,
        "female": 1
    },
    "25-34": {
        "male": 0,
        "female": 0
    },
    "35-44": {
        "male": 0,
        "female": 0
    },
    "45-54": {
        "male": 0,
        "female": 5
    },
    "55-64": {
        "male": 0,
        "female": 0
    },
    "65-": {
        "male": 2,
        "female": 0
    }
}