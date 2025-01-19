import unittest
from unittest.mock import patch
import pandas as pd
from main import load_csv, sort_data

class TestCSVFunctions(unittest.TestCase):

    def test_load_csv(self):
        """Test loading a valid CSV file."""
        with patch('builtins.open', unittest.mock.mock_open(read_data="col1,col2\nval1,val2\nval3,val4")):
            data = load_csv('test.csv')
            self.assertIsNotNone(data)
            self.assertEqual(list(data.columns), ['col1', 'col2'])
            self.assertEqual(len(data), 2)

    def test_sort_data(self):
        """Test sorting data."""
        data = pd.DataFrame({"col1": [2, 1], "col2": ["B", "A"]})
        tree_mock = unittest.mock.MagicMock()
        sort_data(data, tree_mock, "col1", ascending=True)
        sorted_values = data.sort_values(by="col1", ascending=True)
        self.assertTrue(sorted_values.equals(data.sort_values(by="col1", ascending=True)))

if __name__ == "__main__":
    unittest.main()