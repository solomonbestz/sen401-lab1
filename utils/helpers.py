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


"""
Inventory Helper Utilities
"""
def highest_stock_item(items):
    return max(items, key=lambda x: x["quantity"]) if items else None

def lowest_stock_item(items):
    return min(items, key=lambda x: x["quantity"]) if items else None