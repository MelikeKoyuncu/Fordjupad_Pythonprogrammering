import pandas as pd                                                                                         

def read_excel(file_path):
    # Read the Excel file
    df = pd.read_excel(file_path)
    return df

def process_data(df):
    # Clean and process the data as needed

    df.rename(columns={
        'SP.POP.TOTL': 'total_population',
        'SP.ADO.TFRT': 'adolescent_fertility_rate',
        'SP.DYN.CONU.ZS': 'contraceptive_prevalence',
        'SH.STA.BRTC.ZS': 'births_attended_by_skilled_staff',
        'SL.TLF.CACT.FE.NE.ZS': 'labor_force_participation_female',
        'SE.PRM.UNER': 'children_out_of_school_primary',
        'SP.DYN.IMRT.IN': 'infant_mortality_rate'
    }, inplace=True)

    # Ensure numeric columns are of type float
    numeric_columns = [
        'total_population', 'adolescent_fertility_rate', 
        'contraceptive_prevalence', 'births_attended_by_skilled_staff', 
        'labor_force_participation_female', 'children_out_of_school_primary', 
        'infant_mortality_rate'
    ]
    
    for col in numeric_columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    return df
