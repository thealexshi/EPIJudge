from test_framework import generic_test


def ss_decode_col_id(col: str) -> int:
    """
    A = 1, B = 2, Z = 26, AA = 27, AB = 28

    - Go through string back to front
    """
    res = 0
    place = 0
    for c in reversed(col):
       res += (26**place)*(ord(c) - ord('A') + 1)
       place += 1

    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spreadsheet_encoding.py',
                                       'spreadsheet_encoding.tsv',
                                       ss_decode_col_id))
