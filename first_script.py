from googlesearch import search
import requests
from lxml.html import fromstring
import csv

def link_title(url):
    try:
        response = requests.get(url)
        tree = fromstring(response.content)
        return tree.findtext('.//title')
    except Exception as e:
        return "Failed to retrieve title"

def write_results_to_csv(results, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'URL'])  # Column headers
        for title, url in results:
            writer.writerow([title, url])

def main():
    company_query = "site:bezosearthfund.org/grants"
    print(company_query)
    print(" ")
    results = []
    for url in search(company_query, tld='com', lang='en', num=100, start=201, stop=300, pause=2.0):
        title = link_title(url)
        print("\t"+"#"+" "+title)
        print("\t"+url)
        print(" ")
        results.append((title, url))
    write_results_to_csv(results, 'search_results.csv')

if __name__ == '__main__':
    main()
