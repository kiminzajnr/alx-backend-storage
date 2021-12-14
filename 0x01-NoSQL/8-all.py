#!/usr/bin/env python3
"""
Lists all documents in Python
"""


def list_all(mongo_collection):
    """List all documents in Python"""
    dct = []
    if mongo_collection.find() is None:
        return []
    else:
        for collection in mongo_collection.find():
            dct.append(collection)
    return dct
