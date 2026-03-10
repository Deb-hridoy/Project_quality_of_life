# Quality of Life Index (2012–2026)

## Project Overview
The objective of this project is to gather data on the quality of life from 2012 to 2026 from this website ***[Link](https://www.numbeo.com/quality-of-life/rankings_by_country.jsp)***. Then, this data is used to visualize and understand the following questions using Tableau Dashboard:<br>
This project aims to answer the following questions:
- Which countries have the highest and lowest cost of living?
- Which countries improved their quality of life the most from 2012 to 2026?
- Is there a relationship between purchasing power and quality of life?
- How do property prices and the cost of living affect quality of life worldwide?
- How do pollution levels compare against safety across countries?
- How do healthcare and pollution levels compare in South Asian countries?

For visualizing and knowing more about the quality of life across the world, use [this link](https://public.tableau.com/views/TheGlobalLivingStandardsfrom2012to2026/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link).

## Findings from Dashboard
- Identified that Iceland and Ireland have the highest cost of living
  While Nigeria has the lowest
- Discovered that Kenya and Pakistan improved their quality of life
  the most over the years
- Found a positive relationship between purchasing power and
  quality of life, with Spain and Qatar as notable outliers
- Revealed that a higher quality of life does not always mean higher
  property prices, as seen in Israel and Oman
- Showed that Finland is the safest country despite moderate
  pollution levels
- Highlighted healthcare and pollution patterns specifically
  across South Asian countries, including Bangladesh

## Data Source
`-https://www.numbeo.com/quality-of-life/rankings_by_country.jsp`

## Setup Instructions
### 1. Open a folder
Create a folder as your desired location. Then go to that folder, and in the address bar of your newly created folder type `cmd`.

### 2. Clone the repository
After the terminal opens, type `git clone` and paste this `https://github.com/Deb-hridoy/Project_quality_of_life.git` and then type
`cd Project_quality_of_life`

### 2. Create a virtual environment
Create a virtual environment by typing this code `python -m venv virenv` and then activate environment by using this code `virenv\Scripts\activate`

### 3. Install dependencies
Install required packages by using this code `pip install -r requirements.txt`

### 4. Run the scraper
Run this code `python website_scrapping.py` to scrape the website and get the data.

### 5. Run data processing
Preprocess the data using this code `python data_prerocess.py`. Finally, the dataset is ready for analysis.
