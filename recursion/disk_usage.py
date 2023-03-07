import os

def disk_usage(path):
    """Return the number of bytes used by a file/folder and any descendents."""
    total = os.path.getsize(path)                      # account for direct usage
    if os.path.isdir(path):                            # if this is a directory,
        for filename in os.listdir(path):              # then for each child:
            childpath = os.path.join(path, filename)   # compose full path to child
            total += disk_usage(childpath)             # add child's usage to total

    print (f'{total:<7}\t{path}')                      # descriptive output (optional)
    return total                                       # return the grand total
