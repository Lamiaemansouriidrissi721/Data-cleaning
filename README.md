📞 Data Cleaning Project: Customer Call List 🧹

## Overview

This project focuses on cleaning and preprocessing a customer call list to prepare it for analysis. The dataset contains customer information, including names, contact details, and preferences. The primary objective is to standardize and clean the data to ensure accuracy and consistency.

## Project Structure

- `data/`: Contains the raw and cleaned datasets.
  - `raw/`: Original, unmodified data files.
  - `cleaned/`: Data files after cleaning and preprocessing.
- `scripts/`: Python scripts used for data cleaning.
  - `clean_data.py`: Main script for cleaning the dataset.
- `README.md`: This file.

## Data Cleaning Steps

1. **Import Libraries**:
   - Utilize `pandas` for data manipulation.

2. **Load Data**:
   - Read the Excel file `Customer Call List.xlsx` into a pandas DataFrame.

3. **Remove Unnecessary Columns**:
   - Drop columns that are not relevant to the analysis.

4. **Clean Specific Columns**:
   - Strip unwanted characters from the `Last_Name` column.
   - Standardize values in the `Do_Not_Contact` and `Paying Customer` columns by replacing 'Yes' with 'Y' and 'No' with 'N'.
   - Replace 'N/a' with an empty string in the DataFrame.

5. **Split Address Column**:
   - Separate the `Address` column into `Street_Address`, `State`, and `Zip_Code` based on commas.

6. **Handle Missing Values**:
   - Fill missing values with empty strings to prevent issues during processing.

7. **Remove Unwanted Rows**:
   - Drop rows where the `Do_Not_Contact` column has a value of 'Y'.
   - Remove duplicate rows from the DataFrame.
   - Drop rows where the `Phone_Number` column is empty.

## Requirements

- Python 3.x
- pandas library

## Usage

1. Place the `Customer Call List.xlsx` file in the `data/raw/` directory.
2. Run the `clean_data.py` script to process the data.
3. The cleaned dataset will be saved in the `data/cleaned/` directory.
