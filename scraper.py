import os
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pathlib import Path
import cssutils
import jsbeautifier

def detect_technologies(url, soup):
    frontend_techs = set()
    backend_techs = set()

    # Detect front-end technologies
    if soup.find('script', src=True):
        frontend_techs.add('JavaScript')
    if soup.find('link', rel='stylesheet') or soup.find('style'):
        frontend_techs.add('CSS')
    if soup.find_all():
        frontend_techs.add('HTML')

    # Backend detection
    response = requests.get(url)
    server_header = response.headers.get('Server', '').lower()
    powered_by_header = response.headers.get('X-Powered-By', '').lower()

    if 'apache' in server_header:
        backend_techs.add('Apache')
    if 'nginx' in server_header:
        backend_techs.add('Nginx')
    if 'iis' in server_header:
        backend_techs.add('IIS')
    if 'php' in powered_by_header or 'php' in response.text.lower():
        backend_techs.add('PHP')
    if 'asp.net' in powered_by_header:
        backend_techs.add('ASP.NET')
    if 'jsp' in response.text.lower() or 'java' in server_header:
        backend_techs.add('Java (JSP)')
    if 'python' in powered_by_header:
        backend_techs.add('Python')
    if 'ruby' in powered_by_header:
        backend_techs.add('Ruby')
    if 'node.js' in powered_by_header:
        backend_techs.add('Node.js')

    return list(frontend_techs), list(backend_techs)

def scrape_content(soup, tech_choice):
    content = ""
    if tech_choice == 'HTML':
        content = soup.prettify()
    elif tech_choice == 'CSS':
        styles = soup.find_all('style')
        links = soup.find_all('link', rel='stylesheet')
        for style in styles:
            content += style.get_text() + "\n"
        for link in links:
            href = link['href']
            if href.startswith('http'):
                css_response = requests.get(href)
                content += css_response.text + "\n"
        content = cssutils.parseString(content).cssText.decode('utf-8')
    elif tech_choice == 'JavaScript':
        scripts = soup.find_all('script')
        for script in scripts:
            if script.get('src'):
                src = script['src']
                if src.startswith('http'):
                    js_response = requests.get(src)
                    content += js_response.text + "\n"
            else:
                content += script.get_text() + "\n"
        content = jsbeautifier.beautify(content)

    return content

def save_content(content, filename):
    downloads_path = str(Path.home() / "Downloads")
    file_path = os.path.join(downloads_path, filename)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f'Content saved to {file_path}')

if __name__ == "__main__":
    print("Welcome to the Website Technology Analyzer and Scraper!")
    url = input("Please enter the URL of the website you want to analyze: ")

    # Set up Selenium WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run Chrome in headless mode
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    driver.get(url)
    response = driver.page_source
    soup = BeautifulSoup(response, 'html.parser')
    driver.quit()

    frontend_techs, backend_techs = detect_technologies(url, soup)
    
    if not frontend_techs and not backend_techs:
        print("Failed to detect any technologies on the provided website.")
    else:
        print("Technologies detected on the website:")
        if frontend_techs:
            print("Front-end:")
            for tech in frontend_techs:
                print(f"- {tech}")
        if backend_techs:
            print("Back-end:")
            for tech in backend_techs:
                print(f"- {tech}")

        print("\nPlease choose which technology content you want to scrape:")
        all_techs = frontend_techs + backend_techs
        for i, tech in enumerate(all_techs, start=1):
            print(f"{i}. {tech}")
        
        choice = int(input("Enter the number corresponding to your choice: "))
        if choice < 1 or choice > len(all_techs):
            print("Invalid choice.")
        else:
            tech_choice = all_techs[choice - 1]
            content = scrape_content(soup, tech_choice)
            if content:
                filename = f"scraped_{tech_choice.lower()}.txt"
                save_content(content, filename)
            else:
                print(f"No content found for {tech_choice}.")
