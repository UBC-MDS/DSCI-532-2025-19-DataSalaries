import pandas as pd

# Load dataset
def load_clean_data():
    df = pd.read_parquet("data/processed/processed_global_data_salary.parquet", columns=[
            'work_year', 'job_title', 'experience_level', 'employment_type', 
            'company_location', 'company_size', 'salary_in_usd', 'remote_ratio'])
    df['salary_in_usd'] = pd.to_numeric(df['salary_in_usd'], errors='coerce')
    return df