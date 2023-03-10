def contains(data, target):
    for item in data:
        if item == target:               # found a match
            return True
    return False
