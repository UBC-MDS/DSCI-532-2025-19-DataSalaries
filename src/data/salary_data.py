import pandas as pd

# Load dataset
def load_clean_data():
        """
        Load and clean the salary dataset from a preprocessed Parquet file.

        The function reads the dataset from a Parquet file, selecting only relevant columns. 
        It ensures that the `salary_in_usd` column is converted to a numeric type, handling 
        any potential errors during conversion.

        Returns
        -------
        pandas.DataFrame

        Example
        -------
        >>> df = load_clean_data()
        """
        df = pd.read_parquet("data/processed/processed_global_data_salary.parquet", columns=[
                'work_year', 'job_title', 'experience_level', 'employment_type', 
                'company_location', 'company_size', 'salary_in_usd', 'remote_ratio'])
        df['salary_in_usd'] = pd.to_numeric(df['salary_in_usd'], errors='coerce')
        return df