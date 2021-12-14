#!/usr/bin/env python3
"""
Insert a document
"""


def insert_school(mongo_collection, **kwargs):
    """inserts a new documents in collection based on kwargs"""
    mongo_collection.insert(kwargs)
    return kwargs.get("_id")
