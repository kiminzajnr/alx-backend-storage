#!/usr/bin/env python3
"""
Change school topics
"""


def update_topics(mongo_collection, name, topics):
    """changes all school topics based on the name"""
    myquery = {"name": name}
    newvalues = {"$set": {"topics": topics}}
    mongo_collection.update(myquery, newvalues)
