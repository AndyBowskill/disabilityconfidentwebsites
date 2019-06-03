import unittest
import main


class TestFindDisabilityConfidentWebsite(unittest.TestCase):
    def setUp(self):
        self.find_website = main.FindDisabilityConfidentWebsite()

    def test_process_csv_company_website(self):
        isValid = self.find_website.process_csv_company_website('https://www.abc.com')
        self.assertTrue(isValid)

        isValid = self.find_website.process_csv_company_website(' ')
        self.assertFalse(isValid)

        isValid = self.find_website.process_csv_company_website('...')
        self.assertFalse(isValid)

        isValid = self.find_website.process_csv_company_website('https://www.youtube.com')
        self.assertFalse(isValid)

    def test_is_row_valid(self):
        row = ['zero', 'one', 'two', 'three', 'four', 'five']
        isValid = self.find_website.is_row_valid(row)
        self.assertFalse(isValid)

        row = ['zero', 'one', 'two', 'three', 'four', '']
        isValid = self.find_website.is_row_valid(row)
        self.assertTrue(isValid)

        row = ['zero', 'one', 'two', 'three', 'four']
        isValid = self.find_website.is_row_valid(row)
        self.assertTrue(isValid)

    def tearDown(self):
        self.find_website.csv_read_close()
        self.find_website.csv_write_close()


if __name__ == '__main__':
    unittest.main()