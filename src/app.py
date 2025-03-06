from dash import Dash, dash_table, dcc, callback, Input, Output, html
import dash_bootstrap_components as dbc
import dash_vega_components as dvc
from vega_datasets import data
import pandas as pd
import altair as alt

# Load dataset
df = pd.read_csv("data/processed/processed_global_data_salary.csv")

# Convert salary to numeric and filter necessary columns
df['salary_in_usd'] = pd.to_numeric(df['salary_in_usd'], errors='coerce')
df = df[['work_year', 'job_title', 'experience_level', 'employment_type', 'company_location', 'company_size', 'salary_in_usd', 'remote_ratio']]

# Initialize Dash app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server
# Components
title = html.H1(
    '💰DataSalaries - Salary Insights for Data Professionals',
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
    style={'width': '100%'},
)

# Bar chart for average salary by experience level 
salary_by_experience_level = dvc.Vega(
    id='salary-by-experience-level',
    opt={'actions': False},
    style={'width': '100%'}
)

# Pie chart for average salary by company size
salary_by_company_size = dvc.Vega(
    id='salary-by-company-size',
    opt={'actions': False},
    style={'width': '50%', 'margin-left': '50px'}
)

# Pie chart for average salary by remote type
salary_by_remote_type = dvc.Vega(
    id='salary-by-remote-type',
    opt={'actions': False},
    style={'width': '50%', 'margin-left': '50px'}
)

# Map chart for average salary by company location
salary_map = dvc.Vega(
    id='salary-map',
    opt={'actions': False},
    style={'width': '100%'}
)

# Sidebar with filters
exp_level_order = ["Entry-level/Junior", "Mid-level", "Senior-level", "Executive-level"]
remote_type_order = ["On-site", "Hybrid", "Fully Remote"]

sidebar = dbc.Col([
    html.H5('Filters', style={'font-weight': 'bold'}),
    html.Br(),
    html.Label("Job Title", style={'font-weight': 'bold'}),
    dcc.Checklist(
        id='job_filter',
        options=[{'label': html.Span(job, style={'margin-left': '10px'}), 'value': job} for job in df['job_title'].dropna().unique()],
        inline=False
    ),
    html.Br(),
    html.Label("Experience Level", style={'font-weight': 'bold'}),
    dcc.Checklist(
        id='exp_level_filter',
        options=[{'label': html.Span(exp_level, style={'margin-left': '10px'}), 'value': exp_level} for exp_level in exp_level_order],
        inline=False,
    ),
    html.Br(),
    html.Label("Employment Type", style={'font-weight': 'bold'}),
    dcc.Checklist(
        id='emp_type_filter',
        options=[{'label': html.Span(emp_type, style={'margin-left': '10px'}), 'value': emp_type} for emp_type in df['employment_type'].dropna().unique()],
        inline=False,
    ),
    html.Br(),
    html.Label("Remote Type", style={'font-weight': 'bold'}),
    dcc.Checklist(
        id='remote_type_filter',
        options=[{'label': html.Span(remote_type, style={'margin-left': '10px'}), 'value': remote_type} for remote_type in remote_type_order],
        inline=False,
    ),
],
    md=3,
    style={
        'background-color': '#E6E6E6',
        'padding': 10,
        'border-radius': 3,
    }
)

# Footer
footer = html.Footer(
    [
        html.Hr(), 
        html.P("📊DataSalaries Dashboard designed to provide salary trends and insights across various data-related roles by visualizing salary based on job title, experience level, and employment details!", style={'font-size': '14px'}),
        html.P("👨‍💻Created by Group 19 - Jessie Zhang, Tianjiao Jiang, Rashid Mammadov, Karlygash Zhakupbayeva | ", style={'font-size': '14px', 'display': 'inline'}),
        html.A("🔗GitHub Repo", href="https://github.com/UBC-MDS/DSCI-532-2025-19-DataSalaries", target="_blank", style={'font-size': '14px', 'color': 'blue', 'display': 'inline'}),
        html.P(" | 📅Last updated: February 28, 2025", style={'font-size': '14px', 'display': 'inline'}),
    ],
    style={
        'text-align': 'center',
        'padding': '10px',
        'background-color': '#f8f9fa',
        'border-top': '1px solid #ddd',
        'margin-top': '20px'
    }
)

