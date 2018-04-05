"""Header column helper(s)"""

def stats(headers):
    """
    Returns header column data
    """

    rows = []

    if headers is None:
        return rows

    for index, column in enumerate(headers):
        row = [column, index+1, index]
        rows.append(row)

    return rows
