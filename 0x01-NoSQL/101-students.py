#!/usr/bin/env python3
""" MongoDB Operations with Python using pymongo """


def top_students(mongo_collection):
    # sourcery skip: inline-immediately-returned-variable
    """ Returns all students sorted by average score """
    pipeline = [
        {
            "$project": {
                "name": 1,
                "scores": 1,
                "averageScore": {"$avg": "$scores"}
            }
        },
        {
            "$sort": {"averageScore": -1}
        }
    ]
    cursor = mongo_collection.aggregate(pipeline)
    students = list(cursor)
    return students

