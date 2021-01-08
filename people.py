from datetime import datetime


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

PEOPLE = {
    "Andrey" : {
        "fname": "Andrey",
        "lname" : "Bolkonsky",
        "timestamp" : get_timestamp()
    },
    "Natasha" : {
        "fname": "Natasha",
        "lname" : "Rostova",
        "timestamp" : get_timestamp()
    },
    "Pier" : {
        "fname": "Pier",
        "lname" : "Bezuhov",
        "timestamp" : get_timestamp()
    }
}

# create a handler for read (GET) people
def read():
    """This function responds to /api/people with a complete list of people"""
    return [PEOPLE[key] for key in sorted(PEOPLE.keys())]
