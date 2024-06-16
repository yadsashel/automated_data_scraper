# Website Technology Analyzer and Scraper

## Overview

This tool allows users to analyze the technologies used on a website and scrape the content of their choice (HTML, CSS, JavaScript). It saves the scraped content to a file in the user's Downloads directory, formatted for readability.

## Features

- Detects front-end technologies (HTML, CSS, JavaScript)
- Detects common back-end technologies (Apache, Nginx, IIS, PHP, ASP.NET, JSP, Python, Ruby, Node.js)
- Allows users to choose which technology content to scrape
- Saves scraped content to a file in the Downloads directory
- Formats the scraped content for better readability

## Requirements

- Python 3.x
- Requests
- BeautifulSoup
- Selenium
- Chrome WebDriver
- cssutils
- jsbeautifier

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/automated_data_scraper.git
    cd automated_data_scraper
    ```

2. Set up a virtual environment and install the dependencies:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3. Install Chrome WebDriver:
    - The script uses `webdriver-manager` to automatically install and manage Chrome WebDriver.

## Usage

1. Run the script:
    ```bash
    python scraper.py
    ```

2. Follow the prompts to enter the URL and choose the technology to scrape.

3. The scraped content will be saved in a file in your Downloads directory.

## Example

```bash
$ python scraper.py
Welcome to the Website Technology Analyzer and Scraper!
Please enter the URL of the website you want to analyze: https://example.com
Technologies detected on the website:
Front-end:
- HTML
- CSS
- JavaScript
Back-end:
- PHP
- Apache

Please choose which technology content you want to scrape:
1. HTML
2. CSS
3. JavaScript
4. PHP
5. Apache
Enter the number corresponding to your choice: 1
Content saved to /Users/YourUsername/Downloads/scraped_html.txt
