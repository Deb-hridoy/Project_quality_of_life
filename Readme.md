# Quality of Life Index (2012–2026)

## Project Overview
This project scrapes Quality of Life Index data from Numbeo
and analyzes trends across countries from 2012 to 2026.

## Data Source
-https://www.numbeo.com/quality-of-life/rankings_by_country.jsp

## Setup Instructions

### 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/Project_quality_of_life.git
cd Project_quality_of_life

### 2. Create a virtual environment
python -m venv virenv
virenv\Scripts\activate

### 3. Install dependencies
pip install -r requirements.txt

### 4. Run the scraper
python website_scrapping.py

### 5. Run data processing
python data_prerocess.py