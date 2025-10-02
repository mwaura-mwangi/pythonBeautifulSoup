# Book Scraper with BeautifulSoup & Pandas

This project is a Python web scraper that extracts book information from [Books to Scrape](https://books.toscrape.com/), a sandbox site for practicing scraping techniques.  
It collects details such as **title, link, price, and stock status**, and saves them into both **Excel (`.xlsx`)** and **CSV (`.csv`)** formats.

---

## Features
- Scrapes all available pages from [Books to Scrape](https://books.toscrape.com/).
- Extracts:
  - Book Title  
  - Product Link (absolute URL)  
  - Price (numeric value, currency symbol removed)  
  - Stock Availability  
- Saves data into:
  - `books.xlsx` (Excel)
  - `books.csv` (CSV)
- Includes error handling and user-friendly console progress.

---

## Tech Stack
- **Python 3.12+**
- [Requests](https://pypi.org/project/requests/) – HTTP requests  
- [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/) – HTML parsing  
- [Pandas](https://pypi.org/project/pandas/) – Data handling  
- [OpenPyXL](https://pypi.org/project/openpyxl/) – Required by Pandas for Excel export  

---

## Project Structure
```

pythonBeautifulSoup/
│── scraper.py        # Main scraping script
│── books.xlsx        # Excel output
│── books.csv         # CSV output
│── requirements.txt  # Project dependencies
└── README.md         # Project documentation

````
---
## Installation & Setup
1. Clone this repository:

   git clone https://github.com/your-username/pythonBeautifulSoup.git
   cd pythonBeautifulSoup


2. Create and activate a virtual environment:

   python3 -m venv .venv
   source .venv/bin/activate   # Linux / macOS
   .venv\Scripts\activate      # Windows
   

3. Install dependencies:

   pip install -r requirements.txt
   

   Example `requirements.txt`:


   requests
   beautifulsoup4
   pandas
   openpyxl


---

## Usage

Run the scraper:

python scraper.py


The script will:

* Scrape all pages of the site
* Print progress in the terminal
* Save results in `books.xlsx` and `books.csv` inside the project folder

---

## Example Output

| Title                | Link                                                                                                                                                   | Price | Stock    |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ----- | -------- |
| A Light in the Attic | https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html | 51.77 | In stock |
| Tipping the Velvet   | https://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html       | 53.74 | In stock |

---

## Disclaimer

This scraper is built for **educational purposes only**.


