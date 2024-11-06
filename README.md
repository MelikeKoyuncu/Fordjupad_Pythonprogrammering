# Gender Data Automation Project


## Overview
This project automates the process of fetching, transforming, and storing gender-related data to SQL Server database. The automation script runs daily, ensuring that the latest data is always available for analysis.


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

  
## Requirements
To run this project, you'll need the following:

- Python 3.6 or higher
- Required Python packages:
  - pandas
  - wbgapi
  - sqlalchemy
  - pytest
  - pyodbc
  - SQL Server
  - 

## Logging
The project uses a logging mechanism to track the process. Logs are saved in process.log, which records the execution steps and any errors encountered.

## Testing
Unit tests are included in test_pipeline.py. Able to run the tests using pytest

