#!/usr/bin/env python3
'''Module for retrieving and sorting students by their average score.
'''


def top_students(mongo_collection):
    '''Returns a cursor with students sorted by their average score in descending order.
    
    Each student's average score is calculated from the `topics.score` field.
    
    Args:
        mongo_collection: The MongoDB collection object containing student documents.
    
    Returns:
        A cursor that yields student documents sorted by average score, with the highest scoring students appearing first.
    '''
    student_detail = mongo_collection.aggregate(
        [
            {
                '$project': {
                    '_id': 1,
                    'name': 1,
                    'averageScore': {
                        '$avg': '$topics.score',
                    },
                    'topics': 1,
                },
            },
            {
                '$sort': {'averageScore': -1},
            },
        ]
    )
    return student_detail
