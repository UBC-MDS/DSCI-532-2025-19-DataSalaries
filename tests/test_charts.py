import pytest
import pandas as pd
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from src.callbacks.line_chart_trend import create_salary_trend_chart
from src.callbacks.bar_chart_experience import create_salary_by_experience_chart
from src.callbacks.update_charts import update_charts
from src.callbacks.donut_chart1_comp_size import create_salary_by_company_size_chart
from src.callbacks.donut_chart2_remote import create_salary_by_remote_type_chart
from src.callbacks.map_chart_location import create_salary_by_location_chart
from src.app import app 
from src.utils.cache import cache

@pytest.fixture(autouse=True)
def initialize_cache():
    """Ensure cache is properly initialized before running tests."""
    cache.init_app(app.server, config={"CACHE_TYPE": "simple"})
    cache.clear()  # Clear cache before running tests

@pytest.fixture
def sample_data():
    """Returns a sample DataFrame with necessary fields for testing charts."""
    return pd.DataFrame({
        "work_year": [2021, 2022, 2023],
        "salary_in_usd": [60000, 65000, 70000],
        "job_title": ["Data Scientist", "Data Analyst", "ML Engineer"],
        "experience_level": ["Entry-level", "Mid-level", "Senior-level"],
        "company_size": ["S", "M", "L"],
        "remote_ratio": [0, 50, 100],
        "company_location": ["US", "CA", "GB"]
    })

@pytest.fixture
def extreme_data():
    """Returns a DataFrame with extreme salary values for testing outliers."""
    return pd.DataFrame({
        "work_year": [2021, 2022, 2023],
        "salary_in_usd": [10000, 500000, 999999],  # Extreme salaries
        "job_title": ["Data Scientist", "Data Analyst", "ML Engineer"],
        "experience_level": ["Entry-level", "Mid-level", "Senior-level"],
        "company_size": ["S", "M", "L"],
        "remote_ratio": [0, 50, 100],
        "company_location": ["US", "CA", "GB"]
    })

@pytest.fixture
def missing_data():
    """Returns a DataFrame with missing values for testing robustness."""
    return pd.DataFrame({
        "work_year": [2021, None, 2023],
        "salary_in_usd": [None, 65000, 70000],
        "job_title": ["Data Scientist", "Data Analyst", None],
        "experience_level": ["Entry-level", None, "Senior-level"],
        "company_size": ["S", "M", None],
        "remote_ratio": [0, None, 100],
        "company_location": ["US", "CA", None]
    })

@pytest.fixture
def empty_data():
    """Returns an empty DataFrame for testing 'No data available' cases."""
    return pd.DataFrame(columns=[
        "work_year", "salary_in_usd", "job_title", "experience_level", 
        "company_size", "remote_ratio", "company_location"
    ])

def test_create_salary_trend_chart(sample_data):
    """Test that the function returns a valid Vega-Lite spec (dict)."""
    chart = create_salary_trend_chart(sample_data, selected_jobs=None)
    assert isinstance(chart, dict), "Function should return a dictionary"

def test_create_salary_by_experience_chart(sample_data):
    """Test that the function returns a valid Vega-Lite spec (dict) for experience levels."""
    chart = create_salary_by_experience_chart(sample_data)
    assert isinstance(chart, dict), "Function should return a dictionary"

def test_create_salary_by_company_size_chart(sample_data):
    """Test that the function returns a valid Vega-Lite spec (dict) for company size."""
    chart = create_salary_by_company_size_chart(sample_data)
    assert isinstance(chart, dict), "Function should return a dictionary"

def test_create_salary_by_remote_type_chart(sample_data):
    """Test that the function returns a valid Vega-Lite spec (dict) for remote work type."""
    chart = create_salary_by_remote_type_chart(sample_data)
    assert isinstance(chart, dict), "Function should return a dictionary"

def test_create_salary_by_location_chart(sample_data):
    """Test that the function returns a valid Vega-Lite spec (dict) for salary by location."""
    chart = create_salary_by_location_chart(sample_data)
    assert isinstance(chart, dict), "Function should return a dictionary"

def test_create_salary_by_experience_chart_extreme(extreme_data):
    """Test experience-level salary chart with extreme values."""
    chart = create_salary_by_experience_chart(extreme_data)
    assert isinstance(chart, dict), "Function should return a dictionary"

def test_create_salary_by_location_chart_missing(missing_data):
    """Test location chart handling missing values."""
    chart = create_salary_by_location_chart(missing_data)
    assert isinstance(chart, dict), "Function should return a dictionary"

def test_update_charts():
    """Test that the update_charts function runs without errors and returns expected outputs."""
    outputs = update_charts(
        selected_year=2023,
        selected_jobs=["Data Scientist"],
        selected_exp_levels=["Senior-level"],
        selected_emp_types=["Full-time"],
        selected_remote_types=[100],
        selected_locations=["US"]
    )
    assert len(outputs) == 5, "update_charts should return five outputs"
    assert all(isinstance(output, dict) for output in outputs), "Each output should be a dict (Vega-Lite JSON spec)"

def test_update_charts_empty_data(empty_data):
    """Test update_charts when there is no matching data."""
    outputs = update_charts(2023, [], [], [], [], [])
    assert len(outputs) == 5, "update_charts should still return five outputs"
    assert all(isinstance(output, dict) for output in outputs), "Each output should be a dict"
    expected_text = "No data available for the selected filters."
    assert all(
        "datasets" in output and isinstance(output["datasets"], dict)
        for output in outputs
    ), "All charts should have a valid Vega-Lite dataset when empty"