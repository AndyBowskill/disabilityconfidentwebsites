import unittest
import main


class TestFindDisabilityConfidentWebsite(unittest.TestCase):
    def setUp(self):
        self.find_website = main.FindDisabilityConfidentWebsite()

    def test_is_website_valid(self):
        href = ['', '', 'www.abc.com']
        isValid = self.find_website.is_website_valid(href)
        self.assertFalse(isValid)

        href = ['', '', '', 'www.youtube.com']
        isValid = self.find_website.is_website_valid(href)
        self.assertFalse(isValid)

        href = ['', '', '', 'www.product.co.uk']
        isValid = self.find_website.is_website_valid(href)
        self.assertTrue(isValid)

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