# Layout
app.layout = dbc.Container([
    dbc.Row(dbc.Col(title)),
    dbc.Row([
        sidebar,
        dbc.Col([
            dbc.Row([
                dbc.Col(salary_trend, md=7),
                dbc.Col(salary_by_company_size, md=3)
            ]), 
            dbc.Row([
                dbc.Col(salary_by_experience_level, md=7),
                dbc.Col(salary_by_remote_type, md=3)
            ]),
            dbc.Row([
                dbc.Col(salary_map, md=12)
            ]),
        ])
    ]),
    footer
])

@callback(
    Output('salary-trend', "spec"),
    Output('salary-by-experience-level', "spec"),
    Output('salary-by-company-size', "spec"),
    Output('salary-by-remote-type', "spec"),
    Output('salary-map', "spec"), 
    Input('job_filter', "value"),
    Input('exp_level_filter', "value"),
    Input('emp_type_filter', "value"),
    Input('remote_type_filter', "value")
)
def update_charts(selected_jobs, selected_exp_levels, selected_emp_types, selected_remote_types):
    # Filter data based on selected filters
    df_filtered = df.copy()
    if selected_jobs:
        df_filtered = df_filtered[df_filtered['job_title'].isin(selected_jobs)]
    if selected_exp_levels:
        df_filtered = df_filtered[df_filtered['experience_level'].isin(selected_exp_levels)]
    if selected_emp_types:
        df_filtered = df_filtered[df_filtered['employment_type'].isin(selected_emp_types)]
    if selected_remote_types:
        df_filtered = df_filtered[df_filtered['remote_ratio'].isin(selected_remote_types)]
    
    # **Trend Line Chart** - Average Salary per Year or by Job Title
    if not selected_jobs:
        # If no job title selected, show average salary per year
        avg_salary_per_year = df_filtered.groupby('work_year', as_index=False)['salary_in_usd'].mean()
        salary_trend_chart = alt.Chart(avg_salary_per_year).mark_line().encode(
            x=alt.X('work_year:O', title=None, axis=alt.Axis(labelAngle=0)),
            y=alt.Y('salary_in_usd:Q', title=None, axis=alt.Axis(grid=False)),
            tooltip=['salary_in_usd']
        ).properties(
            width=550,
            height=370,
            title="Average Salary Trend Over Year, USD"
        )

        points = alt.Chart(avg_salary_per_year).mark_point(size=60, filled=True, color='coral').encode(
            x='work_year:O',
            y='salary_in_usd:Q'
        )
        
        text_labels = alt.Chart(avg_salary_per_year).mark_text(
            align='center', dy=25, fontSize=12, color="black"
        ).encode(
            x='work_year:O',
            y='salary_in_usd:Q',
            text=alt.Text('salary_in_usd:Q', format=',.0f')
        )
        salary_trend_chart = (salary_trend_chart + points + text_labels).configure_view(stroke=None)
    else:
        # If job titles are selected, show salary trend by job title
        salary_trend_data = df_filtered.groupby(['work_year', 'job_title'], as_index=False)['salary_in_usd'].mean()
        salary_trend_chart = alt.Chart(salary_trend_data).mark_line().encode(
            x=alt.X('work_year:O', title=None, axis=alt.Axis(labelAngle=0)),
            y=alt.Y('salary_in_usd:Q', title=None, axis=alt.Axis(grid=False)),
            color=alt.Color('job_title:N', legend=alt.Legend(title=None, orient="top")),
            tooltip=[alt.Tooltip('job_title', title="Job Title"),
                    alt.Tooltip('work_year', title="Year"),
                    alt.Tooltip('salary_in_usd:Q', format="$,.0f", title="Avg Salary (USD)")]
        ).properties(
            width=550,
            height=370,
            title="Average Salary Trend by Job Titles, USD"
        ).configure_view(
            stroke=None
        )
    
    # Bar Chart: Average Salary by Experience Level Over Time (Half-width)
    salary_by_experience_level_chart = alt.Chart(df_filtered).mark_bar().encode(
        x=alt.X('experience_level:N', axis=None, sort=['Entry-level/Junior', 'Mid-level', 'Senior-level', 'Executive-level']),  
        y=alt.Y('mean(salary_in_usd):Q', title=None, axis=alt.Axis(grid=False)),  
        color=alt.Color(
            'experience_level:N', 
            legend=alt.Legend(title=None, orient="top", offset=10),  
            sort=['Entry-level/Junior', 'Mid-level', 'Senior-level', 'Executive-level']  
        ),
        column=alt.Column('work_year:N', title=None, header=alt.Header(labelOrient="bottom")),  
        tooltip=[alt.Tooltip('work_year', title="Year"),
                alt.Tooltip('experience_level', title="Experience Level"),
                alt.Tooltip('mean(salary_in_usd):Q', format="$,.0f", title="Avg Salary (USD)")]  
    ).properties(
        width=90,
        height=400,
        title=alt.TitleParams(
            text="Average Salary by Experience Level, USD",
            anchor="middle"  
        )
    ).configure_header(
        labelFontSize=12,
        titleFontSize=16
    )
    
    salary_by_company_size_data = df_filtered.groupby(['company_size'] , as_index=False)['salary_in_usd'].mean()
    # Donut Chart: Average Salary by Company Size
    company_size_labels = {
    'L': 'Large (251+)',
    'M': 'Medium (51-250)',
    'S': 'Small (1-50)'
    }

    salary_by_company_size_data['company_size'] = salary_by_company_size_data['company_size'].map(company_size_labels)
    salary_by_company_size_data['percentage'] = (
    salary_by_company_size_data['salary_in_usd'] / salary_by_company_size_data['salary_in_usd'].sum()
    ) * 100


    salary_by_company_size_chart = alt.Chart(salary_by_company_size_data).mark_arc(innerRadius=80).encode(
        theta=alt.Theta('salary_in_usd:Q', title="Average Salary"),  
        color=alt.Color('company_size:N', 
            scale=alt.Scale(scheme="blues"), legend=alt.Legend(title=None, orient="top", offset=-20),
            sort=['Small (1-50)', 'Medium (51-250)', 'Large (251+)']
        ), 
        tooltip=[alt.Tooltip('company_size', title="Company Size"),
                alt.Tooltip('salary_in_usd:Q', format="$,.0f", title="Avg Salary (USD)"), 
                alt.Tooltip('percentage:Q', format=".1f", title="Percentage (%)")]
    ).properties(
        width=300,  
        height=400,
        title=alt.TitleParams(
            text="Average Salary by Company Size, USD",
            anchor="middle"
        )
    )

    salary_by_remote_ratio_data = df_filtered.groupby('remote_ratio', as_index=False)['salary_in_usd'].mean()
    salary_by_remote_ratio_data['total_salary'] = salary_by_remote_ratio_data['salary_in_usd'].sum()
    salary_by_remote_ratio_data['percentage'] = (salary_by_remote_ratio_data['salary_in_usd'] / salary_by_remote_ratio_data['total_salary']) * 100

    # Pie Chart: Average Salary by Remote Type
    salary_by_remote_ratio_chart = alt.Chart(salary_by_remote_ratio_data).mark_arc(innerRadius=80).encode(
        theta=alt.Theta('salary_in_usd:Q', title="Average Salary"),
        color=alt.Color('remote_ratio:N', scale=alt.Scale(scheme="oranges"), legend=alt.Legend(title=None, orient="top", offset=-20),
            sort=['On-site', 'Hybrid', 'Fully Remote']),
        tooltip=[alt.Tooltip('remote_ratio', title="Remote Type"),
                alt.Tooltip('salary_in_usd:Q', format="$,.0f", title="Avg Salary (USD)"),
                alt.Tooltip('percentage:Q', format=".1f", title="Percentage (%)")
                ]
    ).properties(
        width=300,
        height=400,
        title=alt.TitleParams(
            text="Average Salary by Remote Type, USD",
            anchor="middle"
        )
    )

    # Map Visualization: Average Salary by Company Location
    avg_salary_by_country = df_filtered.groupby('company_location', as_index=False)['salary_in_usd'].mean()
    country_mapping = {
    'Australia': 36, 'United States': 840, 'Ireland': 372, 'Portugal': 620, 'United Kingdom': 826,
    'Germany': 276, 'India': 356, 'Spain': 724, 'Netherlands': 528, 'Canada': 124, 'Ukraine': 804,
    'Italy': 380, 'Vietnam': 704, 'Mexico': 484, 'Poland': 616, 'Egypt': 818, 'Denmark': 208,
    'Honduras': 340, 'Colombia': 170, 'Armenia': 51, 'Central African Republic': 140, 'Philippines': 608,
    'Lithuania': 440, 'Russia': 643, 'New Zealand': 554, 'Japan': 392, 'France': 250, 'South Africa': 710,
    'Slovenia': 705, 'Estonia': 233, 'Greece': 300, 'Brazil': 76, 'Switzerland': 756, 'Austria': 40,
    'Malaysia': 458, 'Sweden': 752, 'Malta': 470, 'Luxembourg': 442, 'Argentina': 32, 'Nigeria': 566,
    'Ecuador': 218, 'Ghana': 288, 'Finland': 246, 'United Arab Emirates': 784, 'Romania': 642,
    'American Samoa': 16, 'Singapore': 702, 'Latvia': 428, 'Belgium': 56, 'Turkey': 792, 'Thailand': 764,
    'Pakistan': 586, 'South Korea': 410, 'Israel': 376, 'Iraq': 368
    }

    # Apply mapping
    avg_salary_by_country['id'] = avg_salary_by_country['company_location'].map(country_mapping).astype(int)
    # Base map with country outlines
    base_map = alt.Chart(alt.topo_feature('https://cdn.jsdelivr.net/npm/world-atlas@2/countries-110m.json', 'countries')).mark_geoshape(
        stroke='white',
        fill='lightgrey'
    ).project(
        type='naturalEarth1'
    ).properties(
        width=800,
        height=500,
        title=alt.TitleParams(
            text="Average Salary by Country, USD",
            anchor="middle"
        )

    )

    # Choropleth (color-coded country salaries)
    salary_for_map = alt.Chart(alt.topo_feature('https://cdn.jsdelivr.net/npm/world-atlas@2/countries-110m.json', 'countries')).mark_geoshape().encode(
        color=alt.Color('salary_in_usd:Q', scale=alt.Scale(scheme="blues"), legend=alt.Legend(title=None)),
        tooltip=[alt.Tooltip('company_location:N', title="Country"),
             alt.Tooltip('salary_in_usd:Q', format="$,.0f", title="Avg Salary (USD)")]
    ).transform_lookup(
        lookup='id',
        from_=alt.LookupData(avg_salary_by_country, 'id', ['salary_in_usd', 'company_location'])
    )

    # Combine map layers
    map_chart = base_map + salary_for_map
   
    return (
        salary_trend_chart.to_dict(),
        salary_by_experience_level_chart.to_dict(),
        salary_by_company_size_chart.to_dict(),
        salary_by_remote_ratio_chart.to_dict(),
        map_chart.to_dict()
    )

if __name__ == '__main__':
    app.run(debug=True)








