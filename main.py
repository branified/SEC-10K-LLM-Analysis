from sec_edgar_downloader import Downloader
import re
from bs4 import BeautifulSoup
import os

def risk_factor_extract(input_file):
    # Read the content of the text file
    with open(input_file, "r", encoding="utf-8") as file:
        file_content = file.read()

    # Extract the company name and filing ID from the input file path
    _, company_name, _, filing_id, _ = input_file.split(os.path.sep)

    # Create the output directory if it doesn't exist
    insights_dir = os.path.join("insights", "risk-factors")
    os.makedirs(insights_dir, exist_ok=True)

    if company_name == "MSFT":
        # Use regular expressions to find the text between "Item 1A" and "Item 1B"
        match = re.search(r'ITEM\s+1A\.\s*RIS.*?K\s+FACTORS(.*?)ITEM\s+1B', file_content, re.DOTALL)

    elif company_name == "AAPL":
        match = re.search(r'Item\s+1A\.\s*(.*?)Item\s+1B', file_content, re.DOTALL)

    # Create the output file path
    output_file_path = os.path.join(insights_dir, f"{company_name}_risk_factor_insights.txt")

    if match:
        text_between_items = match.group(1).strip()

        # Write the risk factor text to the output file
        with open(output_file_path, "a", encoding="utf-8") as output_file:
            output_file.write(f"---{filing_id}---\n")
            output_file.write(text_between_items + "\n\n")
    else:
        # Write the error message to the output file
        with open(output_file_path, "a", encoding="utf-8") as output_file:
            output_file.write(f"No risk factor found for {company_name} - {filing_id}\n")

def extract_trends(input_file):
    pass

def html_to_text(input_file):
    # Extract company name, filing type, and filing ID from the input file path
    _, company_name, filing_type, filing_id, _ = input_file.split(os.path.sep)
    print(filing_id)

    with open(input_file, "r", encoding="utf-8") as file:
        html_content = file.read()

    # Parse HTML using BeautifulSoup
    soup = BeautifulSoup(html_content, 'lxml')
    print("Parsing HTML\n")
    # Extract text content
    text_content = []

    # Extract paragraphs
    paragraphs = soup.find_all('p')
    for paragraph in paragraphs:
        text_content.append(paragraph.get_text(separator='\n').strip())

    # Extract tables
    tables = soup.find_all('table')
    for table in tables:
        rows = table.find_all('tr')
        table_content = []
        for row in rows:
            cells = row.find_all(['th', 'td'])
            row_content = [cell.get_text().strip() for cell in cells]
            table_content.append(row_content)
        text_content.append(table_content)
    
    print(len(text_content))

    # Create the output directory if it doesn't exist
    output_path = os.path.join("extracted-text", company_name, filing_type, filing_id)
    os.makedirs(output_path, exist_ok=True)

    # Write the extracted text to a new file inside the output directory
    output_file_path = os.path.join(output_path, f"{filing_id}.txt")
    with open(output_file_path, "w", encoding="utf-8") as output_file:
        for item in text_content:
            if isinstance(item, str):
                output_file.write("Paragraph:\n")
                output_file.write(item + "\n\n")
            elif isinstance(item, list):
                output_file.write("Table:\n")
                for row in item:
                    output_file.write(str(row) + "\n")
                output_file.write("\n")

def iterate_sec_filings(root_dir, process_function):
    # Define a set to store folder names to exclude from HTML parsing

    # Iterate through each company folder (AAPL, MSFT, etc.)
    for company_folder in os.listdir(root_dir):
        company_path = os.path.join(root_dir, company_folder)
        if os.path.isdir(company_path):
            # Inside each company folder, look for the 10-K folder
            ten_k_folder = os.path.join(company_path, "10-K")
            if os.path.isdir(ten_k_folder):
                # Inside the 10-K folder, iterate through each filing folder
                for filing_folder in os.listdir(ten_k_folder):
                    filing_path = os.path.join(ten_k_folder, filing_folder)
                    if os.path.isdir(filing_path):
                        # Inside each filing folder, look for the text file
                        for file_name in os.listdir(filing_path):
                            if file_name.endswith(".txt"):
                                file_path = os.path.join(filing_path, file_name)
                                # Call the process function with the file path and output directory
                                process_function(file_path)
    return

def main():
    dl = Downloader("University of Denver", "john.alfred@du.edu")

    companies = ["AAPL", "MSFT"]

    for company in companies:
        dl.get("10-K", company, after="1995-01-01", before="2024-01-01")
    
    print("Downloaded SEC 10-K Filings")

    # HTML Parser
    iterate_sec_filings("sec-edgar-filings", html_to_text)
    print("Parsed")
    
    iterate_sec_filings("extracted-text", risk_factor_extract)
    print("Risk Factors extracted")

if __name__ == '__main__':
    main()