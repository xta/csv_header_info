"""Header test cases"""

import unittest
import header

class HeaderTest(unittest.TestCase):
    """Header tests"""

    def test_stats(self):
        """Default stats behavior"""

        header_columns = ["col1", "col2"]
        actual = header.stats(header_columns)
        expected = [["col1", 1, 0], ["col2", 2, 1]]

        self.assertEqual(actual, expected)

    def test_stats_single_element(self):
        """only 1 element stats behavior"""

        header_column = ["title"]
        actual = header.stats(header_column)
        expected = [["title", 1, 0]]

        self.assertEqual(actual, expected)

    def test_stats_empty(self):
        """empty header stats behavior"""

        actual = header.stats(None)
        self.assertEqual([], actual)
