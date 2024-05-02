from googlesearch import search
import requests
from lxml.html import fromstring
import csv

def read_urls_from_csv(filename):
    urls = set()
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader, None)  # Skip the header
        for row in reader:
            urls.add(row[1])  # Assuming URL is in the second column
    return urls

def link_title(url):
    try:
        response = requests.get(url)
        tree = fromstring(response.content)
        return tree.findtext('.//title')
    except Exception as e:
        return "Failed to retrieve title"

def write_results_to_csv(results, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as file:  # Write mode to create new or overwrite existing
        writer = csv.writer(file)
        writer.writerow(['Title', 'URL'])  # Column headers
        for title, url in results:
            writer.writerow([title, url])

def main():
    input_filename = 'search_results.csv'  # Use the previously created CSV file
    output_filename = 'updated_search_results.csv'  # New file for updated results

    existing_urls = read_urls_from_csv(input_filename)
    new_results = []

    company_query = "site:xxxxx.org/grants"
    # Start at the 101st result
    for url in search(company_query, tld='com', lang='en', num=100, start=100, stop=200, pause=2.0):
        if url not in existing_urls:
            title = link_title(url)
            new_results.append((title, url))

    if new_results:
        write_results_to_csv(new_results, output_filename)
        print(f"Added {len(new_results)} new entries to the CSV.")
    else:
        print("No new URLs to add.")

if __name__ == '__main__':
    main()
