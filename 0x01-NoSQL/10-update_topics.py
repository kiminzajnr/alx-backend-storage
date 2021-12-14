#!/usr/bin/env python3
"""
Change school topics
"""


def update_topics(mongo_collection, name, topics):
    """changes all school topics based on the name"""
    if mongo_collection['name'] == name:
        mongo_collection['name'] = topics
    return mongo_collection
