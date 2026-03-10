from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

columns_name = ['Year', 'Rank', 'Country', 'Quality of Life Index', 'Purchasing Power Index', 'Safety Index', 'HealthCare Index', 'Cost of Living Index', 'Property Price to Income Ratio Index', 'Traffic Commute Time Index', 'Pollution Index', 'Climate Index']
years = ['2012-Q1', '2013-Q1', 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026]
data_table = []

for year in years:
    driver = webdriver.Chrome()
    url = f"https://www.numbeo.com/quality-of-life/rankings_by_country.jsp?title={year}"
    driver.get(url)
    time.sleep(5)
    tables_row = driver.find_elements(By.CSS_SELECTOR, "#t2 tbody tr")
    for row in tables_row:
        cols = row.find_elements(By.TAG_NAME, "td")
        data = [col.text for col in cols]
        data.insert(0, year)
        data_table.append(data)
    driver.close()

df = pd.DataFrame(data=data_table, columns=columns_name)
df.to_csv("Quality_of_life_Index_from_2012_to_2026.csv", index=False)