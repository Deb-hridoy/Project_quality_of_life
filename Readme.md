# Quality of Life Index (2012–2026)

## Project Overview
The objective of this project is to gather data on the quality of life from 2012 to 2026 from this website [Link](https://www.numbeo.com/quality-of-life/rankings_by_country.jsp). Then, this data is used to visualize and understand the following questions using Tableau Dashboard:<br>
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

### 1. Clone the repository
`git clone https://github.com/YOUR_USERNAME/Project_quality_of_life.git`
cd Project_quality_of_life

### 2. Create a virtual environment
`python -m venv virenv`
`virenv\Scripts\activate`

### 3. Install dependencies
`pip install -r requirements.txt`

### 4. Run the scraper
`python website_scrapping.py`

### 5. Run data processing
`python data_prerocess.py`
