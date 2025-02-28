from dash import Dash, dash_table, dcc, callback, Input, Output, html
import dash_bootstrap_components as dbc
import dash_vega_components as dvc
from vega_datasets import data
import pandas as pd
import altair as alt

# Load dataset
df = pd.read_csv("../data/raw/global_data_salary.csv")

# Convert salary to numeric and filter necessary columns
df['salary_in_usd'] = pd.to_numeric(df['salary_in_usd'], errors='coerce')
df = df[['work_year', 'job_title', 'experience_level', 'employment_type', 'company_location', 'company_size', 'salary_in_usd']]

# Initialize Dash app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

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

table = dash_table.DataTable(
    id='table',
    column_selectable="single",
    selected_columns=['salary_in_usd'], 
    page_size=5,
    sort_action='native',
    filter_action='native',
)

dropdown = dcc.Dropdown(
    id='dropdown',
    options=[{'label': col, 'value': col} for col in df.columns],
    value=['job_title', 'salary_in_usd', 'company_location'],
    multi=True
)

scatter = dvc.Vega(
    id='scatter',
    opt={'actions': False},
    style={'width': '100%'}
)

histogram = dvc.Vega(
    id='histogram',
    opt={'actions': False},
    style={'width': '100%'}
)

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
        'background-color': '#e6e6e6',
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
            dbc.Col([table]),
            dbc.Row([
                dbc.Col(histogram),
                dbc.Col(scatter),
            ]),
            dbc.Row([
                dbc.Col(dvc.Vega(id='line_chart', opt={'actions': False}))
            ])
        ],
        md=9),
    ])
])

@callback(
    Output('histogram', "spec"),
    Output('scatter', "spec"),
    Output('line_chart', "spec"),
    Input('job_filter', "value"), 
    Input('exp_level_filter', "value"), 
    Input('emp_type_filter', "value"), 
    prevent_initial_call=True
)

def update_charts(selected_jobs, selected_exp, selected_emp):
    print("Callback triggered!")  # Debugging statement
    
    df_filtered = df.copy()

    # Apply dropdown filters
    if selected_jobs:
        df_filtered = df_filtered[df_filtered['job_title'].isin(selected_jobs)]
    if selected_exp:
        df_filtered = df_filtered[df_filtered['experience_level'].isin(selected_exp)]
    if selected_emp:
        df_filtered = df_filtered[df_filtered['employment_type'].isin(selected_emp)]

    print(f"Filtered DataFrame shape: {df_filtered.shape}")  # Debugging statement

    if df_filtered.empty:
        print("Filtered DataFrame is empty!")
        return {}, {}, {}

    # Generate plots
    histogram = alt.Chart(df_filtered).mark_bar().encode(
        alt.X('salary_in_usd:Q', bin=True),
        alt.Y('count()')
    )

    scatter = alt.Chart(df_filtered).mark_point().encode(
        x=alt.X('salary_in_usd:Q'),
        y=alt.Y('work_year:O'),
        tooltip=['job_title', 'salary_in_usd']
    )

    line_chart = alt.Chart(df_filtered).mark_line().encode(
        x=alt.X('work_year:O', title='Year'),
        y=alt.Y('mean(salary_in_usd):Q', title='Average Salary'),
        color='job_title:N'
    )

    return histogram.to_dict(), scatter.to_dict(), line_chart.to_dict()

if __name__ == '__main__':
    app.run(debug=True)
