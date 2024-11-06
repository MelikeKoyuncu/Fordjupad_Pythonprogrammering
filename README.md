# Gender Data Automation Project


## Overview
The primary objective of this project is to automate the process of fetching gender-related statistics from an external API (World Bank) and storing them in a SQL Server database for further analysis and reporting. The entire process is automated using a Python script that is scheduled to run at specific intervals via Task Scheduler or an equivalent task scheduling system.


## gender_statistics Project Structure

1. gender_automate.py # Main automation script that runs daily.

2. config.py          # Configuration file for SQL Server and selected indicators. 

3. gender_api.py      # Contains functions for fetching and transforming data from excel file.
   
4. database.py        # Manages SQL Server connection and data insertion. 

5. test_pipeline.py   # Unit tests for the functionality of the data pipeline. 

6. process.log        # Log file that records the process steps and errors.


## Indicators
The project uses the following World Bank indicators:

- **SP.POP.TOTL**: Population, total
- **SP.ADO.TFRT**: Adolescent fertility rate (births per 1,000 women ages 15-19)
- **SP.DYN.CONU.ZS**: Contraceptive prevalence, any method (% of married women ages 15-49)
- **SH.STA.BRTC.ZS**: Births attended by skilled health staff (% of total)
- **SL.TLF.CACT.FE.NE.ZS**: Labor force participation rate, female (% of female population ages 15+)
- **SE.PRM.UNER**: Children out of school, primary
- **SP.DYN.IMRT.IN**: Mortality rate, infant (per 1,000 live births)

## Technical Stack:
Programming Language: Python

## Libraries/Modules:
- wbgapi: A library to fetch data from the World Bank API.
- pandas: For data manipulation and transformation.
- sqlalchemy: For interacting with SQL Server (using pyodbc).
- pytest: For testing the functionality of the script.
- logging: For logging execution details and errors.
- openpyxl: If the Excel file (e.g., gender data.xlsx) is used for storing or loading data locally.

## Database: 
SQL Server (with ODBC connectivity)

## Automated Execution
Task Scheduler is used to automate the running of the script on a set schedule, ensuring the database is regularly updated with the latest data from the API.

## Logging
The project uses a logging mechanism to track the process. Logs are saved in process.log, which records the execution steps and any errors encountered.

## Testing
Unit tests are included in test_pipeline.py. Able to run the tests using pytest

