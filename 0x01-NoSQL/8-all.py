#!/usr/bin/env python3
""" Connects to a mongodb db and list all the collections"""


def list_all(mongo_collection):
    """ list all documents in a collection """
    data = []
    for school in mongo_collection.find():
        data.append(school)
    return data
