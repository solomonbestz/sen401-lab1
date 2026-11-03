"""
Helper Utilities Module
Calculates minimum and maximum score records.
"""

def get_highest_score(data):
    if not data:
        return None
    return max(data, key=lambda x: x["score"])

def get_lowest_score(data):
    if not data:
        return None
    return min(data, key=lambda x: x["score"])