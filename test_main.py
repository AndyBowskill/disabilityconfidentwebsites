import unittest
import main


class TestFindDisabilityConfidentWebsite(unittest.TestCase):

    def test_is_website_valid(self):
        find_website = main.FindDisabilityConfidentWebsite()

        href = ['', '', 'www.abc.com']
        isValid = find_website.is_website_valid(href)
        self.assertFalse(isValid)

        href = ['', '', '', 'www.youtube.com']
        isValid = find_website.is_website_valid(href)
        self.assertFalse(isValid)

        href = ['', '', '', 'www.product.co.uk']
        isValid = find_website.is_website_valid(href)
        self.assertTrue(isValid)

    def test_is_row_valid(self):
        find_website = main.FindDisabilityConfidentWebsite()

        row = ['zero', 'one', 'two', 'three', 'four', 'five']
        isValid = find_website.is_row_valid(row)
        self.assertFalse(isValid)

        row = ['zero', 'one', 'two', 'three', 'four', '']
        isValid = find_website.is_row_valid(row)
        self.assertTrue(isValid)

        row = ['zero', 'one', 'two', 'three', 'four']
        isValid = find_website.is_row_valid(row)
        self.assertTrue(isValid)


if __name__ == '__main__':
    unittest.main()