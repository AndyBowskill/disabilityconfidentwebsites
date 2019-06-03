import csv
import urllib.parse
from selenium import webdriver


class FindDisabilityConfidentWebsite:
    def __init__(self):
        self.csv_read_open()
        self.csv_write_open()

    def csv_read_open(self):
        self.read_csv_file = open('data/disabilityconfident.csv', 'r', encoding='Windows-1252')
        self.csv_reader = csv.reader(self.read_csv_file, delimiter=',')

    def csv_write_open(self):
        self.write_csv_file = open('data/disabilityconfidentwebsite.csv', 'w', encoding='Windows-1252', newline='')
        self.csv_writer = csv.writer(self.write_csv_file)

    def csv_read_close(self):
        self.read_csv_file.close()

    def csv_write_close(self):
        self.write_csv_file.close()

    def csv_write_header(self):
        self.csv_writer.writerow(['Business name', 'Town or city', 'Postcode', 'Sector', 'DC level', 'Website'])

    def process_csv_company_website(self, href_text):

        if href_text.find(' ') != -1:
            return False

        if href_text.find('...') != -1:
            return False

        bad_websites = ['www.indeed.co.uk',
                        'www.imdb.com',
                        'www.youtube.com',
                        'business.facebook.com',
                        'www.facebook.com',
                        'en-gb.facebook.com',
                        'www.instagram.com',
                        'www.tripadvisor.co.uk',
                        'www.tripadvisor.com',
                        'www.ebay.co.uk',
                        'www.yell.com',
                        'en.wiktionary.org',
                        'en.wikipedia.org',
                        'uk.linkedin.com',
                        'www.linkedin.com',
                        'companycheck.co.uk']

        if any(bad_website in href_text for bad_website in bad_websites):
            return False

        return True

    def csv_write_company(self, row):
        driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver')

        driver.get('https://www.google.co.uk/search?q=' +  urllib.parse.quote_plus(row[0]))
        class_name = driver.find_elements_by_class_name('iUh30')

        for link in [0, 1, 2]:
            href_text = class_name[link].text
            if self.process_csv_company_website(href_text):
                break
            else:
                href_text = ''
                continue

        self.csv_writer.writerow([row[0], row[1], row[2], row[3], row[4], href_text])

    def is_row_valid(self, row):
        if len(row) >= 6 and row[5] != '':
            return False
        else:
            return True

    def process(self, line_start, line_maximum):
        line_count = 0

        for row in self.csv_reader:

            line_count += 1

            if line_count < line_start:
                continue

            if line_count > line_maximum:
                break

            print('Processing {}.'.format(line_count))

            if not self.is_row_valid(row):
                continue

            if line_count == 1:
                self.csv_write_header()
                continue
            else:
                self.csv_write_company(row)
                continue

        self.csv_read_close()
        self.csv_write_close()


def main():
    find_website = FindDisabilityConfidentWebsite()
    find_website.process(11001, 11264)


if __name__ == '__main__':
    main()
