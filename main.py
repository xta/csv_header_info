# -*- coding: utf-8 -*-
"""Show CSV header info"""

import csv
import sys
from tabulate import tabulate

def stats(headers):
    """
    Returns header column data
    """

    rows = []

    for index, column in enumerate(headers):
        row = [column, index+1, index]
        rows.append(row)

    return rows

if __name__ == '__main__':

    with open(sys.argv[0]) as input_stream:
        READER = csv.reader(sys.stdin)

        INPUT_HEADERS = next(READER, None)
        if INPUT_HEADERS:
            COLUMNS = stats(INPUT_HEADERS)

            OUTPUT_HEADER = ["Column", "Position", "Index"]
            print(tabulate(COLUMNS, OUTPUT_HEADER, tablefmt="grid"))
