import pandas as pd

# Load dataset
def load_clean_data():
    df = pd.read_csv("data/processed/processed_global_data_salary.csv")
    df['salary_in_usd'] = pd.to_numeric(df['salary_in_usd'], errors='coerce')
    df = df[['work_year', 'job_title', 'experience_level', 'employment_type', 
             'company_location', 'company_size', 'salary_in_usd', 'remote_ratio']]
    return df