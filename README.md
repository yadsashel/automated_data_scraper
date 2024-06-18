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

3. If you encounter permission issues on Termux or other environments, check the permissions of the `pip` executable:
    ```bash
    ls -l venv/bin/pip
    chmod +x venv/bin/pip
    ```

4. If permissions issues persist, you can install the dependencies globally or in your user directory without using a virtual environment. This is not recommended for production but can be a workaround.:
   ```bash
   pip install --user -r requirements.txt
   ```

5. If the above steps don't work, try recreating the virtual environment.

   ```bash
   deactivate
   rm -rf venv
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ``` 

6. Install Chrome WebDriver:
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
```

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request if you have any suggestions or improvements.

## Copyright and Rights
© 2024 Yazide Salhi. All rights reserved.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
