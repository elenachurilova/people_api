from datetime import datetime

from flask import make_response
from werkzeug.exceptions import abort


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


def create(person):
    """This function creates a new person in the people list
        based on the passed in person data"""
    lname = person.get("lname")
    fname = person.get("fname")

    if fname not in PEOPLE and fname is not None:
        PEOPLE[fname.title()] = {
            "fname" : fname,
            "lname" : lname,
            "timestamp" : get_timestamp()
    }
        return make_response(
            f"{fname} successfully created", 201
        )
    else:
        abort(
            406,
            f"Person with first name {fname} already exists",
        )


def read_one(fname):
    """This function responds to a requests for
    /api/people/{fname} with one matching person from people

    :param fname:       first name of person to find
    :return:            person matching first name
    """
    if fname in PEOPLE:
        person = PEOPLE.get(fname)
    else:
        abort(
            404, f"Person with first name {fname} not found"
        )
    return person


def delete_one(fname):
    """
    This function deletes a person from the people structure
    :param fname:   first name of person to delete
    :return:        200 on successful delete, 404 if not found
    """

    if fname in PEOPLE:
        del PEOPLE[fname]
        return make_response(
            f"{fname} successfully deleted", 200
        )
    else:
        abort(404, f"Person with first name {fname} not found")


def update(fname, person):
    """This function updates an existing person in the people list

    :param fname:   first name of person to update in the people structure
    :param person:  person to update
    :return:        updated person structure
    """

    if fname in PEOPLE:
        PEOPLE[fname]["fname"] = person.get("fname")
        PEOPLE[fname]["lname"] = person.get("lname")

        return PEOPLE[fname]

    else:
        abort(
            404, f"Person with first name {fname} not found"
        )




