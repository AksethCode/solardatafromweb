

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.re-plus.com/see-whos-attending/")

table = driver.find_element(By.TAG_NAME, 'table')
if table:
        # Get the HTML content of the table
        table_html = table.get_attribute('outerHTML')
        
        # Use BeautifulSoup to parse the HTML
        soup = BeautifulSoup(table_html, 'html.parser')
        
        # Find all table rows (tr) and extract data
        table_data = []
        for row in soup.find_all('tr'):
            row_data = [cell.text.strip() for cell in row.find_all('td')]
            table_data.append(row_data)
        
        # Convert the table data into a Pandas DataFrame
        df = pd.DataFrame(table_data, columns=None)
        
        # Display the DataFrame
        print(df)
else:
      print("No table found")


driver.quit()
