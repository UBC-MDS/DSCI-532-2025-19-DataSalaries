from dash import html, dcc, Dash
import dash_bootstrap_components as dbc
from .components import sidebar, footer, title, collapse_button, collapse_section
from .components.charts import (
    salary_trend, salary_by_experience_level, salary_by_company_size,
    salary_by_remote_type, salary_by_location
)
from .callbacks import update_charts, update_button
from .data import load_clean_data

# Initialize Dash app
app = Dash(
    __name__, 
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    assets_folder="assets"
)

server = app.server

df = load_clean_data()
# Define tabs
tabs = dbc.Tabs(
    [
        dbc.Tab(
            label="📈 Salary Trends",
            tab_id="tab-trend",
            children=[
                dbc.Row(
                    dbc.Col(
                        dbc.Card([
                            dbc.CardHeader("Salary Trend Over Time, USD", className="card-header"),
                            dbc.CardBody(salary_trend, className="chart-card-body")
                        ], className="mb-4"), md=12
                    )
                ),
                dbc.Row(
                    dbc.Col(
                        dbc.Card([
                            dbc.CardHeader("Average Salary by Experience Level, USD", className="card-header"),
                            dbc.CardBody(salary_by_experience_level, className="chart-card-body")
                        ], className="mb-4"), md=12
                    )
                )
            ]
        ),
        dbc.Tab(
            label="🌍 Salary by Location & Company Factors",
            tab_id="tab-location",
            children=[
                dbc.Row(
                    dbc.Col(
                        dbc.Card([
                             dbc.CardHeader(
                                     dbc.Row([
                                        dbc.Col(html.Span("Average Salary by Location, USD", className="card-header-text"), width="auto"),
                                        dbc.Col(
                                             dcc.Dropdown(
                                                id="year_filter",
                                                options=[{"label": str(year), "value": year} for year in sorted(df["work_year"].unique())],
                                                value=df["work_year"].max(),
                                                clearable=False,
                                                className="chart-dropdown",
                                                ), width="auto", className="dropdown-container"
                                            )
                                        ], align="center", justify="center"),
                                    className="card-header"
                                ),
                            dbc.CardBody(salary_by_location, className="chart-card-body")
                        ], className="mb-4"), md=12
                    )
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            dbc.Card([
                                dbc.CardHeader("Average Salary by Company Size, USD", className="card-header"),
                                dbc.CardBody(salary_by_company_size, className="chart-card-body")
                            ], className="mb-4"), md=6
                        ),
                        dbc.Col(
                            dbc.Card([
                                dbc.CardHeader("Average Salary by Remote Type, USD", className="card-header"),
                                dbc.CardBody(salary_by_remote_type, className="chart-card-body")
                            ], className="mb-4"), md=6
                        )
                    ]
                )
            ]
        )
    ],
    id="tabs",
    active_tab="tab-trend",
    className="custom-tabs"
)

# App Layout
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            title,
            collapse_section
        ]),
        dbc.Col(
            collapse_button,
            md=3,
        )
    ], className="headerbg"),
    
    dbc.Row([
        sidebar,
        dbc.Col(
            [
                tabs, 
                html.Div(id="tab-content")
            ], md=9
        )
    ]),
    footer
])

if __name__ == '__main__':
    app.run_server(debug=False)