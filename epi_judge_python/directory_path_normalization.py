from test_framework import generic_test


def shortest_equivalent_path(path: str) -> str:
    """
    ./../ -> ../
    .././ -> ../ -> if the stack is empty, push .. onto it. We cancel each .. out with every item on the stack

    1. Absolute paths (start with /)
    2. Relative paths

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

    return '/' + '/'.join(stack) if is_absolute else '/'.join(stack)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('directory_path_normalization.py',
                                       'directory_path_normalization.tsv',
                                       shortest_equivalent_path))
