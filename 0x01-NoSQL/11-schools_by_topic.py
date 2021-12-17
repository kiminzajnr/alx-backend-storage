#!/usr/bin/env python3
"""
List of schools by topic
"""


def schools_by_topic(mongo_collection, topic):
    """Return list of school having a specific topic"""
    schools = []
    for collection in mongo_collection.find():
        if collection.get("topics") is not None:
            if topic in collection.get("topics"):
                schools.append(collection)
    return schools
