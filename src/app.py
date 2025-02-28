from dash import Dash, dash_table, dcc, callback, Input, Output, html
import dash_bootstrap_components as dbc
import dash_vega_components as dvc
from vega_datasets import data
import pandas as pd
import altair as alt

# Load dataset
df = pd.read_csv("data/raw/global_data_salary.csv")

# Convert salary to numeric and filter necessary columns
df['salary_in_usd'] = pd.to_numeric(df['salary_in_usd'], errors='coerce')
df = df[['work_year', 'job_title', 'experience_level', 'employment_type', 'company_location', 'company_size', 'salary_in_usd']]

# Initialize Dash app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

# Components
title = html.H1(
    'Data Science Salary Dashboard',
    style={
        'backgroundColor': 'steelblue',
        'padding': 20,
        'color': 'white',
        'margin-top': 20,
        'margin-bottom': 20,
        'text-align': 'center',
        'font-size': '48px',
        'border-radius': 3,
        'margin-left': -10,
    }
)

# Trend line graph
salary_trend = dvc.Vega(
    id='salary-trend',
    opt={'actions': False},
    style={'width': '100%'}
)

# Bar chart for average salary by experience level (clustered by year)
salary_by_experience_level = dvc.Vega(
    id='salary-by-experience-level',
    opt={'actions': False},
    style={'width': '100%'}
)

# Donut chart for average salary by company size
salary_by_company_size = dvc.Vega(
    id='salary-by-company-size',
    opt={'actions': False},
    style={'width': '100%'}
)

# Sidebar with filters
sidebar = dbc.Col([
    html.H5('Filters'),
    html.Br(),
    dcc.Dropdown(
        id='job_filter',
        options=[{'label': job, 'value': job} for job in df['job_title'].dropna().unique()],
        multi=True,
        placeholder="Select Job Title"
    ),
    html.Br(),
    dcc.Dropdown(
        id='exp_level_filter',
        options=[{'label': exp_level, 'value': exp_level} for exp_level in df['experience_level'].dropna().unique()],
        multi=True,
        placeholder="Select Experience Level"
    ),
    html.Br(),
    dcc.Dropdown(
        id='emp_type_filter',
        options=[{'label': emp_type, 'value': emp_type} for emp_type in df['employment_type'].dropna().unique()],
        multi=True,
        placeholder="Select Employment Type"
    )
],
    md=3,
    style={
        'background-color': '#E6E6E6',
        'padding': 10,
        'border-radius': 3,
    }
)

# Layout
app.layout = dbc.Container([
    dbc.Row(dbc.Col(title)),
    dbc.Row([
        sidebar,
        dbc.Col([
            dbc.Row([dbc.Col(salary_trend)]),  # Keep the trend line graph
            dbc.Row([dbc.Col(salary_by_experience_level)]),  # Clustered bar chart for salary by experience level
            dbc.Row([dbc.Col(salary_by_company_size)]),  # Donut chart for salary by company size
        ],
        md=9),
    ])
])

@callback(
    Output('salary-trend', "spec"),
    Output('salary-by-experience-level', "spec"),
    Output('salary-by-company-size', "spec"),
    Input('job_filter', "value"),
    Input('exp_level_filter', "value"),
    Input('emp_type_filter', "value")
)
def update_charts(selected_jobs, selected_exp_levels, selected_emp_types):
    # Filter data based on selected filters
    df_filtered = df.copy()

    # Filter by job title if selected
    if selected_jobs:
        df_filtered = df_filtered[df_filtered['job_title'].isin(selected_jobs)]

    # Filter by experience level if selected
    if selected_exp_levels:
        df_filtered = df_filtered[df_filtered['experience_level'].isin(selected_exp_levels)]

    # Filter by employment type if selected
    if selected_emp_types:
        df_filtered = df_filtered[df_filtered['employment_type'].isin(selected_emp_types)]

    # **Trend Line Chart** - Average Salary per Year or by Job Title
    if not selected_jobs:
        # If no job title selected, show average salary per year
        avg_salary_per_year = df_filtered.groupby('work_year', as_index=False)['salary_in_usd'].mean()
        salary_trend_chart = alt.Chart(avg_salary_per_year).mark_line().encode(
            x=alt.X('work_year:O', title='Year'),
            y=alt.Y('salary_in_usd:Q', title='Average Salary in USD'),
            tooltip=[alt.Tooltip('salary_in_usd:Q', format="$,.0f")],
        ).properties(
            width=800,
            height=400,
            title="Average Salary Per Year"
        )
    else:
        # If job titles are selected, show salary trend by job title
        salary_trend_data = df_filtered.groupby(['work_year', 'job_title'], as_index=False)['salary_in_usd'].mean()
        salary_trend_chart = alt.Chart(salary_trend_data).mark_line().encode(
            x=alt.X('work_year:O', title='Year'),
            y=alt.Y('salary_in_usd:Q', title='Average Salary in USD'),
            color='job_title:N',
            tooltip=[alt.Tooltip('salary_in_usd:Q', format="$,.0f"), 'job_title', 'work_year']  # Format as currency
        ).properties(
            width=800,
            height=400,
            title="Salary Trend by Job Title"
        )

    # **Clustered Bar Chart** - Average Salary by Experience Level for each Year (Clustered)
    salary_by_experience_level_chart = alt.Chart(df_filtered).mark_bar().encode(
        x=alt.X('work_year:N', title='Year'),  # X-axis is the year
        y=alt.Y('mean(salary_in_usd):Q', title='Average Salary in USD'),  # Y-axis is the average salary
        color=alt.Color('experience_level:N', scale=alt.Scale(scheme='set2')),  # Distinct colors for experience levels
        column='experience_level:N',  # Group by experience level for clustered bars
        tooltip=[alt.Tooltip('mean(salary_in_usd):Q', format="$,.0f"), 'work_year', 'experience_level']  # Format as currency
    ).properties(
        width=100,  # Width for each bar
        height=300,
        title="Average Salary by Experience Level"
    )

    # **Donut Chart** - Average Salary by Company Size
    salary_by_company_size_data = df_filtered.groupby('company_size', as_index=False)['salary_in_usd'].mean()
    salary_by_company_size_chart = alt.Chart(salary_by_company_size_data).mark_arc(innerRadius=100).encode(
        theta=alt.Theta(field="salary_in_usd", type="quantitative", title="Average Salary in USD"),
        color=alt.Color('company_size:N', legend=alt.Legend(title="Company Size"), scale=alt.Scale(scheme='tableau20')),
        tooltip=[alt.Tooltip('mean(salary_in_usd):Q', format="$,.0f"), 'company_size']  # Format as currency
    ).properties(
        width=300,
        height=300,
        title="Average Salary by Company Size"
    )

    # Return all three charts
    return salary_trend_chart.to_dict(), salary_by_experience_level_chart.to_dict(), salary_by_company_size_chart.to_dict()

if __name__ == '__main__':
    app.run(debug=True)