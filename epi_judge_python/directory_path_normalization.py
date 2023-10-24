from test_framework import generic_test


def shortest_equivalent_path(path: str) -> str:
    """
    ./../ -> ../
    .././ -> ../ -> if the stack is empty, push .. onto it. We cancel each .. out with every item on the stack

    1. Absolute paths (start with /)
    2. Relative paths

    - Split tokens by /
      - If you encounter a '.', continue 
      - If you encounter an alphanumeric, push it onto the stack (If its a directory w a name, we are going
      deeper/forward in our traversal)
      - If you encounter .., we are going backwards in traversal:
          - If the top of the stack is an alphanumeric, pop it and continue, cancelling out the forward traversal
          with a backward traversal.
          - Else, add the token to the stack.

    How does split work:
    '/' -> ['', '']
    '/a/' -> ['', 'a', '']
    'a/' -> ['a', '']

    Time: O(N)
    Space: O(N)

    """
    """
    ./../
    """
    stack = []

    is_absolute = path[0] == '/'
    for token in path.split('/'):
        if token == '' or token == '.':
            continue
        elif token == '..':
            if stack and stack[-1] != '..':
                stack.pop()
            else:
                stack.append(token)
        else:
            stack.append(token)

    result = '/'.join(stack)
    if is_absolute:
        result = '/' + result

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('directory_path_normalization.py',
                                       'directory_path_normalization.tsv',
                                       shortest_equivalent_path))
