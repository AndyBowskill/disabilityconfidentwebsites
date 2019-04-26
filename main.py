import requests
import bs4
import csv


class FindWebsite:
    def __init__(self):
        self.csv_read_open()
        self.csv_write_open()

    def csv_read_open(self):
        self.read_csv_file = open('data/disabilityconfident.csv', 'r')
        self.csv_reader = csv.reader(self.read_csv_file, delimiter=',')

    def csv_write_open(self):
        self.write_csv_file = open('data/disabilityconfidentwebsite.csv', 'w', newline='')
        self.csv_writer = csv.writer(self.write_csv_file)

    def csv_read_close(self):
        self.read_csv_file.close()

    def csv_write_close(self):
        self.write_csv_file.close()

    def process_csv_header(self):
        self.csv_writer.writerow(['Business name', 'Town or city', 'Postcode', 'Sector', 'DC level', 'Website'])

    def process_csv_company(self, row):
        html = requests.get('https://www.google.co.uk/search?q=' + row[0])
        if html.status_code != 200:
            return False

        soup = bs4.BeautifulSoup(html.text, 'html.parser')
        link_elements = soup.select('.r a')

        try:
            website_found = False

            for link in [0, 1, 2]:

                href_text = link_elements[link].get('href')
                all_text = href_text.split('/')

                if self.process_csv_company_website(all_text):
                    website_found = True
                    break
                else:
                    continue

            if website_found:
                website_text = all_text[3]
            else:
                website_text = ''

            self.csv_writer.writerow([row[0], row[1], row[2], row[3], row[4], website_text])

        except:
            print('Error for the ' + row[0] + ' website.')
            return False

        return True

    def process_csv_company_website(self, all_text):

        if len(all_text) < 4:
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
        website = all_text[3]

        for bad_website in bad_websites:
            if website == bad_website:
                return False

        return True

    def process(self):
        line_count = 0
        for row in self.csv_reader:

            line_count += 1
            print('Processing {}.'.format(line_count))

            if len(row) >= 6 and row[5] != '':
                continue

            if line_count == 1:
                self.process_csv_header()
                continue
            else:
                if not self.process_csv_company(row):
                    continue

            if line_count + 1000 >= 3000:
                break

        self.csv_read_close()
        self.csv_write_close()



def main():
    fw = FindWebsite()
    fw.process()


if __name__ == "__main__":
    main()
