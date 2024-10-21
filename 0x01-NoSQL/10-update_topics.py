#!/usr/bin/env python3
""" Python function that changes all topics of a
school document based on the name"""


def update_topics(mongo_collection, name, topics):
    """ update a document based on the name  """
    collection = mongo_collection
    query = {"name": name}
    newvalue = {"$set": {"topics": topics}}

    collection.update_one(query, newvalue)
