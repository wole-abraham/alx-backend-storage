#!/usr/bin/env python3
""" Python script returns a list of school  """


def schools_by_topic(mongo_collection, topic):
    """ returns document with topic """
    return mongo_collection.find({"topic": topic})
