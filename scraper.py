#required libraries
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import pandas as pd

#Base url for site to scrape
base_url = "https://books.toscrape.com/catalogue/"
current_page = 1 #start from the first page
data = [] #list to store scraped data

#session object for efficient requests
session = requests.Session()
session.headers.update({"User-Agent": "Mozilla/5.0"}) #user agent to avoid blocking

#loop until there are no more pages
while True:
    print(f"Currently scraping page: {current_page}")
    url = f"{base_url}page-{current_page}.html"

    #fetch page with error handling
    try:
        resp = session.get(url, timeout=15)
    except requests.RequestException as e:
        print(f"Request failed on page {current_page}: {e}")
        break

    #stop if we reach a 404 code(page not found)
    if resp.status_code == 404:
        # no more pages
        break

    #parse the html page
    soup = BeautifulSoup(resp.text, "html.parser")
    #find all book containers
    all_books = soup.find_all("li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")
    if not all_books:
        # safety stop if no book found
        break

    #extract details for each book
    for book in all_books:
        img = book.find("img") # image element (contains title in alt attribute)
        a = book.find("a") # link element
        price_el = book.find("p", class_="price_color") #price element
        stock_el = book.find("p", class_="instock availability") #stock element

        #clean extracted values
        title = img.get("alt", "").strip() if img else ""
        href = a.get("href", "").strip() if a else ""
        link = urljoin(base_url, href)  # make absolute
        raw_price = price_el.get_text(strip=True) if price_el else ""
        price = raw_price.replace("£", "").replace(",", "")
        stock = stock_el.get_text(strip=True) if stock_el else ""

        #store details in a dictionary
        item = {
            "Title": title,
            "Link": link,
            "Price": price,
            "Stock": stock,
        }
        data.append(item) #add book data to list
        print(link) #print link to console as progress feedback

    # if there is no "next" pagination link, stop
    next_link = soup.select_one("li.next a")
    if not next_link:
        break
    #move to next page
    current_page += 1

# Save outputs into exel and csv in folder
save_path = "/home/khan/Documents/PythonProject/pythonBeautifulSoup/"
df = pd.DataFrame(data)

#write to excel and csv
df.to_excel(f"{save_path}books.xlsx", index=False)
df.to_csv(f"{save_path}books.csv", index=False)

print(f"Saved {len(df)} rows to {save_path}books.xlsx and {save_path}books.csv")
