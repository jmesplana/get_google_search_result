


# Download a List of Google Search Results in a CSV

## Overview
This project comprises two Python scripts designed to get a list of all the URLs needed to run a web scraper and automate the extraction of information from a website. The first script fetches a set of URLs from a specific site, and the second script updates this dataset by avoiding duplicates and appending new entries from subsequent searches.

## Why am I doing this?
Google has a python package that allows you to get a list of the search results. However, it is limited to 100 items which is why I needed to create 2 scripts to get a list of all websites (300+). 
I'm sure there is a more efficient way of doing this but I only had 4 hours to complete this task.

## Prerequisites
Before running these scripts, ensure you have Python 3.x installed, along with the following packages:
- `requests`: For making HTTP requests.
- `lxml`: For parsing HTML and XML documents.
- `googlesearch-python`: For performing Google searches.

You can install these dependencies using pip:
```bash
pip install requests lxml googlesearch-python
```

## Scripts Description

### Script 1: Initial Search Automation
This script searches for pages, fetches their titles and URLs, and saves them in a CSV file.

#### Functions:
- `link_title(url)`: Fetches and returns the page title from a given URL.
- `write_results_to_csv(results, filename)`: Writes the search results to a CSV file.

#### Main Process:
- Constructs a search query to fetch the first batch of URLs from the site's subpages.
- Saves the results in `search_results.csv`.

### Script 2: Grant Search Update
This script reads URLs from the initially created CSV file to ensure no duplicates are fetched in the subsequent searches. It then appends only new entries to an updated CSV file.

#### Functions:
- `read_urls_from_csv(filename)`: Reads URLs from a given CSV file to avoid fetching duplicates.
- `link_title(url)` and `write_results_to_csv(results, filename)`: Same as in the first script.

#### Main Process:
- Uses the list of previously fetched URLs to avoid duplicates.
- Updates the dataset with new entries and saves them in `updated_search_results.csv`.

## How to Run the Scripts

1. **Run the first script**:
   - Modify the `company_query` to match the site's URL.
   - Execute the script to fetch the initial set of URLs.
   ```bash
   python first_script.py
   ```

2. **Run the second script**:
   - Adjust the `start` and `stop` parameters based on the last fetched URL in the first script.
   - Execute the script to fetch additional URLs and avoid duplicates.
   ```bash
   python second_script.py
   ```

   Repeat this step as necessary by adjusting the `start` and `stop` parameters each time to fetch more results.

## Limitations
- Due to API limits, each script fetches a maximum of 100 URLs at a time. You will need to manually adjust the search parameters to cover all intended results.
- Change num to 100 to get 100 items
- Change start to 0 to start from 0 and end at 100 so you get 100 items
- Then change start to 101 and end to 200 and so on...

## License
Specify the license under which these scripts are released (e.g., MIT, GPL-3.0, etc.).

## Author
John Mark Esplana
```

