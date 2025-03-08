# Interpol Scraper

This script is designed to scrape search results from the Interpol website using Selenium and BeautifulSoup. It initializes a headless Chrome WebDriver, performs a search based on a given keyword, and extracts relevant information from the search results.

## Requirements

- Python 3.6+
- Selenium
- BeautifulSoup4
- webdriver-manager

## Installation

1. Clone the repository or download the `interpol-scraper.py` file.

2. Install the required Python packages using pip:

    ```bash
    pip install selenium beautifulsoup4 webdriver-manager
    ```

## Usage

1. Ensure that you have Chrome installed on your system.

2. Run the [interpol-scraper.py](https://github.com/ininike/interpol_scraper/blob/main/interpol-scraper.py) script:

    ```bash
    python interpol-scraper.py
    ```

3. The script will perform a search on the Interpol website based on the keyword provided in the `search` method and print the extracted results.
