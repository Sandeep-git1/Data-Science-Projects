import os
import requests
from bs4 import BeautifulSoup
import time

BASE_URL = "https://www.nirfindia.org"
YEARS = range(2020, 2026)
DOMAINS = ["Engineering", "Law", "Research", "Overall"]

# Create directory structure
def create_directories():
    for year in YEARS:
        for domain in DOMAINS:
            os.makedirs(f"NIRF/{year}/{domain}", exist_ok=True)

# Download PDF with timeout and retry handling
def download_pdf(url, file_path):
    try:
        response = requests.get(url, timeout=30, stream=True)
        response.raise_for_status()
        with open(file_path, "wb") as f:
            f.write(response.content)
        print(f"Downloaded: {file_path}")
    except requests.exceptions.Timeout:
        print(f"Timeout error for {url}. Retrying once...")
        try:
            response = requests.get(url, timeout=45, stream=True)
            response.raise_for_status()
            with open(file_path, "wb") as f:
                f.write(response.content)
            print(f"Downloaded on retry: {file_path}")
        except requests.RequestException as retry_error:
            print(f"Failed to download {url} after retry: {retry_error}")
    except requests.RequestException as e:
        print(f"Failed to download {url}: {e}")

# Scrape PDFs for a year and domain
def scrape_pdfs(year, domain):
    if domain == "Research":
        if year == 2020:
            print(f"Research domain not available for {year}, skipping...")
            return
        else:
            domain_url = "ResearchRanking"
    else:
        domain_url = f"{domain}Ranking"
    
    url = f"{BASE_URL}/Rankings/{year}/{domain_url}.html"
    save_dir = f"NIRF/{year}/{domain}"
    
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Find PDF links
        for link in soup.find_all("a", href=lambda href: href and ".pdf" in href.lower()):
            pdf_url = link["href"]
            if not pdf_url.startswith("http"):
                pdf_url = f"{BASE_URL}/{pdf_url.lstrip('/')}"
            file_name = os.path.basename(pdf_url).replace("%20", "_")
            file_path = os.path.join(save_dir, file_name)
            
            if not os.path.exists(file_path):
                download_pdf(pdf_url, file_path)
            else:
                print(f"Already exists: {file_path}")
        
        # Download annual report
        archive_url = f"{BASE_URL}/nirfpdfcdn/{year}/pdf/Report/IR{year}_Report.pdf"
        file_path = os.path.join(save_dir, f"IR{year}_Report.pdf")
        if not os.path.exists(file_path):
            download_pdf(archive_url, file_path)
        
        time.sleep(2)  # Rate limiting
        
    except requests.RequestException as e:
        print(f"Failed to access {url}: {e}")

# Main execution
def main():
    create_directories()
    for year in YEARS:
        for domain in DOMAINS:
            print(f"Scraping {year} - {domain}")
            scrape_pdfs(year, domain)

if __name__ == "__main__":
    main()