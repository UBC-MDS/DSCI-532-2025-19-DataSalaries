from dash import dcc, html
import dash_bootstrap_components as dbc
from ..data import load_clean_data

exp_level_order = ["Entry-level/Junior", "Mid-level", "Senior-level", "Executive-level"]
remote_type_order = ["On-site", "Hybrid", "Fully Remote"]
df = load_clean_data()

sidebar = dbc.Col([
        html.Br(),
        # Add job title checklist
        html.Label("Job Title", style={'font-weight': 'bold'}),
        dcc.Checklist(
            id='job_filter',
            options=[{'label': html.Span(job, style={'margin-left': '10px'}), 'value': job} for job in sorted(df['job_title'].dropna().unique())],
            inline=False
        ),
        html.Br(),
        # Add location country dropdown
        html.Label("Company Location", style={'font-weight': 'bold'}),
        dcc.Dropdown(
            id='company_location_filter',
            options=[{'label': country, 'value': country} for country in sorted(df['company_location'].dropna().unique())],
            multi=True,
            placeholder="Select Company Location(s)"
        ),
        html.Br(),
        # Add experience level checklist
        html.Label("Experience Level", style={'font-weight': 'bold'}),
        dcc.Checklist(
            id='exp_level_filter',
            options=[{'label': html.Span(exp_level, style={'margin-left': '10px'}), 'value': exp_level} for exp_level in exp_level_order],
            inline=False,
        ),
        html.Br(),
        # Add employment type checklist
        html.Label("Employment Type", style={'font-weight': 'bold'}),
        dcc.Checklist(
            id='emp_type_filter',
            options=[{'label': html.Span(emp_type, style={'margin-left': '10px'}), 'value': emp_type} for emp_type in df['employment_type'].dropna().unique()],
            inline=False,
        ),
        html.Br(),
        # Add remote type checklist
        html.Label("Remote Type", style={'font-weight': 'bold'}),
        dcc.Checklist(
            id='remote_type_filter',
            options=[{'label': html.Span(remote_type, style={'margin-left': '10px'}), 'value': remote_type} for remote_type in remote_type_order],
            inline=False,
        ),
        html.Br(),
        # Add Disclaimer
        html.Div([
            html.Strong("Disclaimer: "), 
            "The dataset used in this dashboard is sourced from publicly available salary data. "
            "It may not be exhaustive and should be interpreted with caution."
            ], style={
                "fontSize": "13px",
                "color": "gray",
                "marginTop": "10px",
                "textAlign": "left"
            }),       
    ],
        md=3,
        style={
            'background-color': '#E6E6E6',
            'padding': 10,
            'border-radius': 3,
        }
    )