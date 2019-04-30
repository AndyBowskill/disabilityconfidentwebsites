import requests
import bs4
import csv


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

    def csv_write_company(self, row):
        html = requests.get('https://www.google.co.uk/search?q=' + row[0])
        if html.status_code != 200:
            return False

        soup = bs4.BeautifulSoup(html.text, 'html.parser')
        link_elements = soup.select('.r a')

        try:
            website = self.get_website(link_elements)
            self.csv_writer.writerow([row[0], row[1], row[2], row[3], row[4], website])

        except:
            print('Error for the ' + row[0] + ' website.')
            return False

        return True

    def get_website(self, link_elements):
        website_found = False

        for link in [0, 1, 2]:

            href = link_elements[link].get('href')
            href = href.split('/')

            if self.is_website_valid(href):
                website_found = True
                break
            else:
                continue

        if website_found:
            website = href[3]
        else:
            website = ''

        return website

    def is_website_valid(self, href):

        if len(href) < 4:
            return False

        bad_websites = ['beta.companieshouse.gov.uk',
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
        website = href[3]

        for bad_website in bad_websites:
            if website == bad_website:
                return False

        return True

    def is_row_valid(self, row):
        if len(row) >= 6 and row[5] != '':
            return False
        else:
            return True

    def process(self, line_maximum):
        line_count = 0

        for row in self.csv_reader:

            line_count += 1

            if line_count > line_maximum:
                break

            print('Processing {}.'.format(line_count))

            if not self.is_row_valid(row):
                continue

            if line_count == 1:
                self.csv_write_header()
                continue
            else:
                if not self.csv_write_company(row):
                    continue

        self.csv_read_close()
        self.csv_write_close()


def main():
    find_website = FindDisabilityConfidentWebsite()
    find_website.process(20)


if __name__ == '__main__':
    main()
