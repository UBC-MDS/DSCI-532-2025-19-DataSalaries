from dash import Input, Output, callback
from .line_chart_trend import create_salary_trend_chart
from .bar_chart_experience import create_salary_by_experience_chart
from .donut_chart1_comp_size import create_salary_by_company_size_chart
from .donut_chart2_remote import create_salary_by_remote_type_chart
from .map_chart_location import create_salary_by_location_chart
from ..data.salary_data import load_clean_data

@callback(
    Output('salary-trend', "spec"),
    Output('salary-by-experience-level', "spec"),
    Output('salary-by-company-size', "spec"),
    Output('salary-by-remote-type', "spec"),
    Output('salary-by-location', "spec"),
    Input('year_filter', "value"),
    Input('job_filter', "value"),
    Input('exp_level_filter', "value"),
    Input('emp_type_filter', "value"),
    Input('remote_type_filter', "value"),
    Input('company_location_filter', "value")
)
def update_charts(selected_year, selected_jobs, selected_exp_levels, selected_emp_types, selected_remote_types, selected_locations):
    df_filtered = load_clean_data()

    # Apply year filter only for map and donut charts
    df_filtered_year = df_filtered[df_filtered["work_year"] == selected_year]

    # Apply filters for all charts
    if selected_jobs:
        df_filtered = df_filtered[df_filtered['job_title'].isin(selected_jobs)]
        df_filtered_year = df_filtered_year[df_filtered_year['job_title'].isin(selected_jobs)]
    if selected_exp_levels:
        df_filtered = df_filtered[df_filtered['experience_level'].isin(selected_exp_levels)]
        df_filtered_year = df_filtered_year[df_filtered_year['experience_level'].isin(selected_exp_levels)]
    if selected_emp_types:
        df_filtered = df_filtered[df_filtered['employment_type'].isin(selected_emp_types)]
        df_filtered_year = df_filtered_year[df_filtered_year['employment_type'].isin(selected_emp_types)]
    if selected_remote_types:
        df_filtered = df_filtered[df_filtered['remote_ratio'].isin(selected_remote_types)]
        df_filtered_year = df_filtered_year[df_filtered_year['remote_ratio'].isin(selected_remote_types)]
    if selected_locations:
        df_filtered = df_filtered[df_filtered['company_location'].isin(selected_locations)]
        df_filtered_year = df_filtered_year[df_filtered_year['company_location'].isin(selected_locations)]

    return(
        create_salary_trend_chart(df_filtered, selected_jobs),
        create_salary_by_experience_chart(df_filtered), 
        create_salary_by_company_size_chart(df_filtered_year),
        create_salary_by_remote_type_chart(df_filtered_year), 
        create_salary_by_location_chart(df_filtered_year),  
    )