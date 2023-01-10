import os

PATH = './testdir'


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    stack = [path]
    hits = []

    while len(stack) > 0:
        curr = stack.pop()
        if os.path.isdir(curr):
            children = [(os.path.join(curr, x)) for x in os.listdir(curr)]
            stack += children
        elif os.path.isfile(curr):
            if os.path.basename(curr).endswith(suffix):
                hits.append(curr)

    return hits


def returns_matches():
    """
    Test Case 1
    Results should be returned as a list of paths
    """
    query = '.h'
    expected_response = sorted(['./testdir/t1.h', './testdir/subdir5/a.h',
                                './testdir/subdir3/subsubdir1/b.h', './testdir/subdir1/a.h'])
    sorted_response = sorted(find_files(query, PATH))
    for index, entry in enumerate(expected_response):
        if (entry != sorted_response[index]):
            return False
    return True


def no_match():
    """
    Test Case 2
    A query which yields no results should return an empty list
    """
    query = '.xyz'
    expected_response_length = 0
    response = find_files(query, PATH)
    return len(response) == expected_response_length


def only_matches_files():
    """
    Test Case 3
    A valid response consists of a list of paths who's files end in the provided query 
    """
    query = 'r1/a.h'
    expected_response_length = 0
    response = find_files(query, PATH)
    return len(response) == expected_response_length


if __name__ == '__main__':
    print(returns_matches())
    # True
    print(no_match())
    # True
    print(only_matches_files())
    # True
