import pytest
import pandas as pd
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.data.salary_data import load_clean_data

def test_load_clean_data():
    """Test that the function loads a DataFrame with the expected columns."""
    df = load_clean_data()
    
    # Ensure it's a DataFrame
    assert isinstance(df, pd.DataFrame)
    
    # Ensure essential columns exist
    expected_columns = {"work_year", "salary_in_usd", "job_title", "experience_level", "employment_type", "company_location"}
    assert expected_columns.issubset(df.columns)
    
    # Ensure DataFrame is not empty
    assert not df.empty