import requests
from bs4 import BeautifulSoup
import csv

# URL of the website to scrape
input_csv_path = 'bef_grants_search_results.csv'
output_csv_path = 'grant_information.csv'

def scrape_data(url):
    # Send a GET request
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    data_row = [url]

    # Get the project title
    selector = r'#main > section > div > div > div.grid.gap-responsive-xl-60.md\:grid-cols-10.md\:gap-0 > div.md\:col-span-3 > h1'
    project_title = soup.select_one(selector).text.strip() if soup.select_one(selector) else "Title not found"
    data_row.append(project_title)

    # Get the award date
    date_awarded_search = soup.find_all(string="Date Awarded")
    date_awarded = date_awarded_search[0].parent.find_next_sibling().text.strip() if date_awarded_search else "Date not available"
    data_row.append(date_awarded)

    # Get the amount granted
    amount_granted_search = soup.find_all(string="Amount Granted")
    amount_granted = amount_granted_search[0].parent.find_next_sibling().text.strip() if amount_granted_search else "Amount not available"
    data_row.append(amount_granted)

    # Program information
    program_information = []
    for keyword in ["Programs", "Program"]:
        programs_search = soup.find_all(string=keyword)
        if programs_search:
            try:
                program_parent = programs_search[0].parent
                program_sibling = program_parent.find_next_sibling()
                if program_sibling and program_sibling.text.strip():
                    program_information.append(program_sibling.text.strip())
            except Exception as e:
                print(f"Error for {keyword}:", str(e))
    program_info = " | ".join(program_information) if program_information else "No program information available"
    data_row.append(program_info)

    # Countries
    countries_search = soup.find_all(string="Countries")
    countries = countries_search[0].parent.find_next_sibling().text.strip() if countries_search else "Countries not available"
    data_row.append(countries)

    # Partners
    partners_search = soup.find_all(string="Partners")
    partners = partners_search[0].parent.find_next_sibling().text.strip() if partners_search else "Partners not available"
    data_row.append(partners)

    # Description
    main_div_content = soup.select_one('#main > div').text.strip() if soup.select_one('#main > div') else "No main content available"
    data_row.append(main_div_content)

    return data_row

# Start reading and processing URLs
with open(input_csv_path, newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    urls = [row['URL'] for row in reader if 'URL' in row]

# Open the output CSV file to append data
with open(output_csv_path, 'a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # If the file is newly created or empty, write a header
    writer.writerow(['Website', 'Project Title', 'Date Awarded', 'Amount Granted', 'Program Info', 'Countries', 'Partners', 'Description'])
    # Process each URL
    for url in urls:
        data_row = scrape_data(url)
        writer.writerow(data_row)
        print(f"Data appended for URL: {url}")

print("All data has been processed and written to grant_information.csv.")
