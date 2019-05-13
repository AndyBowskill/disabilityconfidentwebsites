import csv
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

    def csv_write_company(self, row):
        driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver')
        driver.get('https://www.google.co.uk/search?q=' + row[0])

        class_name = driver.find_elements_by_class_name('iUh30')

        for link in [0, 1, 2]:
            href_text = class_name[link].text
            if href_text is None:
                continue
            else:
                break

        self.csv_writer.writerow([row[0], row[1], row[2], row[3], row[4], href_text])

        return True

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
                if not self.csv_write_company(row):
                    continue

        self.csv_read_close()
        self.csv_write_close()


def main():
    find_website = FindDisabilityConfidentWebsite()
    find_website.process(0,10)


if __name__ == '__main__':
    main()
