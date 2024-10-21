#!/usr/bin/env python3
"""  Python script that inserts a new document
in a collection based on kwargs """


def insert_school(mongo_collection, **kwargs):
    """ function inserts kwargs """
    school = mongo_collection.insert_one(kwargs)
    return school.inserted_id
