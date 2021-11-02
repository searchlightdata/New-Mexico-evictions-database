# Analysis of New Mexico Eviction Data  — 01/2010 to 08/2021

This repository contains data, analytic code, and findings that support portions of the article, “Evictions Epidemic (https://searchlightnm.org/eviction-epidemic),” published November 2, 2021. Please read that article, which contains important context and details, before proceeding.

## Data

This analysis uses the following spreadsheets:
- [`data/eviction_cases/allCases_2010_anonymized.csv`](data/eviction_cases/allCases_2010_anonymized.csv), [`data/eviction_cases/allCases_2011_anonymized.csv`](data/eviction_cases/allCases_2011_anonymized.csv), etc. which contain all eviction cases from the past ten years. The data was collected from New Mexico's electronic court records website, Secured Odyssey Public Access (SOPA). For 51 cases, the courts did not list a plaintiff. While these cases were included in overall tallies, they did not factor into charts of top evictors.

- [`data/walkover_cleaned_names.csv`](data/walkover_cleaned_names.csv) Where appropriate, New Mexico Searchlight also combined several company names for the 50 plaintiffs who filed the most evictions in the past ten years, based on reporting.

## Methodology

### Scraping and Parsing
The data for this project was gathered using the scraper and a parser.

The scraper [`scripts/scraper.py`](scripts/scraper.py) was used to search New Mexico's electronic court records website, Secured Odyssey Public Access (SOPA), for eviction filings and to download summary pages. The scraper used a 'wildcard' search that includes the court location, case type, and year.
- Court locations include all magistrate courts and Bernallilo Metropolitan court.
- Case types include the following categories: `Landlord Tenant`, `Mobile Home Park`, `Forcible Detainer`, and `Interpleader`. These are the types of cases that Samuel Taub, a law student at University of New Mexico, is using to track evictions. He describes that methodology [here](https://www.nmevictions.org/?page_id=903). 
- Years for each search are hardcoded in. We began in 2010 and gathered data from each year, with the exception of 2021. In 2021, we ran the scraper for all months up to August 24th.

After scraping case summary pages from SOPA, the parser [`scripts/parser.py`](scripts/parser.py) extracted important information from each case summary. This information includes details such as the parties involved, the date the case was filed, and the name of the judicial officer. The parser then writes that information into `.csv` files for each year. The CSV files in [`eviction_cases`](eviction_cases) are the results of the scraping and parsing process.

### Cleaning and Analysis
The notebook [`notebooks/01-newmexico-eviction-analysis.ipynb`](notebooks/01-newmexico-eviction-analysis.ipynb) performs the following analyses:

- first it filters out irrelevant cases, ones that aren't `Landlord Tenant`, `Mobile Home Park`, `Forcible Detainer`, and `Interpleader` but were pulled down in the process of scraping.
- then it cleans the data, replacing any plaintiff names identified by a New Mexico Searchlight reporter as names with typos or improper spellings with cleaned-up and harmonized names, using the [`data/walkover_cleaned_names.csv`](data/walkover_cleaned_names.csv) spreadsheet. For instance, eviction cases that named “T and C management” and “T and C management LLC” as plaintiffs were combined into the same category based on reporting. This sheet contains information on how these names were harmonized.
- then it runs a series of analyses and produces multiple outputs, including the following:
  - [`output/top_evictors_all_time.csv`](output/top_evictors_all_time.csv) — a list of all plaintiffs by count of evictions filed
  - [`output/top_pandemic_evictors.csv`](output/top_pandemic_evictors.csv) — a list of all plaintiffs by count of evictions filed since the pandemic. This analysis uses March 11, 2020 as the beginning of the pandemic in New Mexico, the day when the state announced its first case.
  - [`output/monthly_evictions.csv`](output/monthly_evictions.csv) - a monthly tally of evictions

The notebook also produces analyses for reporting purposes that include defendant names. New Mexico Searchlight did not publish the details of these defendants to protect their identity. 

## Licensing

All code in this repository is available under the [MIT License](https://opensource.org/licenses/MIT). The data file in the output/ directory is available under the [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/) (CC BY 4.0) license. All files in the data/ directory are released into the public domain.

Nick Troutman contributed to the code for the scraper ['01-newmexico-eviction-scraper.ipynb'](01-newmexico-eviction-scraper.ipynb) and parser ['02-newmexico-eviction-parser.ipynb'](02-newmexico-eviction-parser.ipynb).

## Feedback / Questions?

Contact Dillon Bergin  at news.dillonbergin@gmail.com and Lam Thuy Vo at lam.vo@journalism.cuny.edu.
